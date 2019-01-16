from clases_py.piezas.pieza import Pieza

class Root(Pieza):
	__tipo = "R"

	@property
	def tipo(self):
		return self.__tipo
	
	#def __repr__(self):
		#return "T" + self.color

	def __init__(self):
		super().__init__()