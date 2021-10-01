from PyQt5 import QtWidgets, uic

class Cf(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("telas/telaCf.ui", self)

		self.btnVoltar = self.findChild(QtWidgets.QPushButton, "voltar")
		self.btnVoltar.clicked.connect(self.fecharJanela)

		self.btnCalcular = self.findChild(QtWidgets.QPushButton, "converter")
		self.btnCalcular.clicked.connect(self.calcular)

		self.esse = self.findChild(QtWidgets.QLineEdit, "esse")

		self.saida = self.findChild(QtWidgets.QLabel, "resultado")

	def fecharJanela(self):
		self.close()
		self.esse.setText("")
		self.saida.setText("")

	def calcular(self):
		self.c = self.esse.text()
		self.c = float(self.c)
		self.faren = ((self.c * 9)/5) + 32
		self.faren = round(self.faren, 2)
		self.faren = str(self.faren)
		self.saida.setText(self.faren)
