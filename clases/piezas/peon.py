from clases.piezas.pieza import Pieza

class Peon(Pieza):
	__tipo = "P"

	@property
	def tipo(self):
		return self.__tipo

	def __repr__(self):
		return "P" + self.color

	def __init__(self):
		super().__init__()