from src_python.pieces.piece import Piece

class Knight(Piece):
	__piece_type = "N"
	
	@property
	def piece_type(self):
		return self.__piece_type
	
	#def __repr__(self):
		#return "C" + self.color

	def __init__(self):
		super().__init__()