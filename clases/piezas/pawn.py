from clases.piezas.pieza import Pieza

class Pawn(Pieza):
	__tipo = "P"

	@property
	def tipo(self):
		return self.__tipo

	@tipo.setter
	def tipo(self, value):
		self.__tipo = value

	#def __repr__(self):
		#return "P" + self.color

	def __init__(self):
		super().__init__()