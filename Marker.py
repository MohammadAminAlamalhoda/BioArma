# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Marker.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Marker(object):
    def setupUi(self, Marker):
        Marker.setObjectName("Marker")
        Marker.resize(181, 298)
        self.valve1 = QtWidgets.QCheckBox(Marker)
        self.valve1.setGeometry(QtCore.QRect(50, 60, 87, 20))
        self.valve1.setChecked(False)
        self.valve1.setObjectName("valve1")
        self.valve2 = QtWidgets.QCheckBox(Marker)
        self.valve2.setGeometry(QtCore.QRect(50, 90, 87, 20))
        self.valve2.setObjectName("valve2")
        self.valve3 = QtWidgets.QCheckBox(Marker)
        self.valve3.setGeometry(QtCore.QRect(50, 120, 87, 20))
        self.valve3.setObjectName("valve3")
        self.valve4 = QtWidgets.QCheckBox(Marker)
        self.valve4.setGeometry(QtCore.QRect(50, 150, 87, 20))
        self.valve4.setObjectName("valve4")
        self.valve5 = QtWidgets.QCheckBox(Marker)
        self.valve5.setGeometry(QtCore.QRect(50, 180, 87, 20))
        self.valve5.setObjectName("valve5")
        self.valve6 = QtWidgets.QCheckBox(Marker)
        self.valve6.setGeometry(QtCore.QRect(50, 210, 87, 20))
        self.valve6.setObjectName("valve6")
        self.BOT = QtWidgets.QCheckBox(Marker)
        self.BOT.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.BOT.setChecked(False)
        self.BOT.setObjectName("BOT")

        self.retranslateUi(Marker)
        QtCore.QMetaObject.connectSlotsByName(Marker)

    def retranslateUi(self, Marker):
        _translate = QtCore.QCoreApplication.translate
        Marker.setWindowTitle(_translate("Marker", "Form"))
        self.valve1.setText(_translate("Marker", "Valve 1"))
        self.valve2.setText(_translate("Marker", "Valve 2"))
        self.valve3.setText(_translate("Marker", "Valve 3"))
        self.valve4.setText(_translate("Marker", "Valve 4"))
        self.valve5.setText(_translate("Marker", "Valve 5"))
        self.valve6.setText(_translate("Marker", "Valve 6"))
        self.BOT.setText(_translate("Marker", "At beginning of task"))
