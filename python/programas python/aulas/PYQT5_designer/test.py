# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import pandas as pd
import openpyxl
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 277)
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_login = QtWidgets.QLabel(self.centralwidget)
        self.label_login.setGeometry(QtCore.QRect(0, 30, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(22)

        self.label_login.setFont(font)
        self.label_login.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_login.setObjectName("label_login")
        self.label_senha = QtWidgets.QLabel(self.centralwidget)
        self.label_senha.setGeometry(QtCore.QRect(0, 80, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(22)

        self.label_senha.setFont(font)
        self.label_senha.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_senha.setObjectName("label_senha")
        self.entry_login = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_login.setGeometry(QtCore.QRect(100, 40, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.entry_login.setFont(font)
        self.entry_login.setObjectName("entry_login")
        self.entry_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_senha.setGeometry(QtCore.QRect(100, 90, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.entry_senha.setFont(font)
        self.entry_senha.setInputMask("")
        self.entry_senha.setText("")
        self.entry_senha.setFrame(True)
        self.entry_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entry_senha.setClearButtonEnabled(False)
        self.entry_senha.setObjectName("entry_senha")

        self.botao_login = QtWidgets.QPushButton(self.centralwidget)
        self.botao_login.setGeometry(QtCore.QRect(20, 150, 141, 61))
        self.botao_login.setFont(font)
        self.botao_login.setObjectName("botao_login")
        self.botao_login.clicked.connect(self.login)                          #comando de login

        self.botao_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.botao_cadastro.setGeometry(QtCore.QRect(200, 150, 141, 61))
        self.botao_cadastro.setFont(font)
        self.botao_cadastro.setObjectName("botao_cadastro")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

       



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_login.setText(_translate("MainWindow", "Login"))
        self.label_senha.setText(_translate("MainWindow", "senha"))
        self.botao_login.setText(_translate("MainWindow", "login"))
        self.botao_cadastro.setText(_translate("MainWindow", "Cadastrar"))
        self.menufile.setTitle(_translate("MainWindow", "file"))

    def login(self,MainWindow):

        self.usuario = self.entry_login.text()
        self.usuario_senha = self.entry_senha.text()
        
        print(f'Seu login é {self.usuario} \nsua senha é {self.usuario_senha}')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
