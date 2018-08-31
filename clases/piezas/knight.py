from clases.piezas.pieza import Pieza

class Knight(Pieza):
	__tipo = "N"
	
	@property
	def tipo(self):
		return self.__tipo
	
	#def __repr__(self):
		#return "C" + self.color

	def __init__(self):
		super().__init__()