# Clase Casillero.
# Indica el color del casillero.
class Casillero:
	__tipo = "c"
	
	@property
	def tipo(self):
		return self.__tipo
	@property
	def colorCasillero(self):
		return self.__colorCasillero

	@colorCasillero.setter
	def colorCasillero(self, value):
		self.__colorCasillero = value
	
	def __repr__(self):
		return "  "

	def __init__(self):
		self.__colorCasillero = ""