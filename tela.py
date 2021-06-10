from PyQt5 import QtWidgets, uic

class Principal(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__
		uic.loadUi("telas/tela.ui", self)
		self.show()