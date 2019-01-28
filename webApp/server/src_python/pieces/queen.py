from src_python.pieces.piece import Piece

class Queen(Piece):
	__piece_type = "Q"
	
	@property
	def piece_type(self):
		return self.__piece_type
	
	#def __repr__(self):
		#return "Q" + self.color

	def __init__(self):
		super().__init__()