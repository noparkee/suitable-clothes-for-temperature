# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MAIN.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from evaluation import Ui_evaluationwindow
from recommendation import Ui_recommendationwindow
from PyQt5.QtWidgets import QMessageBox
from makebasisfile import makebasis

class Ui_mainwindow(object):

    def openEvaluation(self):
        f = open('myrecommendation.txt', 'rt')
        fir = f.readline()  # 이전 추천 내역이 있는지 없는지 확인
        if fir == '0':
            QMessageBox.about(self.evaButton, "!", "NO DATA  ")
            f.close()

        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_evaluationwindow()
            self.ui.setupUi(self.window)
            self.window.show()

    def openRecommendation(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_recommendationwindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(450, 310)
        self.recoButton = QtWidgets.QPushButton(mainwindow)
        self.recoButton.setGeometry(QtCore.QRect(85, 50, 280, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.recoButton.setFont(font)
        self.recoButton.setCheckable(False)
        self.recoButton.setObjectName("recoButton")

        self.recoButton.clicked.connect(self.openRecommendation)


        self.evaButton = QtWidgets.QPushButton(mainwindow)
        self.evaButton.setGeometry(QtCore.QRect(85, 180, 280, 80))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        self.evaButton.setFont(font)
        self.evaButton.setObjectName("evaButton")

        self.evaButton.clicked.connect(self.openEvaluation)

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
        mainwindow.setTabOrder(self.recoButton, self.evaButton)

    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle('Suitable clothes for temperature')
        self.recoButton.setText(_translate("mainwindow", "RECOMMENDATION"))
        self.evaButton.setText(_translate("mainwindow", "EVALUATION"))


if __name__ == "__main__":
    import sys
    makebasis()
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QDialog()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
