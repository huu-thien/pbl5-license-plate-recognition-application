# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PBL5\PBL5_app\PBL5-Car-Lisence-Plate-Recognition-Application-v2\My-App-PBL5\UI\detailsHistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(808, 813)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(9, -1, 801, 721))
        self.frame.setStyleSheet("QFrame {\n"
"    backgroud-color: #eee;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 811, 821))
        self.groupBox_4.setMouseTracking(True)
        self.groupBox_4.setTabletTracking(False)
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
"    background-color: #e7eaed;\n"
"    border: none;\n"
"    border-radius: 10px\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.txtName = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtName.setEnabled(False)
        self.txtName.setGeometry(QtCore.QRect(280, 110, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    padding-left: 12px;\n"
"    color: #371881;\n"
"}")
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(130, 220, 540, 1))
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: #371881;\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setGeometry(QtCore.QRect(130, 160, 540, 1))
        self.label_4.setStyleSheet("QLabel {\n"
"    background-color: #371881;\n"
"}")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.txtLisencePlate = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtLisencePlate.setEnabled(False)
        self.txtLisencePlate.setGeometry(QtCore.QRect(280, 170, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtLisencePlate.setFont(font)
        self.txtLisencePlate.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    padding-left: 12px;\n"
"    color: #371881;\n"
"}")
        self.txtLisencePlate.setText("")
        self.txtLisencePlate.setObjectName("txtLisencePlate")
        self.label_16 = QtWidgets.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(180, 30, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("QLabel {\n"
"    color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
" background-color: #e7eaed;\n"
"}")
        self.label_16.setObjectName("label_16")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(130, 120, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("QLabel {\n"
"    color: #371881;\n"
" background-color: #e7eaed;\n"
"}")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(130, 180, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("QLabel {\n"
"    color: #371881;\n"
" background-color: #e7eaed;\n"
"}")
        self.label_15.setObjectName("label_15")
        self.label_LicensePicture = QtWidgets.QLabel(self.groupBox_4)
        self.label_LicensePicture.setGeometry(QtCore.QRect(120, 350, 571, 381))
        self.label_LicensePicture.setStyleSheet("QLabel {\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0.306818 rgba(143, 0, 146, 255), stop:0.886364 rgba(0, 100, 245, 255));\n"
"   border : none;\n"
"}")
        self.label_LicensePicture.setText("")
        self.label_LicensePicture.setObjectName("label_LicensePicture")
        self.label_17 = QtWidgets.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(130, 300, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("QLabel {\n"
"    color: #371881;\n"
" background-color: #e7eaed;\n"
"}")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_4)
        self.label_18.setGeometry(QtCore.QRect(130, 240, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("QLabel {\n"
"    color: #371881;\n"
" background-color: #e7eaed;\n"
"}")
        self.label_18.setObjectName("label_18")
        self.txtTime = QtWidgets.QLineEdit(self.groupBox_4)
        self.txtTime.setEnabled(False)
        self.txtTime.setGeometry(QtCore.QRect(280, 230, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txtTime.setFont(font)
        self.txtTime.setStyleSheet("QLineEdit{\n"
"    border-radius: 20px;\n"
"    padding-left: 12px;\n"
"    color: #371881;\n"
"}")
        self.txtTime.setText("")
        self.txtTime.setObjectName("txtTime")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(130, 280, 540, 1))
        self.label_5.setStyleSheet("QLabel {\n"
"    background-color: #371881;\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setEnabled(True)
        self.label_27.setGeometry(QtCore.QRect(660, 740, 111, 71))
        self.label_27.setTabletTracking(False)
        self.label_27.setStyleSheet("QLabel {\n"
"    backround-color: red;\n"
"}\n"
"")
        self.label_27.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_27.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap("d:\\PBL5\\PBL5_app\\PBL5-Car-Lisence-Plate-Recognition-Application-v2\\My-App-PBL5\\UI\\../imageUI/icon-deco.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setEnabled(True)
        self.label_28.setGeometry(QtCore.QRect(30, 740, 111, 71))
        self.label_28.setTabletTracking(False)
        self.label_28.setStyleSheet("QLabel {\n"
"    backround-color: red;\n"
"}\n"
"")
        self.label_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_28.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap("d:\\PBL5\\PBL5_app\\PBL5-Car-Lisence-Plate-Recognition-Application-v2\\My-App-PBL5\\UI\\../imageUI/icon-deco.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Details History"))
        self.label_16.setText(_translate("Dialog", "DETAILS HISTORY AND CHECK-IN TIME"))
        self.label_14.setText(_translate("Dialog", "Name :"))
        self.label_15.setText(_translate("Dialog", "License Plate :"))
        self.label_17.setText(_translate("Dialog", "Identification System :"))
        self.label_18.setText(_translate("Dialog", "Time :"))
        self.label_5.setText(_translate("Dialog", "tIME"))
