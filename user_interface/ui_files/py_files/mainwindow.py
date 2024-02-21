# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QPushButton,
    QSizePolicy, QSplitter, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(602, 554)
        MainWindow.setMinimumSize(QSize(602, 554))
        MainWindow.setMaximumSize(QSize(602, 554))
        icon = QIcon()
        icon.addFile(u"../../src_img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(191, 185, 182);")
        self.database_tableView = QTableView(MainWindow)
        self.database_tableView.setObjectName(u"database_tableView")
        self.database_tableView.setGeometry(QRect(10, 120, 581, 381))
        self.database_tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableManipulate_group = QSplitter(MainWindow)
        self.tableManipulate_group.setObjectName(u"tableManipulate_group")
        self.tableManipulate_group.setGeometry(QRect(10, 60, 581, 52))
        self.tableManipulate_group.setMinimumSize(QSize(0, 52))
        self.tableManipulate_group.setMaximumSize(QSize(16777215, 27))
        self.tableManipulate_group.setOrientation(Qt.Horizontal)
        self.add_button = QPushButton(self.tableManipulate_group)
        self.add_button.setObjectName(u"add_button")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.add_button.setFont(font)
        self.tableManipulate_group.addWidget(self.add_button)
        self.remove_button = QPushButton(self.tableManipulate_group)
        self.remove_button.setObjectName(u"remove_button")
        self.remove_button.setFont(font)
        self.tableManipulate_group.addWidget(self.remove_button)
        self.tableView_group = QSplitter(MainWindow)
        self.tableView_group.setObjectName(u"tableView_group")
        self.tableView_group.setGeometry(QRect(10, 11, 581, 40))
        self.tableView_group.setMinimumSize(QSize(0, 40))
        self.tableView_group.setMaximumSize(QSize(16777215, 23))
        self.tableView_group.setOrientation(Qt.Horizontal)
        self.usersView_button = QPushButton(self.tableView_group)
        self.usersView_button.setObjectName(u"usersView_button")
        self.tableView_group.addWidget(self.usersView_button)
        self.purchaseView_button = QPushButton(self.tableView_group)
        self.purchaseView_button.setObjectName(u"purchaseView_button")
        self.tableView_group.addWidget(self.purchaseView_button)
        self.productView_button = QPushButton(self.tableView_group)
        self.productView_button.setObjectName(u"productView_button")
        self.tableView_group.addWidget(self.productView_button)
        self.supplyView_button = QPushButton(self.tableView_group)
        self.supplyView_button.setObjectName(u"supplyView_button")
        self.tableView_group.addWidget(self.supplyView_button)
        self.return_button = QPushButton(MainWindow)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(260, 520, 75, 23))
        icon1 = QIcon()
        icon1.addFile(u"src_img/return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.return_button.setIcon(icon1)
        self.return_button.setAutoDefault(True)
        self.return_button.setFlat(False)

        self.retranslateUi(MainWindow)

        self.return_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u0417\u0410\u041f\u0418\u0421\u042c", None))
        self.remove_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0414\u0410\u041b\u0418\u0422\u042c \u0417\u0410\u041f\u0418\u0421\u042c", None))
        self.usersView_button.setText(QCoreApplication.translate("MainWindow", u"\u00ab\u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0438\u00bb", None))
        self.purchaseView_button.setText(QCoreApplication.translate("MainWindow", u"\u00ab\u041f\u043e\u043a\u0443\u043f\u043a\u0438\u00bb", None))
        self.productView_button.setText(QCoreApplication.translate("MainWindow", u"\u00ab\u041f\u0440\u043e\u0434\u0443\u043a\u0442\u044b\u00bb", None))
        self.supplyView_button.setText(QCoreApplication.translate("MainWindow", u"\u00ab\u041f\u043e\u0441\u0442\u0430\u0432\u043a\u0438\u00bb", None))
        self.return_button.setText("")
    # retranslateUi

