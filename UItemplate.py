# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UItemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1065, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(340, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setStyleSheet("background-color:rgb(243, 243, 243)")
        self.connectButton.setObjectName("connectButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ipEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit.setGeometry(QtCore.QRect(90, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit.setFont(font)
        self.ipEdit.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.ipEdit.setObjectName("ipEdit")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(260, 190, 791, 531))
        self.groupBox.setObjectName("groupBox")
        self.CurImage = QtWidgets.QLabel(self.groupBox)
        self.CurImage.setGeometry(QtCore.QRect(20, 30, 751, 481))
        self.CurImage.setText("")
        self.CurImage.setObjectName("CurImage")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(930, 720, 141, 21))
        self.label_11.setObjectName("label_11")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 10, 81, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_ssh = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_ssh.setGeometry(QtCore.QRect(10, 20, 83, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_ssh.setFont(font)
        self.radioButton_ssh.setObjectName("radioButton_ssh")
        self.radioButton_telnet = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_telnet.setGeometry(QtCore.QRect(10, 50, 83, 16))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_telnet.setFont(font)
        self.radioButton_telnet.setIconSize(QtCore.QSize(16, 16))
        self.radioButton_telnet.setObjectName("radioButton_telnet")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 40, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.ipEdit_username = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit_username.setGeometry(QtCore.QRect(90, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit_username.setFont(font)
        self.ipEdit_username.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.ipEdit_username.setObjectName("ipEdit_username")
        self.ipEdit_password = QtWidgets.QTextEdit(self.centralwidget)
        self.ipEdit_password.setGeometry(QtCore.QRect(90, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ipEdit_password.setFont(font)
        self.ipEdit_password.setStyleSheet("background-color:rgb(231, 231, 231)")
        self.ipEdit_password.setObjectName("ipEdit_password")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(790, 0, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 110, 241, 411))
        self.groupBox_4.setObjectName("groupBox_4")
        self.Button_photo = QtWidgets.QPushButton(self.groupBox_4)
        self.Button_photo.setGeometry(QtCore.QRect(70, 30, 81, 31))
        self.Button_photo.setObjectName("Button_photo")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(260, 109, 361, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_commend = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_commend.setGeometry(QtCore.QRect(10, 20, 341, 41))
        self.lineEdit_commend.setObjectName("lineEdit_commend")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(640, 109, 411, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.LogFileter_Edit = QtWidgets.QPlainTextEdit(self.groupBox_5)
        self.LogFileter_Edit.setGeometry(QtCore.QRect(10, 20, 391, 41))
        self.LogFileter_Edit.setObjectName("LogFileter_Edit")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 530, 241, 191))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_Ravg = QtWidgets.QLabel(self.groupBox_6)
        self.label_Ravg.setGeometry(QtCore.QRect(100, 40, 31, 16))
        self.label_Ravg.setText("")
        self.label_Ravg.setObjectName("label_Ravg")
        self.label_Gavg = QtWidgets.QLabel(self.groupBox_6)
        self.label_Gavg.setGeometry(QtCore.QRect(130, 40, 31, 16))
        self.label_Gavg.setText("")
        self.label_Gavg.setObjectName("label_Gavg")
        self.label_Bavg = QtWidgets.QLabel(self.groupBox_6)
        self.label_Bavg.setGeometry(QtCore.QRect(160, 40, 31, 16))
        self.label_Bavg.setText("")
        self.label_Bavg.setObjectName("label_Bavg")
        self.label_Yavg = QtWidgets.QLabel(self.groupBox_6)
        self.label_Yavg.setGeometry(QtCore.QRect(70, 40, 31, 16))
        self.label_Yavg.setText("")
        self.label_Yavg.setObjectName("label_Yavg")
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(190, 40, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_6)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_6)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 41, 16))
        self.label_7.setObjectName("label_7")
        self.label_snrY = QtWidgets.QLabel(self.groupBox_6)
        self.label_snrY.setGeometry(QtCore.QRect(70, 70, 91, 16))
        self.label_snrY.setText("")
        self.label_snrY.setObjectName("label_snrY")
        self.label_snrR = QtWidgets.QLabel(self.groupBox_6)
        self.label_snrR.setGeometry(QtCore.QRect(70, 90, 91, 16))
        self.label_snrR.setText("")
        self.label_snrR.setObjectName("label_snrR")
        self.label_snrG = QtWidgets.QLabel(self.groupBox_6)
        self.label_snrG.setGeometry(QtCore.QRect(70, 110, 91, 16))
        self.label_snrG.setText("")
        self.label_snrG.setObjectName("label_snrG")
        self.label_snrB = QtWidgets.QLabel(self.groupBox_6)
        self.label_snrB.setGeometry(QtCore.QRect(70, 130, 91, 16))
        self.label_snrB.setText("")
        self.label_snrB.setObjectName("label_snrB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1065, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.connectButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "IP "))
        self.groupBox.setTitle(_translate("MainWindow", "Streaming"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0000ff;\">made with QT by IOD</span></p></body></html>"))
        self.radioButton_ssh.setText(_translate("MainWindow", "SSH"))
        self.radioButton_telnet.setText(_translate("MainWindow", "Telnet"))
        self.label_12.setText(_translate("MainWindow", "Username"))
        self.label_13.setText(_translate("MainWindow", "Password"))
        self.label_15.setText(_translate("MainWindow", "Debug HMI"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Function"))
        self.Button_photo.setText(_translate("MainWindow", "Photo"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Commend Window"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Log Filter Window"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Image Info"))
        self.label_2.setText(_translate("MainWindow", "Brightness ("))
        self.label_3.setText(_translate("MainWindow", ")"))
        self.label_4.setText(_translate("MainWindow", "SNR_Y"))
        self.label_5.setText(_translate("MainWindow", "SNR_R"))
        self.label_6.setText(_translate("MainWindow", "SNR_G"))
        self.label_7.setText(_translate("MainWindow", "SNR_B"))
