from clases_py.casillero import Casillero

# Clase Pieza.
class Pieza(Casillero):
	__tipo = "p"
	
	@property
	def tipo(self):
		return self.__tipo
	
	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	@property
	def id(self):
		return self.__idPieza

	@id.setter
	def id(self, value):
		self.__idPieza = value
	
	def __repr__(self):
		return self.tipo + self.color

	def __init__(self):
		super().__init__()
		#self.color = None
		#self.id = None