import sys

from PyQt5 import QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 221)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 90, 81, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 90, 81, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 90, 81, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(270, 90, 81, 81))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(360, 90, 81, 81))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(450, 90, 81, 81))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 90, 81, 81))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 70, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(380, 70, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 70, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 70, 47, 13))
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 624, 21))
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
        self.pushButton.setText(_translate("MainWindow", "A"))
        self.pushButton_2.setText(_translate("MainWindow", "C"))
        self.pushButton_3.setText(_translate("MainWindow", "B"))
        self.pushButton_4.setText(_translate("MainWindow", "D"))
        self.pushButton_5.setText(_translate("MainWindow", "E"))
        self.pushButton_6.setText(_translate("MainWindow", "F"))
        self.pushButton_7.setText(_translate("MainWindow", "G"))
        self.label.setText(_translate("MainWindow", "До"))
        self.label_2.setText(_translate("MainWindow", "Ре"))
        self.label_3.setText(_translate("MainWindow", "Ми"))
        self.label_4.setText(_translate("MainWindow", "Фа"))
        self.label_5.setText(_translate("MainWindow", "Соль"))
        self.label_6.setText(_translate("MainWindow", "Ля"))
        self.label_7.setText(_translate("MainWindow", "Си"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Фортепиано')
        self.b = True
        self.load_mp3_1('D:/pymusik/noty-do.mp3')
        self.load_mp3_2('D:/pymusik/re.mp3')
        self.load_mp3_3('D:/pymusik/mi.mp3')
        self.load_mp3_4('D:/pymusik/fa.mp3')
        self.load_mp3_5('D:/pymusik/sol.mp3')
        self.load_mp3_6('D:/pymusik/lja.mp3')
        self.load_mp3_7('D:/pymusik/si.mp3')
        self.pushButton.clicked.connect(self.player1.play)
        self.pushButton_2.clicked.connect(self.player2.play)
        self.pushButton_3.clicked.connect(self.player3.play)
        self.pushButton_4.clicked.connect(self.player4.play)
        self.pushButton_5.clicked.connect(self.player5.play)
        self.pushButton_6.clicked.connect(self.player6.play)
        self.pushButton_7.clicked.connect(self.player7.play)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.player1.play()
        elif event.key() == Qt.Key_B:
            self.player2.play()
        elif event.key() == Qt.Key_C:
            self.player3.play()
        elif event.key() == Qt.Key_D:
            self.player4.play()
        elif event.key() == Qt.Key_E:
            self.player5.play()
        elif event.key() == Qt.Key_F:
            self.player6.play()
        elif event.key() == Qt.Key_G:
            self.player7.play()

    def load_mp3_1(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player1 = QtMultimedia.QMediaPlayer()
        self.player1.setMedia(content)

    def load_mp3_2(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player2 = QtMultimedia.QMediaPlayer()
        self.player2.setMedia(content)

    def load_mp3_3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player3 = QtMultimedia.QMediaPlayer()
        self.player3.setMedia(content)

    def load_mp3_4(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player4 = QtMultimedia.QMediaPlayer()
        self.player4.setMedia(content)

    def load_mp3_5(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player5 = QtMultimedia.QMediaPlayer()
        self.player5.setMedia(content)

    def load_mp3_6(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player6 = QtMultimedia.QMediaPlayer()
        self.player6.setMedia(content)

    def load_mp3_7(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player7 = QtMultimedia.QMediaPlayer()
        self.player7.setMedia(content)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())