import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import choose_w
from create import CreateInsurance

class Choose_Window(QtWidgets.QMainWindow, choose_w.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createStr.clicked.connect(self.createStra)
        self.exitApp.clicked.connect(self.bb)

    def createStra(self):
        self.booba = CreateInsurance()
        result = self.booba.createStrahouka()
        #print(result.firstName)
        self.booba.show()
        self.close()

    def bb(self):
        sys.exit()