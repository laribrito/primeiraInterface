from PyQt5 import QtWidgets, uic

class Cf(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("telas/telaCf.ui", self)