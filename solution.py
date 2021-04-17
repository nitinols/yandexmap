import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 410)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel('', self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 700, 311))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton('Искать', self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(560, 340, 131, 21))
        self.pushButton.setObjectName("pushbutton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 340, 541, 20))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Большая задача по Maps API. Часть №5"))
        self.label.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Искать"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def getImage(self):
        a = self.lineEdit.text()
        a1 = '+'.join(a.split())
        geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&format' \
                           f'=json&geocode={a1}'
        response = requests.get(geocoder_request)

        if response:
            json_response = response.json()
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            toponym_coodrinates = toponym["Point"]["pos"]
            addr = toponym_coodrinates.split()

            map_request = f'https://static-maps.yandex.ru/1.x/?ll={addr[0]},{addr[-1]}&spn=0.002,0.002&l=map&pt={addr[0]},{addr[-1]},pmwtm1~{addr[0]},{addr[-1]}'
            response = requests.get(map_request)

            self.map_file = "map.png"
            with open(self.map_file, "wb") as file:
                file.write(response.content)

            self.pixmap = QPixmap(self.map_file)
            self.label.setPixmap(self.pixmap)
            self.statusbar.showMessage('Запрос выполнен успешно!')

        if not response:
            self.statusbar.showMessage('Ошибка запроса!')

    def run(self):
        self.getImage()

    def closeEvent(self, event):
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())