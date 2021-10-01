from PyQt5 import QtWidgets, uic

class Fc(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("telas/telaFc.ui", self)

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
		self.f = self.esse.text()
		self.f = float(self.f)
		self.cels = 5 * ((self.f-32) / 9)
		self.cels = round(self.cels, 2)
		self.cels = str(self.cels)
		self.saida.setText(self.cels)