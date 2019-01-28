from src_python.pieces.piece import Piece

class Bishop(Piece):
	__piece_type = "B"
	
	@property
	def piece_type(self):
		return self.__piece_type
	
	#def __repr__(self):
		#return super().__repr__() + self.color

	def __init__(self):
		super().__init__()