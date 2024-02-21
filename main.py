from PySide6.QtWidgets import QApplication

from user_interface.view import MainWindow

if __name__ == '__main__':
    application_view = QApplication([])

    user_view = MainWindow()
    user_view.show()

    application_view.exec()
