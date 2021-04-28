# refer site : https://wikidocs.net/35485
# interperiter :

#Qdate 는 Core에 종속
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime, QDate
from PyQt5 import uic

form_class = uic.loadUiType("basic_Clock.ui")[0]

#dataTimeVar = QData.fromString("2019-05-17","yyyy-MM-dd")

class WindowClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()

        #dateVar = QDate(year, month, day)
        #timeVar = QTime(hour, minute, second)

        self.setupUi(self)
        self.pB_connect.clicked.connect(self.changedfunction)

    def changedfunction(self) :
        dataVar = QDate.currentDate()
        #self.label_date.setText("{0}",dataVar)
        self.label_voltage.setText("Try connect to device...")



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
