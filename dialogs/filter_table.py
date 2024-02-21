from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class FilterDialog(QDialog):
    def __init__(self):
        super(FilterDialog, self).__init__()
        self.setWindowTitle("Введите значение для фильтрации")
        self.layout = QVBoxLayout(self)
        self.value_label = QLabel("Значение для фильтрации:")
        self.value_text = QLineEdit()
        self.layout.addWidget(self.value_label)
        self.layout.addWidget(self.value_text)
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_filter_value(self):
        return self.value_text.text()
