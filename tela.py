"""
This file is part of Conversor de Temperatura.

Conversor de Temperatura is free software: you can redistribute
it and/or modify it under the terms of the GNU General Public License 
as published by the Free Software Foundation, either version 3 of
the License, or any later version.

Conversor de Temperatura is distributed in the hope that 
it will be useful, but WITHOUT ANY WARRANTY; without even the 
implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Conversor de Temperatura. If not, see <https://www.gnu.org/licenses/>.
"""

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
