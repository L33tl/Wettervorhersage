# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change_city_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        self.not_found_error_label = QtWidgets.QLabel(Dialog)
        self.not_found_error_label.setGeometry(QtCore.QRect(30, 160, 154, 16))
        self.not_found_error_label.setStyleSheet("font: 10pt \"Arial\";")
        self.not_found_error_label.setText("")
        self.not_found_error_label.setObjectName("not_found_error_label")
        self.ok_btn = QtWidgets.QPushButton(Dialog)
        self.ok_btn.setGeometry(QtCore.QRect(190, 140, 91, 41))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(Dialog)
        self.cancel_btn.setGeometry(QtCore.QRect(290, 140, 91, 41))
        self.cancel_btn.setObjectName("cancel_btn")
        self.city_edit = QtWidgets.QLineEdit(Dialog)
        self.city_edit.setGeometry(QtCore.QRect(120, 30, 161, 27))
        self.city_edit.setObjectName("city_edit")
        self.city_label = QtWidgets.QLabel(Dialog)
        self.city_label.setGeometry(QtCore.QRect(30, 30, 71, 27))
        self.city_label.setStyleSheet("font: 75 18pt \"Arial\";")
        self.city_label.setLineWidth(1)
        self.city_label.setObjectName("city_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ok_btn.setText(_translate("Dialog", "OK"))
        self.cancel_btn.setText(_translate("Dialog", "Отмена"))
        self.city_label.setText(_translate("Dialog", "Город:"))
