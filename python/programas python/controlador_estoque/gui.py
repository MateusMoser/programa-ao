# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

unidades = ['litro','kilo','unid','metro']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 900)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Estoque_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.Estoque_combobox.setGeometry(QtCore.QRect(10, 50, 125, 41))
        self.Estoque_combobox.setObjectName("Estoque_combobox")
        self.Estoque_combobox.addItem("")
        self.nome = QtWidgets.QLabel(self.centralwidget)
        self.nome.setGeometry(QtCore.QRect(16, -1, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.nome.setFont(font)
        self.nome.setObjectName("nome")
        
        self.Preco_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.Preco_entrada.setGeometry(QtCore.QRect(10, 140, 125, 30))
        self.Preco_entrada.setInputMask("")
        self.Preco_entrada.setText("")
        self.Preco_entrada.setObjectName("Preco_entrada")

        self.quantidade_entrada = QtWidgets.QLineEdit(self.centralwidget)
        self.quantidade_entrada.setGeometry(QtCore.QRect(10, 180, 125, 30))
        self.quantidade_entrada.setInputMask("")
        self.quantidade_entrada.setText("")
        self.quantidade_entrada.setObjectName("quantidade_entrada")

        self.botao_entrada = QtWidgets.QPushButton(self.centralwidget)
        self.botao_entrada.setGeometry(QtCore.QRect(10, 220, 125, 30))
        self.botao_entrada.setObjectName("botao_entrada")

        self.Preco_saida = QtWidgets.QLineEdit(self.centralwidget)
        self.Preco_saida.setGeometry(QtCore.QRect(160, 140, 125, 30))
        self.Preco_saida.setInputMask("")
        self.Preco_saida.setText("")
        self.Preco_saida.setObjectName("Preco_saida")
        self.botao_saida = QtWidgets.QPushButton(self.centralwidget)
        self.botao_saida.setGeometry(QtCore.QRect(160, 220, 125, 30))
        self.botao_saida.setObjectName("botao_saida")

        self.quantidade_saida = QtWidgets.QLineEdit(self.centralwidget)
        self.quantidade_saida.setGeometry(QtCore.QRect(160, 180, 125, 30))
        self.quantidade_saida.setInputMask("")
        self.quantidade_saida.setText("")
        self.quantidade_saida.setObjectName("quantidade_saida")

        self.produto_saida = QtWidgets.QComboBox(self.centralwidget)
        self.produto_saida.setGeometry(QtCore.QRect(160, 100, 125, 30))
        self.produto_saida.setObjectName("produto_saida")
        self.produto_saida.addItem("")

        self.gastou = QtWidgets.QLabel(self.centralwidget)
        self.gastou.setGeometry(QtCore.QRect(340, 760, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gastou.setFont(font)
        self.gastou.setObjectName("gastou")

        self.gasto = QtWidgets.QLabel(self.centralwidget)
        self.gasto.setGeometry(QtCore.QRect(410, 760, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gasto.setFont(font)
        self.gasto.setObjectName("gasto")

        self.ganhou = QtWidgets.QLabel(self.centralwidget)
        self.ganhou.setGeometry(QtCore.QRect(340, 780, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ganhou.setFont(font)
        self.ganhou.setObjectName("ganhou")

        self.ganhou_2 = QtWidgets.QLabel(self.centralwidget)
        self.ganhou_2.setGeometry(QtCore.QRect(410, 780, 60, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ganhou_2.setFont(font)
        self.ganhou_2.setObjectName("ganhou_2")

        self.atualizar_gasto = QtWidgets.QPushButton(self.centralwidget)
        self.atualizar_gasto.setGeometry(QtCore.QRect(360, 820, 75, 23))
        self.atualizar_gasto.setObjectName("atualizar_gasto")

        self.estoque = QtWidgets.QListWidget(self.centralwidget)
        self.estoque.setGeometry(QtCore.QRect(10, 340, 191, 461))
        self.estoque.setObjectName("estoque")
        item = QtWidgets.QListWidgetItem()
        self.estoque.addItem(item)

        self.legenda_estoque = QtWidgets.QLabel(self.centralwidget)
        self.legenda_estoque.setGeometry(QtCore.QRect(20, 320, 60, 20))
        self.legenda_estoque.setObjectName("legenda_estoque")

        self.legenda_estoque_2 = QtWidgets.QLabel(self.centralwidget)
        self.legenda_estoque_2.setGeometry(QtCore.QRect(140, 320, 60, 20))
        self.legenda_estoque_2.setObjectName("legenda_estoque_2")

        self.produto_saida_2 = QtWidgets.QComboBox(self.centralwidget)
        self.produto_saida_2.setGeometry(QtCore.QRect(10, 100, 125, 30))
        self.produto_saida_2.setObjectName("produto_saida_2")
        self.produto_saida_2.addItem("")
        self.botao_entrada_2 = QtWidgets.QPushButton(self.centralwidget)
        self.botao_entrada_2.setGeometry(QtCore.QRect(300, 220, 125, 30))
        self.botao_entrada_2.setObjectName("botao_entrada_2")

        self.nome_novo = QtWidgets.QLineEdit(self.centralwidget)
        self.nome_novo.setGeometry(QtCore.QRect(300, 140, 125, 30))
        self.nome_novo.setInputMask("")
        self.nome_novo.setText("")
        self.nome_novo.setObjectName("nome_novo")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 180, 125, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.cadastro = QtWidgets.QLabel(self.centralwidget)
        self.cadastro.setGeometry(QtCore.QRect(300, 100, 125, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cadastro.setFont(font)
        self.cadastro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cadastro.setAlignment(QtCore.Qt.AlignCenter)
        self.cadastro.setObjectName("cadastro")

        self.produto_tranforma_1 = QtWidgets.QComboBox(self.centralwidget)
        self.produto_tranforma_1.setGeometry(QtCore.QRect(220, 340, 125, 30))
        self.produto_tranforma_1.setObjectName("produto_tranforma_1")
        self.produto_tranforma_1.addItem("")

        self.label_vira = QtWidgets.QLabel(self.centralwidget)
        self.label_vira.setGeometry(QtCore.QRect(260, 370, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_vira.setFont(font)
        self.label_vira.setObjectName("label_vira")

        self.quantidade_transforma = QtWidgets.QLineEdit(self.centralwidget)
        self.quantidade_transforma.setGeometry(QtCore.QRect(360, 340, 125, 30))
        self.quantidade_transforma.setObjectName("quantidade_transforma")
        
        self.produto_tranforma_2 = QtWidgets.QComboBox(self.centralwidget)
        self.produto_tranforma_2.setGeometry(QtCore.QRect(220, 390, 125, 30))
        self.produto_tranforma_2.setObjectName("produto_tranforma_2")
        self.produto_tranforma_2.addItem("")
        self.quantidade_transforma_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.quantidade_transforma_2.setGeometry(QtCore.QRect(360, 390, 125, 30))
        self.quantidade_transforma_2.setObjectName("quantidade_transforma_2")

        self.atualizar_estoque = QtWidgets.QPushButton(self.centralwidget)
        self.atualizar_estoque.setGeometry(QtCore.QRect(10, 800, 191, 41))
        self.atualizar_estoque.setObjectName("atualizar_estoque")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
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
        self.Estoque_combobox.setItemText(0, _translate("MainWindow", "Estoque"))
        self.nome.setText(_translate("MainWindow", "PEPPER LEMON HAMBURGUERIA E FRANGO"))
        self.Preco_entrada.setPlaceholderText(_translate("MainWindow", "Preço"))
        self.quantidade_entrada.setPlaceholderText(_translate("MainWindow", "Quantidade"))
        self.botao_entrada.setText(_translate("MainWindow", "Entrada"))
        self.Preco_saida.setPlaceholderText(_translate("MainWindow", "Preço"))
        self.botao_saida.setText(_translate("MainWindow", "Saida"))
        self.quantidade_saida.setPlaceholderText(_translate("MainWindow", "Quantidade"))
        self.produto_saida.setItemText(0, _translate("MainWindow", "produto"))
        self.gastou.setText(_translate("MainWindow", "Gastou="))
        self.gasto.setText(_translate("MainWindow", "gasto"))
        self.ganhou.setText(_translate("MainWindow", "ganhou="))
        self.ganhou_2.setText(_translate("MainWindow", "ganhou"))
        self.atualizar_gasto.setText(_translate("MainWindow", "atualizar"))
        __sortingEnabled = self.estoque.isSortingEnabled()
        self.estoque.setSortingEnabled(False)
        item = self.estoque.item(0)
        item.setText(_translate("MainWindow", "item do estoque"))
        self.estoque.setSortingEnabled(__sortingEnabled)
        self.legenda_estoque.setText(_translate("MainWindow", "Item"))
        self.legenda_estoque_2.setText(_translate("MainWindow", "quantidade"))
        self.produto_saida_2.setItemText(0, _translate("MainWindow", "produto"))
        self.botao_entrada_2.setText(_translate("MainWindow", "Entrada"))
        self.nome_novo.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Unidade"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Kilograma"))
        self.comboBox.setItemText(2, _translate("MainWindow", "metro"))
        self.comboBox.setItemText(3, _translate("MainWindow", "litro"))
        self.cadastro.setText(_translate("MainWindow", "cadastro"))
        self.produto_tranforma_1.setItemText(0, _translate("MainWindow", "produto"))
        self.label_vira.setText(_translate("MainWindow", "vira"))
        self.quantidade_transforma.setPlaceholderText(_translate("MainWindow", "quantidade"))
        self.produto_tranforma_2.setItemText(0, _translate("MainWindow", "produto"))
        self.quantidade_transforma_2.setPlaceholderText(_translate("MainWindow", "quantidade"))
        self.atualizar_estoque.setText(_translate("MainWindow", "atualizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
