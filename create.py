import logging

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIntValidator
import create_form
from createInsuranceText import CreateInsuranceText


class Strahouka:
    def __init__(self, firstName, sureName):
      self.firstName = firstName
      self.sureName = sureName


class CreateInsurance(QtWidgets.QMainWindow, create_form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.b_back.clicked.connect(self.but_back)
        self.b_next.clicked.connect(self.createStrahouka)

        regexp = QRegExp(r'^[а-яА-я]*$')
        self.IntValidator = QIntValidator()
        self.validator = QRegExpValidator(regexp)

        self.edit_pass.setValidator(self.IntValidator)

        self.edit_pass.setMaxLength(10)
        self.edit_snils.setValidator(self.IntValidator)
        self.edit_vznos.setValidator(self.IntValidator)
        self.edit_last.setValidator(self.validator)
        self.edit_first.setValidator(self.validator)

        self.edit_third.setValidator(self.validator)

    def but_back(self):
        from choose import Choose_Window
        self.choose = Choose_Window()
        self.choose.show()
        self.close()

    def createStrahouka(self):
        self.boba = CreateInsuranceText(self.edit_first.text(), self.edit_last.text())
        self.boba.start()
        # strahouka = Strahouka(self.edit_first.text(), self.edit_last.text())
        # # strahouka = Strahouka('пися', 'попа')
        # print(strahouka)
        # return strahouka

class ExtendInsurance(QtWidgets.QMainWindow, create_form.Ui_MainWindow):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.b_back.clicked.connect(self.but_back)

        regexp = QRegExp(r'^[а-яА-я]*$')
        self.IntValidator = QIntValidator()
        self.validator = QRegExpValidator(regexp)

        self.edit_pass.setValidator(self.IntValidator)
        self.edit_pass.setMaxLength(10)
        self.edit_snils.setValidator(self.IntValidator)
        self.edit_last.setValidator(self.validator)
        self.edit_first.setValidator(self.validator)
        self.edit_third.setValidator(self.validator)

    def but_back(self):
        self.parent.show()
        self.close()

