from PySide6.QtWidgets import QDialog, QVBoxLayout, QRadioButton, QDialogButtonBox


class ExportDialog(QDialog):
    def __init__(self):
        super(ExportDialog, self).__init__()
        self.setWindowTitle("Выберите формат экспорта")
        self.layout = QVBoxLayout(self)
        self.csv_radio = QRadioButton("CSV")
        self.sqlite_radio = QRadioButton("SQLite")
        self.layout.addWidget(self.csv_radio)
        self.layout.addWidget(self.sqlite_radio)
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_export_format(self):
        return "csv" if self.csv_radio.isChecked() else "sqlite" if self.sqlite_radio.isChecked() else None
