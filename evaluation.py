# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EVALUATION.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from evaluateclothes import toohot, toocold, findnumber
from PyQt5.QtWidgets import QMessageBox

class Ui_evaluationwindow(object):

    def printpreviouscondition(self):
        f = open('myrecommendation.txt', 'rt')
        fir = f.readline()  # 이전 추천 내역이 있는지 없는지 확인
        '''if fir == '0':
            QMessageBox.about(self.OKButton, "!", "NO DATA  ")
            self.nowlabel_2.setText('NO DATA')
            f.close()
            return 0
        else:'''
        condition = f.readline()            # 이게 조건
        self.nowlabel_2.setText(condition)
        rec = f.readlines()
        for i in rec:
            self.comboBox.addItem(i[:-1])
        f.close()
        return 1

    def evaluation(self):
        f = open('myrecommendation.txt', 'rt')
        f.readline()
        condition = f.readline()
        word = condition.split(' ')
        cel = float(word[-1][:-3])

        clo = self.comboBox.currentText()
        num = findnumber(clo)

        if self.hotButton.isChecked():
            toohot(cel, num)
        elif self.coldButton_2.isChecked():
            toocold(cel, num)


        QMessageBox.about(self.OKButton, "Thank you", "Thank you for your evaluation  ")


    def setupUi(self, evaluationwindow):
        evaluationwindow.setObjectName("evaluationwindow")
        evaluationwindow.resize(450, 310)
        self.recentlabel = QtWidgets.QLabel(evaluationwindow)
        self.recentlabel.setGeometry(QtCore.QRect(60, 40, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.recentlabel.setFont(font)
        self.recentlabel.setObjectName("recentlabel")
        self.comboBox = QtWidgets.QComboBox(evaluationwindow)
        self.comboBox.setGeometry(QtCore.QRect(60, 90, 331, 31))
        self.comboBox.setObjectName("comboBox")
        self.groupBox = QtWidgets.QGroupBox(evaluationwindow)
        self.groupBox.setGeometry(QtCore.QRect(60, 150, 330, 100))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.OKButton = QtWidgets.QPushButton(self.groupBox)
        self.OKButton.setGeometry(QtCore.QRect(270, 60, 50, 30))
        self.OKButton.setObjectName("OKButton")
        self.OKButton.clicked.connect(self.evaluation)

        self.hotButton = QtWidgets.QRadioButton(self.groupBox)
        self.hotButton.setGeometry(QtCore.QRect(70, 45, 71, 19))
        self.hotButton.setObjectName("hotButton")

        self.coldButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.coldButton_2.setGeometry(QtCore.QRect(150, 45, 81, 19))
        self.coldButton_2.setObjectName("coldButton_2")

        self.nowlabel_2 = QtWidgets.QLabel(evaluationwindow)
        self.nowlabel_2.setGeometry(QtCore.QRect(55, 70, 330, 31))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(9)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.nowlabel_2.setFont(font)
        self.nowlabel_2.setObjectName("nowlabel_2")
        self.printpreviouscondition()

        self.retranslateUi(evaluationwindow)
        QtCore.QMetaObject.connectSlotsByName(evaluationwindow)

    def retranslateUi(self, evaluationwindow):
        _translate = QtCore.QCoreApplication.translate
        evaluationwindow.setWindowTitle(_translate("evaluationwindow", "Evaluate"))
        self.recentlabel.setText(_translate("evaluationwindow", "Previous"))
        self.groupBox.setTitle(_translate("evaluationwindow", "Evaluation"))
        self.OKButton.setText(_translate("evaluationwindow", "OK"))
        self.hotButton.setText(_translate("evaluationwindow", "HOT"))
        self.coldButton_2.setText(_translate("evaluationwindow", "COLD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evaluationwindow = QtWidgets.QDialog()
    ui = Ui_evaluationwindow()
    ui.setupUi(evaluationwindow)
    evaluationwindow.show()
    sys.exit(app.exec_())
