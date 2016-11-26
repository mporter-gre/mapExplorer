# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 614)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.dataTree = QtWidgets.QTreeWidget(self.centralWidget)
        self.dataTree.setGeometry(QtCore.QRect(420, 40, 331, 501))
        self.dataTree.setObjectName("dataTree")
        self.dataTree.headerItem().setText(0, "1")
        self.dataTree.header().setVisible(False)
        self.keyvalCols = QtWidgets.QColumnView(self.centralWidget)
        self.keyvalCols.setGeometry(QtCore.QRect(30, 90, 341, 192))
        self.keyvalCols.setObjectName("keyvalCols")
        self.keyvalFilterCols = QtWidgets.QColumnView(self.centralWidget)
        self.keyvalFilterCols.setGeometry(QtCore.QRect(30, 350, 341, 192))
        self.keyvalFilterCols.setObjectName("keyvalFilterCols")
        self.addFilterBtn = QtWidgets.QPushButton(self.centralWidget)
        self.addFilterBtn.setGeometry(QtCore.QRect(140, 300, 121, 31))
        self.addFilterBtn.setObjectName("addFilterBtn")
        self.userCombo = QtWidgets.QComboBox(self.centralWidget)
        self.userCombo.setGeometry(QtCore.QRect(210, 40, 151, 22))
        self.userCombo.setObjectName("userCombo")
        self.groupCombo = QtWidgets.QComboBox(self.centralWidget)
        self.groupCombo.setGeometry(QtCore.QRect(40, 40, 151, 21))
        self.groupCombo.setObjectName("groupCombo")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 785, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addFilterBtn.setText(_translate("MainWindow", "Add to filter list"))

