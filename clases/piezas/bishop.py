from clases.piezas.pieza import Pieza

class Bishop(Pieza):
	__tipo = "B"
	
	@property
	def tipo(self):
		return self.__tipo
	
	#def __repr__(self):
		#return super().__repr__() + self.color

	def __init__(self):
		super().__init__()