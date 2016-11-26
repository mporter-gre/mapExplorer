import sys
import omeroMatPy
import matlab
from PyQt5.QtWidgets import QApplication, QMainWindow
from Interfaces.mainwindow import Ui_MainWindow
from connDlgModule import connDlg


class keyvalExplorerMain(QMainWindow, Ui_MainWindow):
    def __init__(self, nargout=1):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        # self.aboutToQuit.connect(quitApplication)
        self.omero = omeroMatPy.initialize()  # initialise the matlab engine.
        print(type(self))
        self.addFilterBtn.clicked.connect(self.addFilter)

        conn = connDlg()
        conn.exec_()
        self.user = conn.user
        self.password = conn.password
        self.server = conn.server
        self.port = conn.port
        print(self.user)

        if self.server == "cancel":
            print("I should be closing")
            return

        self.client, self.session = self.omero.globalConnect(self.user, self.password, self.server, self.port,
                                                             nargout=2)

    def addFilter(self):
        print(self.user)
        print(self.client)


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


def quitApplication():
    window.omero.globalDisconnect(nargout=0)
    print(window.client)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == '__main__':  # if we're running file directly and not importing it
    # Create the application and show the window
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(quitApplication)
    window = keyvalExplorerMain()
    window.show()


    try:
        sys.exit(app.exec_())
    except:
        print('Exiting')
