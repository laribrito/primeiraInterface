from PyQt5 import QtWidgets, uic
from telaSobre import Sobre
from telaCf import Cf
from telaFc import Fc

class Principal(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("telas/tela.ui", self)
		self.show()

		self.sobre = Sobre()
		self.btnSobre = self.findChild(QtWidgets.QPushButton, "sobre")
		self.btnSobre.clicked.connect(self.exibirSobre)

		self.cf = Cf()
		self.btnCf = self.findChild(QtWidgets.QPushButton, "cf")
		self.btnCf.clicked.connect(self.exibirCf)

		self.fc = Fc()
		self.btnFc = self.findChild(QtWidgets.QPushButton, "fc")
		self.btnFc.clicked.connect(self.exibirFc)

	def exibirSobre(self):
		self.sobre.show()

	def exibirCf(self):
		self.cf.show()

	def exibirFc(self):
		self.fc.show()
