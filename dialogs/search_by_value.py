from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QLineEdit, QDialogButtonBox


class SearchDialogByValue(QDialog):
    def __init__(self, column_names):
        super(SearchDialogByValue, self).__init__()
        self.setWindowTitle("Введите значение для поиска")
        self.layout = QVBoxLayout(self)
        self.column_label = QLabel("Выберите столбец:")
        self.column_combo = QComboBox()
        self.column_combo.addItems(column_names)
        self.value_label = QLabel("Искомое значение:")
        self.value_text = QLineEdit()
        self.layout.addWidget(self.column_label)
        self.layout.addWidget(self.column_combo)
        self.layout.addWidget(self.value_label)
        self.layout.addWidget(self.value_text)
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_search_criteria(self):
        column_name = self.column_combo.currentText()
        search_value = self.value_text.text()
        return column_name, search_value
