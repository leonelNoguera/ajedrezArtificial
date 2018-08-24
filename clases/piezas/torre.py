from clases.piezas.pieza import Pieza

class Torre(Pieza):
	__tipo = "T"

	@property
	def tipo(self):
		return self.__tipo
	
	def __repr__(self):
		return "T" + self.color

	def __init__(self):
		super().__init__()