import csv
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMessageBox, QMainWindow, QDialog, QAbstractItemView, QFileDialog, QMenu, \
    QHeaderView
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from dialogs.export_table import ExportDialog
from dialogs.filter_table import FilterDialog
from dialogs.search_by_value import SearchDialogByValue
from dialogs.search_by_id import SearchDialogById
from dialogs.add_record import AddRecordDialog
from conditions.build_search_condition import build_search_condition_by_value
from user_interface.ui_files.py_files.login import Ui_LoginScreen
from user_interface.ui_files.py_files.reg import Ui_RegistrationScreen
from user_interface.ui_files.py_files.mainwindow import Ui_MainWindow
from src_db.connection import create_database, check_user_credentials, add_user_to_database, get_product_names, \
    get_user_ids


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        create_database()
        self.ui_login = Ui_LoginScreen()
        self.ui_registration = Ui_RegistrationScreen()
        self.ui_main = Ui_MainWindow()

        self.ui_login.setupUi(self)
        self.ui_registration_dialog = QDialog()
        self.ui_registration.setupUi(self.ui_registration_dialog)
        self.ui_main_window = QDialog()
        self.ui_main.setupUi(self.ui_main_window)

        self.ui_login.incorrect_data_label.hide()
        self.ui_login.login_button.setDefault(True)
        self.ui_login.login_text.returnPressed.connect(self.ui_login.login_button.click)
        self.ui_login.password_text.returnPressed.connect(self.ui_login.login_button.click)

        self.ui_main.supplyView_button.clicked.connect(self.show_supply_data_in_table)
        self.ui_main.usersView_button.clicked.connect(self.show_user_data_in_table)
        self.ui_main.purchaseView_button.clicked.connect(self.show_purchases_data_in_table)
        self.ui_main.productView_button.clicked.connect(self.show_product_data_in_table)
        self.ui_main.add_button.clicked.connect(self.add_record)

        self.ui_login.reg_button.clicked.connect(self.open_registration_window)

        self.ui_login.login_button.clicked.connect(self.open_database_window)
        self.ui_main.database_tableView.setSortingEnabled(True)

        self.ui_registration.return_button.clicked.connect(self.open_login_screen)
        self.ui_registration.reg_button.clicked.connect(self.on_register_click)

        self.ui_main.return_button.clicked.connect(self.open_login_screen)

        self.ui_main.remove_button.clicked.connect(self.delete_record)

        self.show_purchases_data_in_table()

    def open_login_screen(self):
        self.ui_registration_dialog.close()
        self.ui_main_window.close()
        self.show()

    def open_registration_window(self):
        self.ui_registration_dialog.show()

    def open_database_window(self):
        username = self.ui_login.login_text.text()
        password = self.ui_login.password_text.text()

        if len(username) < 4 or len(password) <= 5:
            self.ui_login.incorrect_data_label.show()
        else:
            self.ui_login.incorrect_data_label.hide()

            if check_user_credentials(username, password):
                self.ui_main_window.show()
                self.close()
            else:
                self.ui_login.incorrect_data_label.show()

    def on_register_click(self):
        user_login = self.ui_registration.login_regtext.text()
        user_password = self.ui_registration.password_regtext.text()

        if len(user_login) >= 4 and len(user_password) >= 5:
            if add_user_to_database(user_login, user_password):
                print('Пользователь успешно зарегистрирован')
                self.ui_registration_dialog.close()
            else:
                QMessageBox.critical(None, "Ошибка", "Не удалось зарегистрировать пользователя")
        else:
            print('Error')

    def show_purchases_data_in_table(self):
        self.show_data_in_table("Purchases")
        self.setup_context_menu()

    def show_user_data_in_table(self):
        self.show_data_in_table("Users")

    def show_supply_data_in_table(self):
        self.show_data_in_table("Deliveries")

    def show_product_data_in_table(self):
        self.show_data_in_table("Products")

    def show_data_in_table(self, table_name, filter_condition=None):
        model = QSqlTableModel()
        model.setTable(table_name)
        model.setSort(0, Qt.AscendingOrder)

        if filter_condition is not None:
            model.setFilter(filter_condition)

        model.select()

        self.ui_main.database_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui_main.database_tableView.verticalHeader().setVisible(False)
        self.ui_main.database_tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui_main.database_tableView.setModel(model)

    def delete_record(self):
        selected_rows = self.ui_main.database_tableView.selectionModel().selectedRows()

        if selected_rows:
            ids_to_delete = [selected_row.siblingAtColumn(0).data() for selected_row in selected_rows]
            current_table = self.ui_main.database_tableView.model().tableName()

            query = QSqlQuery()
            query.prepare(f"DELETE FROM {current_table} WHERE id IN ({', '.join(map(str, ids_to_delete))})")

            if query.exec():
                reset_query = QSqlQuery()
                reset_query.exec(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{current_table}'")

                QMessageBox.information(None, "Success", "Records deleted successfully.")
                self.ui_main.database_tableView.model().select()
            else:
                QMessageBox.critical(None, "Error", "Failed to delete records.")
        else:
            QMessageBox.warning(None, "Warning", "Select records to delete.")

    def add_record(self):
        current_table = self.ui_main.database_tableView.model().tableName()

        # Получаем имена столбцов, кроме столбца id
        column_names = [self.ui_main.database_tableView.model().headerData(i, Qt.Horizontal) for i in
                        range(self.ui_main.database_tableView.model().columnCount())]

        # Получаем список user_id из таблицы Users, если столбец user_id существует
        user_ids = get_user_ids() if "user_id" in column_names else []

        # Получаем список product_name из таблицы Products, если столбец product_name существует
        product_names = get_product_names() if "product_name" in column_names else []

        if current_table != 'Deliveries':
            add_record_dialog = AddRecordDialog(column_names, user_ids, product_names)
        else:
            add_record_dialog = AddRecordDialog(column_names, user_ids, product_names, True)

        if add_record_dialog.exec() == QDialog.Accepted:
            record_data = add_record_dialog.get_record_data()

            # Строим строку SQL для вставки записи без указания id
            columns = ', '.join(record_data.keys())
            values = ', '.join([f"'{value}'" for value in record_data.values()])
            sql_query = f"INSERT INTO {current_table} ({columns}) VALUES ({values})"

            # Выполняем SQL-запрос
            query = QSqlQuery()
            query.prepare(sql_query)

            if query.exec():
                QMessageBox.information(None, "Успех", "Запись добавлена успешно.")
                self.ui_main.database_tableView.model().select()
            else:
                QMessageBox.critical(None, "Ошибка", "Не удалось добавить запись.")
        else:
            QMessageBox.warning(None, "Предупреждение", "Добавление записи отменено пользователем.")

    def save_cell(self, row, column, new_value):
        record_id = self.ui_main_window.database.item(row, 0).text()
        field_name = self.tableWidget.horizontalHeaderItem(column).text()

        table_name = "your_table_name"
        new_data = {field_name: new_value}
        self.update_record(table_name, record_id, new_data)

    def reload_table(self):
        current_table = self.ui_main.database_tableView.model().tableName()
        self.show_data_in_table(current_table)

    def show_context_menu(self, position):
        menu = QMenu(self.ui_main.database_tableView)

        title_action = QAction("ЗАПРОСЫ")
        title_action.setEnabled(False)
        menu.addAction(title_action)

        action1 = menu.addAction("1. Вывод таблицы")
        action2 = menu.addAction("2. Фильтр по значению атрибута")
        action3 = menu.addAction("3. Поиск записи по идентификатору")
        action4 = menu.addAction("4. Поиск по значению ячейки")
        action5 = menu.addAction("Обновить таблицу")

        action1.triggered.connect(lambda: self.handle_context_menu_action(1))
        action2.triggered.connect(lambda: self.handle_context_menu_action(2))
        action3.triggered.connect(lambda: self.handle_context_menu_action(3))
        action4.triggered.connect(lambda: self.handle_context_menu_action(4))
        action5.triggered.connect(lambda: self.handle_context_menu_action(5))

        menu.exec(self.ui_main.database_tableView.mapToGlobal(position))

    def handle_context_menu_action(self, action_number):
        if action_number == 1:
            self.export_table()
        elif action_number == 2:
            self.perform_search_by_value()
        elif action_number == 3:
            self.perform_search_by_id()
        elif action_number == 4:
            self.apply_filter()
        elif action_number == 5:
            self.reload_table()

    def setup_context_menu(self):
        self.ui_main.database_tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui_main.database_tableView.customContextMenuRequested.connect(self.show_context_menu)

    def export_table(self):
        model = self.ui_main.database_tableView.model()
        if model is not None:
            export_dialog = ExportDialog()
            if export_dialog.exec() == QDialog.Accepted:
                export_format = export_dialog.get_export_format()
                if export_format == "csv":
                    self.export_table_to_csv(model)
                elif export_format == "sqlite":
                    self.export_table_to_sqlite()
                else:
                    QMessageBox.warning(None, "Предупреждение", "Выберите формат экспорта.")
            else:
                QMessageBox.warning(None, "Предупреждение", "Экспорт отменен.")
        else:
            QMessageBox.warning(None, "Предупреждение", "Таблица пуста.")

    def export_table_to_sqlite(self):
        model = self.ui_main.database_tableView.model()
        if model is not None:
            file_dialog = QFileDialog(self)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("SQLite Files (*.sqlite)")
            file_dialog.setDefaultSuffix("sqlite")

            if file_dialog.exec() == QFileDialog.Accepted:
                new_db_path = file_dialog.selectedFiles()[0]

                new_db = QSqlDatabase.addDatabase("QSQLITE", "export_connection")
                new_db.setDatabaseName(new_db_path)

                if new_db.open():
                    new_query = QSqlQuery(new_db)
                    new_query.exec(f"ATTACH DATABASE '{model.database().databaseName()}' AS source_db")

                    selected_rows = self.ui_main.database_tableView.selectionModel().selectedRows()

                    if selected_rows:
                        ids = [selected_row.siblingAtColumn(0).data() for selected_row in selected_rows]
                        ids_str = ','.join(map(str, ids))
                        new_query.exec(
                            f"CREATE TABLE {model.tableName()} AS SELECT * FROM source_db.{model.tableName()} WHERE "
                            f"id IN ({ids_str})")
                    else:
                        visible_rows = [model.index(row, 0).data() for row in range(model.rowCount()) if
                                        not self.ui_main.database_tableView.isRowHidden(row)]
                        visible_rows_str = ','.join(map(str, visible_rows))
                        new_query.exec(
                            f"CREATE TABLE {model.tableName()} AS SELECT * FROM source_db.{model.tableName()} WHERE "
                            f"id IN ({visible_rows_str})")

                    new_db.close()

                    self.show_data_in_table(model.tableName())

                    QMessageBox.information(None, "Успех", "Таблица успешно экспортирована в SQLite файл.")
                else:
                    QMessageBox.warning(None, "Ошибка", f"Не удалось открыть базу данных: {new_db.lastError().text()}")
            else:
                QMessageBox.warning(None, "Предупреждение", "Экспорт отменен.")
        else:
            QMessageBox.warning(None, "Предупреждение", "Таблица пуста.")

    def export_table_to_csv(self, model):
        file_dialog = QFileDialog(self)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("CSV Files (*.csv)")
        file_dialog.setDefaultSuffix("csv")

        if file_dialog.exec() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]

            with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)

                header = [model.headerData(i, Qt.Horizontal) for i in range(model.columnCount())]
                csv_writer.writerow(header)

                for row in range(model.rowCount()):
                    if not self.ui_main.database_tableView.isRowHidden(row):
                        row_data = [model.data(model.index(row, col)) for col in range(model.columnCount())]
                        csv_writer.writerow(row_data)

            QMessageBox.information(None, "Успех", "Таблица успешно экспортирована в CSV файл.")
        else:
            QMessageBox.warning(None, "Предупреждение", "Экспорт отменен.")

    def apply_filter(self):
        filter_dialog = FilterDialog()
        if filter_dialog.exec() == QDialog.Accepted:
            filter_value = filter_dialog.get_filter_value()
            self.filter_table_by_value(filter_value)
        else:
            QMessageBox.warning(None, "Предупреждение", "Фильтрация отменена пользователем.")

    def filter_table_by_value(self, filter_value):
        model = self.ui_main.database_tableView.model()
        if model is not None:
            selected_column = "all_columns"
            filter_condition = build_search_condition_by_value(model, selected_column, filter_value)
            self.show_data_in_table(model.tableName(), filter_condition)

    def perform_search_by_id(self):
        search_dialog = SearchDialogById()
        if search_dialog.exec() == QDialog.Accepted:
            search_id = search_dialog.get_search_id()

            model = self.ui_main.database_tableView.model()
            if model is not None:
                filter_condition = f"id = {search_id}"
                self.show_data_in_table(model.tableName(), filter_condition)
        else:
            QMessageBox.warning(None, "Предупреждение", "Поиск отменен пользователем.")

    def perform_search_by_value(self):
        search_dialog = SearchDialogByValue(self.get_column_names())
        if search_dialog.exec() == QDialog.Accepted:
            column_name, search_value = search_dialog.get_search_criteria()

            model = self.ui_main.database_tableView.model()
            if model is not None:
                filter_condition = f"{column_name} LIKE '%{search_value}%'"
                self.show_data_in_table(model.tableName(), filter_condition)
        else:
            QMessageBox.warning(None, "Предупреждение", "Поиск отменен пользователем.")

    def get_column_names(self):
        model = self.ui_main.database_tableView.model()
        if model is not None:
            columns = [model.headerData(i, Qt.Horizontal) for i in range(model.columnCount()) if i != 0]
            return columns
        return []

    def get_selected_column(self):
        selected_column_index = self.ui_main.database_tableView.selectionModel().currentIndex().column()
        model = self.ui_main.database_tableView.model()
        if model is not None and 0 <= selected_column_index < model.columnCount():
            return model.headerData(selected_column_index, Qt.Horizontal)
        return None