# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RECOMMENDATION.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from recommendclothes import selectyourclothes, gettemperature, printclothes, saverecommendation
import xml.etree.ElementTree as ET
from datetime import datetime


class Ui_recommendationwindow(object):

    def selection(self):
        try:
            city = self.lineEditCity.text()
            temp = gettemperature(city)
            doc = ET.parse('clotheslist.xml')
            root = doc.getroot()

            select = selectyourclothes(float(temp), root)
            clothes = printclothes(select)
            self.clotheslist.clear()
            for i in clothes:               # list 화면에 보여주기
                self.clotheslist.append(i)

            y = datetime.today().year
            m = datetime.today().month
            d = datetime.today().day
            h = datetime.today().hour
            mi = datetime.today().minute

            self.nowlabel.setText('%d년 %d월 %d일 %d시 %d분 %s 체감 온도 %s°C' %(y, m, d, h, mi, city, temp))

            saverecommendation(select, temp, city, y, m, d, h, mi)

        except:     #흠 예외처리 어케 하지?
            QMessageBox.about(self.inputOK, "Input", "Invalid Value!  ")

    def setupUi(self, recommendationwindow):
        recommendationwindow.setObjectName("recommendationwindow")
        recommendationwindow.resize(450, 310)
        self.inputOK = QtWidgets.QPushButton(recommendationwindow)
        self.inputOK.setGeometry(QtCore.QRect(320, 60, 50, 30))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(10)
        self.inputOK.setFont(font)
        self.inputOK.setObjectName("inputOK")
        self.inputOK.clicked.connect(self.selection)

        self.label = QtWidgets.QLabel(recommendationwindow)
        self.label.setGeometry(QtCore.QRect(80, 35, 220, 20))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(9)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEditCity = QtWidgets.QLineEdit(recommendationwindow)
        self.lineEditCity.setGeometry(QtCore.QRect(80, 60, 220, 30))
        self.lineEditCity.setObjectName("lineEditCity")
        self.lineEditCity.returnPressed.connect(self.selection)

        self.nowlabel = QtWidgets.QLabel(recommendationwindow)
        self.nowlabel.setGeometry(QtCore.QRect(0, 100, 450, 40))
        self.nowlabel.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(9)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.nowlabel.setFont(font)
        self.nowlabel.setText("")
        self.nowlabel.setObjectName("nowlabel")

        self.clotheslist = QtWidgets.QTextBrowser(recommendationwindow)
        self.clotheslist.setGeometry(QtCore.QRect(55, 130, 340, 120))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(10)
        self.clotheslist.setFont(font)
        self.clotheslist.setObjectName("clotheslist")



        self.retranslateUi(recommendationwindow)
        QtCore.QMetaObject.connectSlotsByName(recommendationwindow)

    def retranslateUi(self, recommendationwindow):
        _translate = QtCore.QCoreApplication.translate
        recommendationwindow.setWindowTitle(_translate("recommendationwindow", "Recommend"))
        self.inputOK.setText(_translate("recommendationwindow", "OK"))
        self.label.setText(_translate("recommendationwindow", "City Name"))
        self.clotheslist.setHtml(_translate("recommendationwindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'D2Coding\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    recommendationwindow = QtWidgets.QDialog()
    ui = Ui_recommendationwindow()
    ui.setupUi(recommendationwindow)
    recommendationwindow.show()
    sys.exit(app.exec_())
