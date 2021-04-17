import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


# ________________0______1______2__3______4______5_____6__7__8_____9______10_11____12_____13
list_of_params = [0.002, 0.002, 17, 0.000005, 0.1, 'map', 0, 0, True, False, 0, 0, False, '']
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(765, 410)
        MainWindow.setMinimumSize(QtCore.QSize(765, 410))
        MainWindow.setMaximumSize(QtCore.QSize(765, 410))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(771, 16777215))
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setTabletTracking(False)
        self.centralwidget.setAcceptDrops(False)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 561, 291))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 320, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 340, 561, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 150, 21, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(680, 150, 21, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 100, 41, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(660, 190, 41, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(700, 150, 51, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(610, 150, 51, 41))
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(650, 10, 82, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(650, 40, 82, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(650, 66, 82, 21))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(580, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 310, 561, 20))
        self.lineEdit_2.setAcceptDrops(True)
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Большая задача по Maps API. Часть №8"))
        self.pushButton.setText(_translate("MainWindow", "Искать"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.pushButton_4.setText(_translate("MainWindow", "^"))
        self.pushButton_5.setText(_translate("MainWindow", "v"))
        self.pushButton_6.setText(_translate("MainWindow", "->"))
        self.pushButton_7.setText(_translate("MainWindow", "<-"))
        self.radioButton.setText(_translate("MainWindow", "Схема"))
        self.radioButton_2.setText(_translate("MainWindow", "Спутник"))
        self.radioButton_3.setText(_translate("MainWindow", "Гибрид"))
        self.pushButton_8.setText(_translate("MainWindow", "Сброс поискового результата"))



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pushButton_3.clicked.connect(self.run)
        self.pushButton_4.clicked.connect(self.run)
        self.pushButton_5.clicked.connect(self.run)
        self.pushButton_6.clicked.connect(self.run)
        self.pushButton_7.clicked.connect(self.run)
        self.pushButton_8.clicked.connect(self.run)

    def getImage(self, arg):
        global list_of_params
        if arg == 1:
            a = self.lineEdit.text()
            a1 = '+'.join(a.split())
            geocoder_request = f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&format' \
                               f'=json&geocode={a1}'
            response = requests.get(geocoder_request)
            list_of_params[8] = False
            list_of_params[12] = False
            if response:
                json_response = response.json()
                toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
                list_of_params[13] = toponym_address
                self.lineEdit_2.setText(list_of_params[13])
                toponym_coodrinates = toponym["Point"]["pos"]
                addr = toponym_coodrinates.split()
                list_of_params[0] = 0.002

                map_request = f'http://static-maps.yandex.ru/1.x/?ll={addr[0]},{addr[-1]}&spn={list_of_params[0]},' \
                              f'{list_of_params[1]}&l={list_of_params[5]}&pt={addr[0]},{addr[-1]},pmwtm1~{addr[0]},{addr[-1]}'
                list_of_params[6] = addr[0]
                list_of_params[7] = addr[-1]
                list_of_params[10] = addr[0]
                list_of_params[11] = addr[-1]

                response = requests.get(map_request)

                self.map_file = "map.png"
                with open(self.map_file, "wb") as file:
                    file.write(response.content)

                self.pixmap = QPixmap(self.map_file)
                self.label.setPixmap(self.pixmap)
                self.statusbar.showMessage('Запрос выполнен успешно!')

            if not response:
                self.statusbar.showMessage('Ошибка запроса!')

        elif arg == 2:
            if list_of_params[8] is True:
                pass
            else:
                if list_of_params[12] is False:
                    if list_of_params[0] - 0.0025 >= list_of_params[3]:
                        list_of_params[0] -= 0.002
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={list_of_params[6]},{list_of_params[7]}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}' \
                                f'&pt={list_of_params[10]},{list_of_params[11]},pmwtm1~{list_of_params[10]},' \
                                f'{list_of_params[11]}'
                    response = requests.get(map_request)

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)

                else:
                    if list_of_params[0] - 0.0025 >= list_of_params[3]:
                        list_of_params[0] -= 0.002
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={list_of_params[6]},{list_of_params[7]}' \
                                  f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
                    response = requests.get(map_request)

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)

        elif arg == 3:
            if list_of_params[8] is True:
                pass
            else:
                if list_of_params[12] is False:
                    if list_of_params[0] + 0.005 < list_of_params[2]:
                        list_of_params[0] += 0.005
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={list_of_params[6]},{list_of_params[7]}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}' \
                                f'&pt={list_of_params[10]},{list_of_params[11]},pmwtm1~{list_of_params[10]},' \
                                f'{list_of_params[11]}'
                    response = requests.get(map_request)

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)
                else:
                    if list_of_params[0] + 0.005 < list_of_params[2]:
                        list_of_params[0] += 0.005
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={list_of_params[6]},{list_of_params[7]}' \
                                  f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
                    response = requests.get(map_request)

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)
        elif arg == 4:
            if list_of_params[8] is True:
                pass
            else:
                if list_of_params[12] is False:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    mode = str(list_of_params[5])
                    c1 = c1 + 0.001
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}' \
                                f'&pt={list_of_params[10]},{list_of_params[11]},pmwtm1~{list_of_params[10]},' \
                                f'{list_of_params[11]}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)

                else:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    mode = str(list_of_params[5])
                    c1 = c1 + 0.001
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={list_of_params[6]},{list_of_params[7]}' \
                                  f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)

        elif arg == 5:
            if list_of_params[8] is True:
                pass
            else:
                if list_of_params[12] is False:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    c1 = c1 - 0.001
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}' \
                                f'&pt={list_of_params[10]},{list_of_params[11]},pmwtm1~{list_of_params[10]},' \
                                f'{list_of_params[11]}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)
                else:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    c1 = c1 - 0.001
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)

        elif arg == 6:
            if list_of_params[8] is True:
                pass
            else:
                if list_of_params[12] is False:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    c = c + 0.001
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}' \
                                f'&pt={list_of_params[10]},{list_of_params[11]},pmwtm1~{list_of_params[10]},' \
                                f'{list_of_params[11]}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)
                else:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    c = c + 0.001
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                  f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)

        elif arg == 7:
            if list_of_params[8] is True:
                pass
            else:
                if list_of_params[12] is False:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    c = c - 0.001
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}' \
                                f'&pt={list_of_params[10]},{list_of_params[11]},pmwtm1~{list_of_params[10]},' \
                                f'{list_of_params[11]}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)
                else:
                    c = float(list_of_params[6])
                    c1 = float(list_of_params[7])
                    c = c - 0.001
                    mode = str(list_of_params[5])
                    map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                                  f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
                    response = requests.get(map_request)
                    list_of_params[6] = c
                    list_of_params[7] = c1

                    self.map_file = "map.png"
                    with open(self.map_file, "wb") as file:
                        file.write(response.content)

                    self.pixmap = QPixmap(self.map_file)
                    self.label.setPixmap(self.pixmap)
        elif arg == 8:
            list_of_params[12] = True
            self.lineEdit_2.setText('')
            c = float(list_of_params[6])
            c1 = float(list_of_params[7])
            mode = str(list_of_params[5])
            map_request = f'http://static-maps.yandex.ru/1.x/?ll={c},{c1}' \
                          f'&spn={list_of_params[0]},{list_of_params[0]}&l={mode}'
            response = requests.get(map_request)
            self.map_file = "map.png"
            with open(self.map_file, "wb") as file:
                file.write(response.content)

            self.pixmap = QPixmap(self.map_file)
            self.label.setPixmap(self.pixmap)


    def run(self):
        global list_of_params
        try:
            if self.radioButton.isChecked():
                h = 'map'
                list_of_params[5] = h
                if self.sender() == self.pushButton:
                    self.getImage(1)
                elif self.sender() == self.pushButton_2:
                    self.getImage(2)
                elif self.sender() == self.pushButton_3:
                    self.getImage(3)
                elif self.sender() == self.pushButton_4:
                    self.getImage(4)
                elif self.sender() == self.pushButton_5:
                    self.getImage(5)
                elif self.sender() == self.pushButton_6:
                    self.getImage(6)
                elif self.sender() == self.pushButton_7:
                    self.getImage(7)
                elif self.sender() == self.pushButton_8:
                    self.getImage(8)
            elif self.radioButton_2.isChecked():
                l1 = 'sat'
                list_of_params[5] = l1
                if self.sender() == self.pushButton:
                    self.getImage(1)
                elif self.sender() == self.pushButton_2:
                    self.getImage(2)
                elif self.sender() == self.pushButton_3:
                    self.getImage(3)
                elif self.sender() == self.pushButton_4:
                    self.getImage(4)
                elif self.sender() == self.pushButton_5:
                    self.getImage(5)
                elif self.sender() == self.pushButton_6:
                    self.getImage(6)
                elif self.sender() == self.pushButton_7:
                    self.getImage(7)
                elif self.sender() == self.pushButton_8:
                    self.getImage(8)
            elif self.radioButton_3.isChecked():
                l2 = 'sat,skl'
                list_of_params[5] = l2
                if self.sender() == self.pushButton:
                    self.getImage(1)
                elif self.sender() == self.pushButton_2:
                    self.getImage(2)
                elif self.sender() == self.pushButton_3:
                    self.getImage(3)
                elif self.sender() == self.pushButton_4:
                    self.getImage(4)
                elif self.sender() == self.pushButton_5:
                    self.getImage(5)
                elif self.sender() == self.pushButton_6:
                    self.getImage(6)
                elif self.sender() == self.pushButton_7:
                    self.getImage(7)
                elif self.sender() == self.pushButton_8:
                    self.getImage(8)
            else:
                if self.sender() == self.pushButton_8:
                    self.getImage(8)
                else:
                    self.statusbar.showMessage('Выберите тип изображаемого участка мира!')
                    pass
        except Exception:
            self.statusbar.showMessage('Ошибка выполнения запроса!')
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
