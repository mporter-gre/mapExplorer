# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectiondlg.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_connectionDlg(object):
    def setupUi(self, connectionDlg):
        connectionDlg.setObjectName("connectionDlg")
        connectionDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        connectionDlg.resize(398, 274)
        self.connectBtn = QtWidgets.QPushButton(connectionDlg)
        self.connectBtn.setGeometry(QtCore.QRect(90, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.connectBtn.setFont(font)
        self.connectBtn.setObjectName("connectBtn")
        self.cancelBtn = QtWidgets.QPushButton(connectionDlg)
        self.cancelBtn.setGeometry(QtCore.QRect(210, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")
        self.widget = QtWidgets.QWidget(connectionDlg)
        self.widget.setGeometry(QtCore.QRect(70, 60, 251, 110))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.userTxt = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.userTxt.setFont(font)
        self.userTxt.setObjectName("userTxt")
        self.verticalLayout.addWidget(self.userTxt)
        self.passTxt = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passTxt.setFont(font)
        self.passTxt.setObjectName("passTxt")
        self.verticalLayout.addWidget(self.passTxt)
        self.serverTxt = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.serverTxt.setFont(font)
        self.serverTxt.setObjectName("serverTxt")
        self.verticalLayout.addWidget(self.serverTxt)
        self.portTxt = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portTxt.setFont(font)
        self.portTxt.setObjectName("portTxt")
        self.verticalLayout.addWidget(self.portTxt)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)

        self.retranslateUi(connectionDlg)
        QtCore.QMetaObject.connectSlotsByName(connectionDlg)
        connectionDlg.setTabOrder(self.userTxt, self.passTxt)
        connectionDlg.setTabOrder(self.passTxt, self.serverTxt)
        connectionDlg.setTabOrder(self.serverTxt, self.portTxt)
        connectionDlg.setTabOrder(self.portTxt, self.connectBtn)
        connectionDlg.setTabOrder(self.connectBtn, self.cancelBtn)

    def retranslateUi(self, connectionDlg):
        _translate = QtCore.QCoreApplication.translate
        connectionDlg.setWindowTitle(_translate("connectionDlg", "Dialog"))
        self.connectBtn.setText(_translate("connectionDlg", "Connect"))
        self.cancelBtn.setText(_translate("connectionDlg", "Cancel"))
        self.label.setText(_translate("connectionDlg", "Username"))
        self.label_2.setText(_translate("connectionDlg", "Password"))
        self.label_3.setText(_translate("connectionDlg", "Server"))
        self.label_4.setText(_translate("connectionDlg", "Port"))

