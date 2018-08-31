from clases.piezas.pieza import Pieza

class Rook(Pieza):
	__tipo = "R"

	@property
	def tipo(self):
		return self.__tipo
	
	#def __repr__(self):
		#return "T" + self.color

	def __init__(self):
		super().__init__()