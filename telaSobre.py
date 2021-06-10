from PyQt5 import QtWidgets, uic

class Sobre(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("telas/telaSobre.ui", self)