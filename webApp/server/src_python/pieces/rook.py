from src_python.pieces.piece import Piece

class Rook(Piece):
	__piece_type = "R"

	@property
	def piece_type(self):
		return self.__piece_type
	
	#def __repr__(self):
		#return "T" + self.color

	def __init__(self):
		super().__init__()