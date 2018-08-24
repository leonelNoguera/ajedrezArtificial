from clases.casillero import Casillero

# Clase Pieza.
class Pieza(Casillero):
	__tipo = "p"
	
	@property
	def tipo(self):
		return self.__tipo
	
	@property
	def color(self):
		return self.__colorPieza

	@color.setter
	def color(self, value):
		self.__colorPieza = value
	
	def __repr__(self):
		return "  "

	def __init__(self):
		self.color = ""
		self.colorCasillero = ""