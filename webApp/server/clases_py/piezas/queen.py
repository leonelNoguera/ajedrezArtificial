from clases_py.piezas.pieza import Pieza

class Queen(Pieza):
	__tipo = "Q"
	
	@property
	def tipo(self):
		return self.__tipo
	
	#def __repr__(self):
		#return "Q" + self.color

	def __init__(self):
		super().__init__()