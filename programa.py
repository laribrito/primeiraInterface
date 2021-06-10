from PyQt5 import QtWidgets
import sys
from tela import Principal

app = QtWidgets.QApplication(sys.argv)
janela = Principal()
app.exec_()