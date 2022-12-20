import sys
from fpdf import FPDF
from PyQt5 import QtWidgets
import create_form
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QIntValidator
import choose_w

# bebra = Choose_Window()



class CreateInsuranceText():
    def __init__(self, name, sureName):
        self.name = name
        self.sureName = sureName

    def start(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
        pdf.set_font('DejaVu', '', 18)
        pdf.cell(200, 10, txt="ДОГОВОР", ln=1, align="C")
        pdf.set_font('DejaVu', '', 10)
        pdf.cell(200, 10, txt="", ln=1, align="С")
        pdf.cell(200, 10, txt="страхование", ln=1, align="C")
        pdf.cell(200, 10, txt=" ", ln=1, align="l")
        pdf.cell(200, 10, txt="г. <<<   >>>                                                                                                     «___»  ______________ 20__ г. ", ln=1, align="l")
        pdf.cell(200, 10, txt=" ", ln=1, align="l")
        pdf.set_font('DejaVu', '', 18)
        pdf.cell(200, 10, txt=" ", ln=1, align="l")
        pdf.cell(200, 10, txt="ПРЕДМЕТ ДОГОВОРА", ln=1, align="C")
        pdf.cell(200, 10, txt=" ", ln=1, align="l")
        pdf.set_font('DejaVu', '', 10)
        pdf.multi_cell(200, 10, txt="По настоящему Договору Страховщик обязуется при наступлении страхового случая выплатить Застрахованному лицу (Выгодоприобретателю) страховое возмещение, а Страхователь обязуется уплатить Страховщику страховую премию в размере, в порядке и в сроки, предусмотренные Договором.", align="l")
        pdf.cell(200, 10, txt=" ", ln=1, align="l")
        pdf.cell(200, 10, txt=f"Застрахованным лицом является: {self.name } {self.sureName}  ", ln=1, align="l")
        pdf.cell(200, 10, txt="Выгодоприобретателем является:   ", ln=1, align="l")
        pdf.cell(200, 10, txt=" ", ln=1, align="l")
        pdf.cell(200, 10, txt=" ", ln=1, align="c")
        pdf.set_font('DejaVu', '', 18)
        pdf.cell(200, 10, txt="СТРАХОВОЙ СЛУЧАЙ. ПРАВА И ОБЯЗАННОСТИ СТОРОН", ln=1, align="C")
        pdf.set_font('DejaVu', '', 10)
        pdf.cell(200, 10, txt="Страховщик обязан: ", ln=1, align="l")
        pdf.multi_cell(200, 10, txt="       При наступлении страхового случая выплатить страховую сумму в размере, порядке и сроки, установленные настоящим Договором.", align="c")

        pdf.cell(200, 10, txt="Страхователь обязан: ", ln=1, align="l")
        pdf.multi_cell(200, 10, txt="       Сообщить Страховщику обстоятельства, имеющие существенное значение для определения вероятности наступления страхового случая, если эти обстоятельства неизвестны и не должны быть известны Страховщику.", align="L")
        pdf.multi_cell(200, 10, txt="Предоставить Страховщику возможность беспрепятственной проверки информации, связанной с настоящим Договором, и представлять все необходимые документы и иные доказательства.", align="L")

        pdf.set_font('DejaVu', '', 18)
        pdf.cell(200, 10, txt="СТРАХОВАЯ ПРЕМИЯ", ln=1, align="C")
        pdf.set_font('DejaVu', '', 10)
        pdf.multi_cell(200, 10, txt="Страховая премия по настоящему Договору составляет "  " рублей, уплачивается Страхователем в срок до «  »  20@@@ г. путем перечисления денежных средств на расчетный счет Страховщика.", align="L")

        pdf.set_font('DejaVu', '', 18)
        pdf.cell(200, 10, txt=" ", ln=1, align="c")
        pdf.cell(200, 10, txt="ВЫПЛАТА СТРАХОВОЙ СУММЫ", ln=1, align="C")
        pdf.set_font('DejaVu', '', 10)
        pdf.multi_cell(200, 10, txt=f"       Страховая сумма устанавливается в размере   рублей.", align="L") #123
        pdf.multi_cell(200, 10, txt="       При наступлении страхового случая Страховщик обязан произвести выплату страховой суммы Застрахованному лицу (Выгодоприобретателю) в течение 1 года после получения и составления всех необходимых документов, указанных в настоящем Договоре.", align="L")
        pdf.multi_cell(200, 10, txt="       Для получения страхового возмещения Страхователь (Выгодоприобретатель) представляет Страховщику следующие документы:", align="L")
        pdf.cell(200, 10, txt="* заявление;", ln=1, align="L")
        pdf.cell(200, 10, txt="* настоящий Договор;", ln=1, align="L")
        pdf.cell(200, 10, txt="* документы, подтверждающие факт наступления страхового случая.", ln=1, align="L")

        pdf.set_y(-40)
        pdf.cell(0, 10, 'Подпись:___________________', 0, 0, 'R') # +фамилия после подписи

        print('+')
        pdf.output("simple_demo.pdf")


# ABOOBA = CreateInsuranceText()
# ABOOBA.start()