import sys
from choose import Choose_Window
from PyQt5.QtWidgets import QApplication, QMainWindow


def appli():
    app = QApplication(sys.argv)
    window = Choose_Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    appli()