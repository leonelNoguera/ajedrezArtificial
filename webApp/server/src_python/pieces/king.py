from src_python.pieces.piece import Piece

class King(Piece):
	__piece_type = "K"
	
	@property
	def piece_type(self):
		return self.__piece_type

	#def __repr__(self):
		#return self.tipo + self.color

	def __init__(self):
		super().__init__()