# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(342, 349)
        LoginScreen.setMinimumSize(QSize(342, 349))
        LoginScreen.setMaximumSize(QSize(342, 349))
        icon = QIcon()
        icon.addFile(u"../../.designer/backup/src_img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        LoginScreen.setWindowIcon(icon)
        LoginScreen.setStyleSheet(u"font: 700 12pt \"Tahoma\";")
        self.centralwidget = QWidget(LoginScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(191, 185, 182);\n"
"font-family: NotoSans-Black;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 306, 256))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 20, 0, 0)
        self.greet_label = QLabel(self.layoutWidget)
        self.greet_label.setObjectName(u"greet_label")
        self.greet_label.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.greet_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.login_label = QLabel(self.layoutWidget)
        self.login_label.setObjectName(u"login_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.login_label)

        self.login_text = QLineEdit(self.layoutWidget)
        self.login_text.setObjectName(u"login_text")
        self.login_text.setAutoFillBackground(False)
        self.login_text.setStyleSheet(u"background-color: white;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.login_text)

        self.password_label = QLabel(self.layoutWidget)
        self.password_label.setObjectName(u"password_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.password_label)

        self.password_text = QLineEdit(self.layoutWidget)
        self.password_text.setObjectName(u"password_text")
        self.password_text.setStyleSheet(u"background-color: white;")
        self.password_text.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_text.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_text)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login_button = QPushButton(self.layoutWidget)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setEnabled(True)
        self.login_button.setStyleSheet(u"font: 14pt \"NotoSans-Black\";\n"
"")
        self.login_button.setCheckable(False)
        self.login_button.setAutoDefault(True)

        self.verticalLayout.addWidget(self.login_button)

        self.reg_button = QPushButton(self.layoutWidget)
        self.reg_button.setObjectName(u"reg_button")
        self.reg_button.setEnabled(True)
        self.reg_button.setStyleSheet(u"font: 14pt \"Microsoft JhengHei UI\";")
        self.reg_button.setCheckable(False)
        self.reg_button.setAutoDefault(True)

        self.verticalLayout.addWidget(self.reg_button)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.incorrect_data_label = QLabel(self.centralwidget)
        self.incorrect_data_label.setObjectName(u"incorrect_data_label")
        self.incorrect_data_label.setEnabled(True)
        self.incorrect_data_label.setGeometry(QRect(30, 310, 291, 16))
        LoginScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432\u043e\u0433\u043e \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430"))
        self.greet_label.setText(QCoreApplication.translate("LoginScreen", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u0414\u041e\u0411\u0420\u041e \u041f\u041e\u0416\u0410\u041b\u041e\u0412\u0410\u0422\u042c!</span></p></body></html>", None))
        self.login_label.setText(QCoreApplication.translate("LoginScreen", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.login_text.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d...", None))
        self.password_label.setText(QCoreApplication.translate("LoginScreen", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.password_text.setPlaceholderText(QCoreApplication.translate("LoginScreen", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c...", None))
        self.login_button.setText(QCoreApplication.translate("LoginScreen", u"\u0412\u041e\u0419\u0422\u0418", None))
        self.reg_button.setText(QCoreApplication.translate("LoginScreen", u"\u0420\u0415\u0413\u0418\u0421\u0422\u0420\u0410\u0426\u0418\u042f", None))
        self.incorrect_data_label.setText(QCoreApplication.translate("LoginScreen", u"\u041d\u0435\u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u044b\u0439 \u043b\u043e\u0433\u0438\u043d \u0438\u043b\u0438 \u043f\u0430\u0440\u043e\u043b\u044c!", None))
    # retranslateUi

