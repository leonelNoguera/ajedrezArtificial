from src_python.pieces.piece import Piece

class Pawn(Piece):
	__piece_type = "P"

	@property
	def piece_type(self):
		return self.__piece_type

	@piece_type.setter
	def piece_type(self, value):
		self.__piece_type = value

	@classmethod
	def ultimateMovement(self):
		0
		#return self.__history[len(self.__history) - 1]

	# Chequea que haya sido el último movimiento.
	def ultimateMovementWas(self, r, description):
		# a.p. --> Captura al paso.
		# double_movement --> Movimiento de dos casillas.
		if self.color == 'w':
			fila = "4"
		else:
			fila = "5"
		
		m = str(self.ultimateMovement())
		#if description == "double_movement" and len(m) == 2 and m[1] == fila:
			#try:
				#0
				#for i in range(len(self.history)):
					#print("Line 27.\nhistory[i] = " + self.history[i])
				#previous = self.history[(len(self.history) - 2)]
				#print("Line 27.\nprevious = " + previous)
			#except:
				#0

			#return True

	#def __repr__(self):
		#return "P" + self.color

	def __init__(self):
		super().__init__()