from clases.piezas.pieza import Pieza

class Alfil(Pieza):
	__tipo = "A"
	
	@property
	def tipo(self):
		return self.__tipo
	
	def __repr__(self):
		return "A" + self.color

	def __init__(self):
		super().__init__()