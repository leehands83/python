import sys
import json
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
import pykorbit



form_class = uic.loadUiType("bitcoin.ui")[0] # loadUiType 매서드는 QT Designer 의 결과물인 bitcoin.ui  파일을 읽어서 파이썬 클래스코드를 만든다.

class MyWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__() # super() 는 파이썬의 내장함수ㄱ
        self.setupUi(self) # form class 에 정의된 매서드로 QT Designer에서 만든 클래스들
        self.timer = QTimer(self)
        self.timer.start(100)
        self.timer.timeout.connect(self.timeout)
        self.pushButton.clicked.connect(self.inquiry)

    def inquiry(self):
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price))
        tesla = web.get_data_yahoo("TSLA",'2021-04-01')

        print("조회버튼 클릭")
        print(str(tesla))


    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)

        price = pykorbit.get_current_price("BTC")
        th_price = str(int(price/1000000))
        hu_price = str(int((price/1000 )% 1000))
        no_price = str(int(price%1000))

        hu_price = hu_price.zfill(3)
        no_price = no_price.zfill(3)

        self.lineEdit.setText(th_price+","+hu_price+","+no_price)

        price = pykorbit.get_current_price("ETH")
        th_price = str(int(price/1000000))
        hu_price = str(int((price/1000 )% 1000))
        no_price = str(int(price%1000))

        hu_price = hu_price.zfill(3)
        no_price = no_price.zfill(3)

        self.lineEdit_ETH.setText(th_price+","+hu_price+","+no_price)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()