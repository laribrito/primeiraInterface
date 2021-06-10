from PyQt5 import QtWidgets, uic

class Fc(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("telas/telaFc.ui", self)