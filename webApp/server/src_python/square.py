# Clase Square.
# Indica el color del casillero.
class Square:
	__piece_type = "c"

	@property
	def piece_type(self):
		return self.__piece_type
	@property
	def square_color(self):
		return self.__square_color

	@square_color.setter
	def square_color(self, value):
		self.__square_color = value
	
	def __repr__(self):
		return "  "

	def __init__(self):
		self.__square_color = ""