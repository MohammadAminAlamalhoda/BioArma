# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 300)
        LoginWindow.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(13, 90, 153);\n"
"}\n"
"\n"
"\n"
"QTextBrowser\n"
"{\n"
"background-color: rgb(13, 90, 153);\n"
"color:white;\n"
"border-radius: 5px;\n"
"}")
        self.widget = QtWidgets.QWidget(LoginWindow)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 291))
        self.widget.setStyleSheet("QDoubleSpinBox\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 4px;\n"
"}\n"
"QDoubleSpinBox:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTextBrowser\n"
"{\n"
"background-color: black;\n"
"color:white;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 8px;\n"
"color:black;\n"
"\n"
"}\n"
"QPushButton:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QSpinBox\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 4px;\n"
"color:black;\n"
"\n"
"}\n"
"QSpinBox:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"}\n"
"\n"
"\n"
"QLabel\n"
"{\n"
"color: white;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"background-color: rgb(200, 200, 200);\n"
"border-radius: 4px;\n"
"color:black;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"  background-color:  rgb(166, 166, 166);\n"
"  color: white;\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setGeometry(QtCore.QRect(110, 0, 161, 141))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("AIRLab_logo.jpg"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(160, 130, 191, 21))
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(160, 160, 191, 21))
        self.password.setStyleSheet("")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(59, 130, 81, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 160, 81, 20))
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(160, 200, 113, 32))
        self.login.setObjectName("login")
        self.LoginStatus = QtWidgets.QLabel(self.widget)
        self.LoginStatus.setGeometry(QtCore.QRect(150, 250, 181, 20))
        self.LoginStatus.setText("")
        self.LoginStatus.setObjectName("LoginStatus")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Dialog"))
        self.label.setText(_translate("LoginWindow", "Username"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.login.setText(_translate("LoginWindow", "Login"))
