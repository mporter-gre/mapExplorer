from PyQt5.QtWidgets import QDialog
from Interfaces.connectionDlg import Ui_connectionDlg


class connDlg(QDialog, Ui_connectionDlg):
    def __init__(self,):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        print("Connection Dialogue!")
        self.connectBtn.clicked.connect(self.connect)
        self.cancelBtn.clicked.connect(self.cancel)
        self.retVal = "qwerqwerqwer"

    def connect(self):
        self.user = self.userTxt.text()
        self.password = self.passTxt.text()
        self.server = self.serverTxt.text()
        self.port = float(self.portTxt.text())
        self.accept()
        # return user, password, server, port

    def cancel(self):
        self.user = "cancel"
        self.password = "cancel"
        self.server = "cancel"
        self.port = "cancel"
        self.accept()
        # return "cancel", "cancel", "cancel", "cancel"