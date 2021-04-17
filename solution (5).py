import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore,  QtWidgets
from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 551, 281))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 370, 151, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 290, 141, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 310, 551, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 151, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 370, 391, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(10, 410, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(110, 410, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(210, 410, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(310, 410, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Построить"))
        self.label.setText(_translate("MainWindow", "Введите функцию"))
        self.label_2.setText(_translate("MainWindow", "Введите диапозон функции"))
        self.radioButton.setText(_translate("MainWindow", "красный"))
        self.radioButton_2.setText(_translate("MainWindow", "синий"))
        self.radioButton_3.setText(_translate("MainWindow", "зелёный"))
        self.radioButton_4.setText(_translate("MainWindow", "белый"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.setWindowTitle('Построение графиков')

    def run(self):
        d = self.lineEdit_2.text()
        e = d.split(";")
        if e[0] == len(d):
            self.statusbar.showMessage("Неправильный формат ввода диапозона!")
            pass
        if len(d) == 0:
            self.statusbar.showMessage("Введите, пожалуйста, функцию, график которой нужно построить!")
            pass
        try:
            if self.radioButton.isChecked():
                self.statusbar.showMessage("Готово!")
                self.graphicsView.clear()
                self.graphicsView.plot([i for i in range(int(e[0]), int(e[1]) + 1)],
                                       [eval(self.lineEdit.text(), {"x": i}) for i in range(int(e[0]), int(e[1]) + 1)],
                                       pen='r')
            elif self.radioButton_2.isChecked():
                self.statusbar.showMessage("Готово!")
                self.graphicsView.clear()
                self.graphicsView.plot([i for i in range(int(e[0]), int(e[1]) + 1)],
                                       [eval(self.lineEdit.text(), {"x": i}) for i in range(int(e[0]), int(e[1]) + 1)],
                                       pen='b')
            elif self.radioButton_3.isChecked():
                self.statusbar.showMessage("Готово!")
                self.graphicsView.clear()
                self.graphicsView.plot([i for i in range(int(e[0]), int(e[1]) + 1)],
                                       [eval(self.lineEdit.text(), {"x": i}) for i in range(int(e[0]), int(e[1]) + 1)],
                                       pen='g')
            elif self.radioButton_4.isChecked():
                self.statusbar.showMessage("Готово!")
                self.graphicsView.clear()
                self.graphicsView.plot([i for i in range(int(e[0]), int(e[1]) + 1)],
                                       [eval(self.lineEdit.text(), {"x": i}) for i in range(int(e[0]), int(e[1]) + 1)])
            else:
                self.statusbar.showMessage("Выберите, пожалуйста, цвет линии графика!")
                pass
        except ValueError:
            self.statusbar.showMessage("Неправильный формат ввода диапозона!")
            pass
        except IndexError:
            self.statusbar.showMessage("Ошибка при построении данного графика!")
            pass
        except NameError:
            self.statusbar.showMessage("Неправильный формат ввода функции!")
            pass
        except SyntaxError:
            self.statusbar.showMessage("Неправильный формат ввода функции!")
            pass
        except ZeroDivisionError:
            self.statusbar.showMessage("Данная программа не поддерживает построение подобных функций!")
            pass


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
