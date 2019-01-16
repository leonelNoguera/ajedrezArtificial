from clases_py.piezas.pieza import Pieza

class King(Pieza):
	__tipo = "K"
	
	@property
	def tipo(self):
		return self.__tipo

	#def __repr__(self):
		#return self.tipo + self.color

	def __init__(self):
		super().__init__()