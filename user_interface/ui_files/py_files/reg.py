# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_RegistrationScreen(object):
    def setupUi(self, RegistrationScreen):
        if not RegistrationScreen.objectName():
            RegistrationScreen.setObjectName(u"RegistrationScreen")
        RegistrationScreen.resize(383, 299)
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/src_img/user.png", QSize(), QIcon.Normal, QIcon.Off)
        RegistrationScreen.setWindowIcon(icon)
        RegistrationScreen.setStyleSheet(u"background-color: rgb(191, 185, 182);\n"
"font-family: NotoSans-Black;")
        self.return_button = QPushButton(RegistrationScreen)
        self.return_button.setObjectName(u"return_button")
        self.return_button.setGeometry(QRect(150, 270, 75, 23))
        icon1 = QIcon()
        icon1.addFile(u"src_img/return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.return_button.setIcon(icon1)
        self.return_button.setAutoDefault(True)
        self.return_button.setFlat(False)
        self.layoutWidget = QWidget(RegistrationScreen)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 40, 235, 195))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.greet_label = QLabel(self.layoutWidget)
        self.greet_label.setObjectName(u"greet_label")
        self.greet_label.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.greet_label)

        self.login_label = QLabel(self.layoutWidget)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setStyleSheet(u"font: 700 8pt \"Tahoma\";")

        self.verticalLayout.addWidget(self.login_label)

        self.login_regtext = QLineEdit(self.layoutWidget)
        self.login_regtext.setObjectName(u"login_regtext")
        self.login_regtext.setAutoFillBackground(False)
        self.login_regtext.setStyleSheet(u"background-color: white;")

        self.verticalLayout.addWidget(self.login_regtext)

        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setStyleSheet(u"font: 700 8pt \"Tahoma\";")

        self.verticalLayout.addWidget(self.password_label)

        self.password_regtext = QLineEdit(self.layoutWidget)
        self.password_regtext.setObjectName(u"password_regtext")
        self.password_regtext.setStyleSheet(u"background-color: white;")
        self.password_regtext.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_regtext.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_regtext)

        self.reg_button = QPushButton(self.layoutWidget)
        self.reg_button.setObjectName(u"reg_button")
        self.reg_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.reg_button.setStyleSheet(u"font: 14pt \"Microsoft JhengHei UI\";")

        self.verticalLayout.addWidget(self.reg_button)


        self.retranslateUi(RegistrationScreen)

        self.return_button.setDefault(False)


        QMetaObject.connectSlotsByName(RegistrationScreen)
    # setupUi

    def retranslateUi(self, RegistrationScreen):
        RegistrationScreen.setWindowTitle(QCoreApplication.translate("RegistrationScreen", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.return_button.setText("")
        self.greet_label.setText(QCoreApplication.translate("RegistrationScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u0414\u041e\u0411\u0410\u0412\u0418\u0422\u042c \u041f\u041e\u041b\u042c\u0417\u041e\u0412\u0410\u0422\u0415\u041b\u042f</span></p></body></html>", None))
        self.login_label.setText(QCoreApplication.translate("RegistrationScreen", u"<html><head/><body><p align=\"center\">\u041b\u043e\u0433\u0438\u043d</p></body></html>", None))
        self.login_regtext.setPlaceholderText(QCoreApplication.translate("RegistrationScreen", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d...", None))
        self.password_label.setText(QCoreApplication.translate("RegistrationScreen", u"<html><head/><body><p align=\"center\">\u041f\u0430\u0440\u043e\u043b\u044c</p></body></html>", None))
        self.password_regtext.setPlaceholderText(QCoreApplication.translate("RegistrationScreen", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c...", None))
        self.reg_button.setText(QCoreApplication.translate("RegistrationScreen", u"\u0420\u0415\u0413\u0418\u0421\u0422\u0420\u0410\u0426\u0418\u042f", None))
    # retranslateUi

