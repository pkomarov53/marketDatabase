from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox


class SearchDialogById(QDialog):
    def __init__(self):
        super(SearchDialogById, self).__init__()
        self.setWindowTitle("Введите идентификатор для поиска")
        self.layout = QVBoxLayout(self)
        self.id_label = QLabel("Идентификатор записи:")
        self.id_text = QLineEdit()
        self.layout.addWidget(self.id_label)
        self.layout.addWidget(self.id_text)
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_search_id(self):
        return self.id_text.text()
