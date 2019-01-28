from src_python.square import Square

# Clase Pieza.
class Piece(Square):
	__piece_type = "p"
	
	@property
	def piece_type(self):
		return self.__piece_type
	
	@property
	def color(self):
		return self.__color

	@color.setter
	def color(self, value):
		self.__color = value

	@property
	def id(self):
		return self.__idPieza

	@id.setter
	def id(self, value):
		self.__idPieza = value
	
	def __repr__(self):
		return self.piece_type + self.color

	def __init__(self):
		super().__init__()
		#self.color = None
		#self.id = None