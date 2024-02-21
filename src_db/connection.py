import sqlite3
from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery


def create_database():
    # Инициализация базы данных
    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("src_db/market.sqlite")

    conn = sqlite3.connect("src_db/market.sqlite")
    cursor = conn.cursor()

    # Таблица для пользователей в системе приложения
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS db_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )''')

    # Таблица для покупателей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            loyalty_Card_Number TEXT,
            bank_Card_Number TEXT
        )''')

    # Таблица для продуктов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            SKU TEXT,
            category TEXT,
            expiration_date DATE,
            description TEXT
        )''')

    # Таблица для поставок
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Deliveries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            supplier TEXT,
            quantity INTEGER,
            delivery_date DATE,
            FOREIGN KEY (product_name) REFERENCES Products(product_name)
        )''')

    # Таблица для покупок
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_name TEXT,
            quantity INTEGER,
            purchase_time TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(id),
            FOREIGN KEY (product_name) REFERENCES Products(product_name)
        )''')

    conn.commit()
    conn.close()

    if not db.open():
        QMessageBox.critical(None, "Ошибка", "Не удалось открыть базу данных")


def check_user_credentials(username, password):
    model = QSqlTableModel()
    model.setTable("db_users")
    model.setFilter(f"username = '{username}' AND password = '{password}'")
    model.select()

    return model.rowCount() > 0


def add_user_to_database(username, password):
    model = QSqlTableModel()
    model.setTable("db_users")
    record = model.record()
    record.setValue("username", username)
    record.setValue("password", password)
    model.insertRecord(-1, record)

    return model.submitAll()


def get_product_names():
    query = QSqlQuery()
    query.exec("SELECT product_name FROM Deliveries")
    product_names = []
    while query.next():
        product_names.append(str(query.value(0)))
    return product_names


def get_user_ids():
    query = QSqlQuery()
    query.exec("SELECT id FROM Users")
    user_ids = []
    while query.next():
        user_ids.append(str(query.value(0)))
    return user_ids
