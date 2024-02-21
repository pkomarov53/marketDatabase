from PySide6.QtWidgets import QDialog, QFormLayout, QLabel, QComboBox, QLineEdit, QDialogButtonBox, QDateTimeEdit


class AddRecordDialog(QDialog):
    def __init__(self, column_names, user_ids, product_names, is_delivery=False):
        super(AddRecordDialog, self).__init__()
        self.setWindowTitle("Добавить запись")
        self.layout = QFormLayout(self)
        self.widgets = {}

        for column_name in column_names:
            if column_name.lower() == "id":
                continue  # Skip the 'id' field in the dialog

            label = QLabel(column_name)

            if column_name.lower() == "user_id" and user_ids:
                combo_box = QComboBox()
                sorted_user_ids = sorted(set(str(user_id) for user_id in user_ids))
                combo_box.addItems(sorted_user_ids)
                self.widgets[column_name] = combo_box
            elif column_name.lower() == "product_name" and product_names and not is_delivery:
                combo_box = QComboBox()
                sorted_product_names = sorted(set(product_names))
                combo_box.addItems(sorted_product_names)
                self.widgets[column_name] = combo_box
            else:
                line_edit = QLineEdit()
                self.widgets[column_name] = line_edit

            self.layout.addRow(label, self.widgets[column_name])

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_record_data(self):
        record_data = {
            column: widget.dateTime().toString("yyyy-MM-dd HH:mm:ss") if isinstance(widget, QDateTimeEdit)
            else (widget.currentText() if isinstance(widget, QComboBox) else widget.text())
            for column, widget in self.widgets.items() if column.lower() != "id"  # Exclude 'id' field
        }
        return record_data
