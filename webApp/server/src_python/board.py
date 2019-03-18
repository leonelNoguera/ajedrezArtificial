import random, os
from src_python.reglamento import Reglamento
from src_python.pieces.pawn import Pawn
from src_python.pieces.king import King
from src_python.pieces.queen import Queen
from src_python.pieces.bishop import Bishop
from src_python.pieces.knight import Knight
from src_python.pieces.rook import Rook
from src_python.square import Square

class Board:
	matrizBoard = []
	__matrizPiezas = []
	reglamento = Reglamento()
	board_str = ''

	columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
	rows = [8, 7, 6, 5, 4, 3, 2, 1]

	#@property
	#def reglamento(self):
		#return self.__reglamento
	
	@classmethod
	def moverOD(self, od):
		print("Recibido en moverOD: " + od)

		if ((od[0]) + (od[1]) != (od[3]) + (od[4])): # Si origen == destino no hace cambios. El castling envía "00 00".
			self.matrizBoard[
				int(od[3])
				][
					int(od[4])
					] = self.matrizBoard[int(od[0])][int(od[1])]
			self.matrizBoard[int(od[0])][int(od[1])] = Square()
		
		self.pintarSquares()
	
	@classmethod
	def partida(self, movimientos):
		for i in range(len(movimientos)):
			self.mover(movimientos[i])
			print(self.__repr__() + "\n")
			#os.system("sleep 1")

	@classmethod
	def back_movement(self, board_str):
		self.reglamento.cambiarTurno(self.reglamento.turno)
		k = 0
		for i in range(8):
			for j in range(8):
				self.matrizBoard[i][j] = Square()
				if board_str[k] == 'R':
					self.matrizBoard[i][j] = Rook()
					self.matrizBoard[i][j].color = board_str[k + 1]
				if board_str[k] == 'N':
					self.matrizBoard[i][j] = Knight()
					self.matrizBoard[i][j].color = board_str[k + 1]
				if board_str[k] == 'B':
					self.matrizBoard[i][j] = Bishop()
					self.matrizBoard[i][j].color = board_str[k + 1]
				if board_str[k] == 'K':
					self.matrizBoard[i][j] = King()
					self.matrizBoard[i][j].color = board_str[k + 1]
				if board_str[k] == 'Q':
					self.matrizBoard[i][j] = Queen()
					self.matrizBoard[i][j].color = board_str[k + 1]
				if board_str[k] == 'P':
					self.matrizBoard[i][j] = Pawn()
					self.matrizBoard[i][j].color = board_str[k + 1]
				k += 2

	@classmethod
	def mover(self, movimiento, simulate_movement = False):
		print('Line 43: El turno actual es: ' + self.reglamento.turno)

		board_str = ''
		for i in range(8):
			for j in range(8):
				board_str += str(self.matrizBoard[i][j])

		print('Line 50 (board.py): En mover(). board_str == ' + board_str)
		#__retornoReglamento = self.__reglamento.mover(__movimiento, __jugador, self.matrizBoard, self.__reglamento.turno)
		retornoReglamento = self.reglamento.mover(
			movimiento, self.reglamento.turno, self.matrizBoard
			)
		print("El reglamento retornó: " + str(retornoReglamento))
		if type(retornoReglamento) == type(str()):
			self.moverOD(retornoReglamento)
			
			print('Line 60 (board.py): En mover(). self.reglamento.turno == ' + self.reglamento.turno)
			player = 'w'
			if self.reglamento.turno == 'w':
				player = 'b'

			if simulate_movement:
				if self.reglamento.is_in_check(player, self.matrizBoard):
					self.back_movement(board_str)
					return False
				else:
					self.back_movement(board_str)
					return True
			else:
				if self.reglamento.is_in_check(player, self.matrizBoard):
					print('Line 65 (board.py): En mover(). Movimiento ilegal porque deja al rey en check')
					self.back_movement(board_str)
					
				else:
					return True

		#input("Line 53 (board.py): En mover(). movimiento == " + movimiento)
		return False
		
	@classmethod
	def inicializarPiezas(self):
		self.__matrizPiezas.append([Rook(), Knight(), Bishop(), Queen(), 
			King(), Bishop(), Knight(), Rook()])
		self.__matrizPiezas.append([Pawn(), Pawn(), Pawn(), Pawn(), Pawn(),
			Pawn(), Pawn(), Pawn()
			])
		self.__matrizPiezas.append([Pawn(), Pawn(), Pawn(), Pawn(), Pawn(),
			Pawn(), Pawn(), Pawn()
			])
		self.__matrizPiezas.append([Rook(), Knight(), Bishop(), Queen(),
			King(), Bishop(), Knight(), Rook()
			])
		id = 0
		for i in range(2):
			for j in range(8):
				self.__matrizPiezas[i][j].id = id
				id += 1
				self.__matrizPiezas[i][j].color = "b"
				self.__matrizPiezas[i+2][j].color = "w"
		#for i in range(2):
			#for j in range(8):
				#input("Line 62.\nid =" + str(self.__matrizPiezas[i][j].id))
				
	@classmethod
	def pintarSquares(self):
		__b = Square()
		__b.colorSquare = "w"
		__n = Square()
		__n.colorSquare = "b"
		
		for i in range(8):
			for j in range(8):
				if i % 2:
					if j % 2:
						self.matrizBoard[i][j].colorSquare = "w"
					else:
						self.matrizBoard[i][j].colorSquare = "b"
				else:
					if j % 2:
						self.matrizBoard[i][j].colorSquare = "b"
					else:
						self.matrizBoard[i][j].colorSquare = "w"
	
	@classmethod
	def tableroToFile(self):
		f = open("tablero.txt", 'w');
		f.write(str(self.matrizBoard));
		f.close()
	
	@classmethod
	def movimientosToFile(self, m, j):
		f = open("movimientos.txt", 'a')
		f.write(("tablero.mover(\'" + m + "\', \'" + j + "\')" + "\n"))
		f.close()

	@classmethod
	def colocarPiezas(self):
		__b = Square()
		__b.colorSquare = "w"
		__n = Square()
		__n.colorSquare = "b"
		
		for i in range(8):
			self.matrizBoard.append([
				Square(), Square(), Square(), Square(), 
				Square(), Square(), Square(), Square(),
				])
				
		for i in range(8):
			#Coordenadas en notación: [a-h][8-1]
			# Blancas: 7 y 8
			# Negras: 1 y 2
			# El rey en el Square de su color.
			self.matrizBoard[0][i] = self.__matrizPiezas[0][i]
			self.matrizBoard[1][i] = self.__matrizPiezas[1][i]
			self.matrizBoard[6][i] = self.__matrizPiezas[2][i]
			self.matrizBoard[7][i] = self.__matrizPiezas[3][i]

		self.pintarSquares();
		#self.tableroToFile();
	
	@classmethod
	def available_movements(self):
		self.reglamento.turno = 'b'
		available_movements = []
		piece_to_use = ''
		capture = ''
		destino_column = ''
		destino_row = ''
		promotion = ''
		capture_or_not = ['', 'x']
		origin_column = ''
		# R, N, B, K, Q, P
		disponible_pieces = [['','','','','',''], ['','','','','','']]
		#bishop_origin_columns_disponible = [[['h', 2]['g', 3]['f', 4]['f', 5]['h', 7]], [['h', 3], ['g', 4], ['g', 5], ['h', 6]], [['h', 4], ['h', 5]], [], [], [['a', 4], ['a', 5]], [['a', 3], ['b', 4], ['a', 6], ['b', 5]], [['a', 2], ['b', 3], ['c', 4], ['c', 5], ['a', 7]]]
		
		for i in range(8):
			for j in range(8):
				if self.matrizBoard[i][j].piece_type != 'c' and self.matrizBoard[i][j].color == 'b':
					if self.matrizBoard[i][j].piece_type == 'R':
						disponible_pieces[0][0] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'N':
						disponible_pieces[0][1] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'B':
						disponible_pieces[0][2] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'K':
						disponible_pieces[0][3] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'Q':
						disponible_pieces[0][4] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'P':
						disponible_pieces[0][5] = self.matrizBoard[i][j].piece_type
					
				if self.matrizBoard[i][j].piece_type != 'c' and self.matrizBoard[i][j].color == 'w':
					if self.matrizBoard[i][j].piece_type == 'R':
						disponible_pieces[1][0] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'N':
						disponible_pieces[1][1] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'B':
						disponible_pieces[1][2] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'K':
						disponible_pieces[1][3] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'Q':
						disponible_pieces[1][4] = self.matrizBoard[i][j].piece_type
					if self.matrizBoard[i][j].piece_type == 'P':
						disponible_pieces[1][5] = self.matrizBoard[i][j].piece_type
					

		#print("Line 199 (board.py): En available_movements(). disponible_pieces == " + str(disponible_pieces))

		color_index = 0
		if self.reglamento.turno == 'w':
			color_index = 1
		
		for i in range(len(disponible_pieces[color_index])):
			piece_to_use = disponible_pieces[color_index][i]
			#print("Line 243 (board.py): En available_movements(). piece_to_use == " + piece_to_use)
			if piece_to_use == 'P':
				piece_to_use = ''
			if piece_to_use == 'tmp_R':
				available_movements.append('0-0')
				available_movements.append('0-0-0')

			for m in range(len(capture_or_not)):
				capture = capture_or_not[m]
				for j in range(len(self.columns)):
					destino_column = self.columns[j]
					for k in range(len(self.rows)):
						destino_row = self.rows[k]

						if piece_to_use == 'tmp_': # 212 movements
							if (self.reglamento.turno == 'w' and destino_row == 8) or (self.reglamento.turno == 'b' and destino_row == 1):
								promotion = ''
								promotion += '='
								available_to_promotion = ['R', 'N', 'B', 'Q']

								for l in range(len(available_to_promotion)):
									promotion += available_to_promotion[l]
									if capture == 'x':
										for n in range(len(self.columns)):
											if (n == (self.columns.index(destino_column) - 1)) or (n == (self.columns.index(destino_column) + 1)):
												available_movements.append(str(piece_to_use) + str(self.columns[n]) + str(capture) + str(destino_column) + str(destino_row) + str(promotion))
									else:
										available_movements.append(str(piece_to_use) + str(origin_column) + str(capture) + str(destino_column) + str(destino_row) + str(promotion))
									promotion = '='
							else:
								if (self.reglamento.turno == 'w' and destino_row >= 3) or (self.reglamento.turno == 'b' and destino_row <= 6):
									if capture == 'x':
										for n in range(len(self.columns)):
											if (n == (self.columns.index(destino_column) - 1)) or (n == (self.columns.index(destino_column) + 1)):
												available_movements.append(str(piece_to_use) + str(self.columns[n]) + str(capture) + str(destino_column) + str(destino_row))
												if (self.reglamento.turno == 'w' and destino_row == 5) or (self.reglamento.turno == 'b' and destino_row == 4):
													available_movements.append(str(piece_to_use) + str(self.columns[n]) + str(capture) + str(destino_column) + str(destino_row) + "e.p.")
									else:
										available_movements.append(str(piece_to_use) + str(origin_column) + str(capture) + str(destino_column) + str(destino_row))
						
						if piece_to_use == 'tmp_B' or piece_to_use == 'tmp_Q':
							available_movements.append(str(piece_to_use) + str(origin_column) + str(capture) + str(destino_column) + str(destino_row))
							for l in range(len(self.columns)):
								bishop_origin_row_posible = False
								if l != destino_row - 1:
										if destino_row == 2 and (l < 3):
											bishop_origin_row_posible = True
										else:
											if destino_row == 3 and (l < 5):
												bishop_origin_row_posible = True
											else:
												if destino_row == 4 and (l < 7):
													bishop_origin_row_posible = True
												else:
													if destino_row == 5 and (l > 0):
														bishop_origin_row_posible = True
													else:
														if destino_row == 6 and (l > 2):
															bishop_origin_row_posible = True
														else:
															if destino_row == 7 and (l > 4):
																bishop_origin_row_posible = True

								if bishop_origin_row_posible:
									available_movements.append(str(piece_to_use) + str(l + 1) + str(capture) + str(destino_column) + str(destino_row))
								
								if (self.columns[l] != destino_column):
									if (destino_column != 'a' or destino_column != 'h') and (destino_row != 1 and destino_row != 8):

										bishop_origin_column_posible = False
										if destino_column == 'a':
											if l < 7:
												if destino_row == 2 or destino_row == 7:
													bishop_origin_column_posible = True
											if l < 6:
												if destino_row == 3 or destino_row == 6:
													bishop_origin_column_posible = True
											if l < 5:
												if destino_row == 4 or destino_row == 5:
													bishop_origin_column_posible = True
										else:
											if destino_column == 'h':
												if l > 0:
													if destino_row == 2 or destino_row == 7:
														bishop_origin_column_posible = True
												if l > 1:
													if destino_row == 3 or destino_row == 6:
														bishop_origin_column_posible = True
												if l > 2:
													if destino_row == 4 or destino_row == 5:
														bishop_origin_column_posible = True
											else:
												if destino_column == 'b':
													if l < 7 and destino_row == 3:
														bishop_origin_column_posible = True
													if l < 6:
														if destino_row == 4 or destino_row == 5:
															bishop_origin_column_posible = True
												else:
													if destino_column == 'g':
														if l > 0 and destino_row == 3:
															bishop_origin_column_posible = True
														if l > 1:
															if destino_row == 4 or destino_row == 5:
																bishop_origin_column_posible = True
													else:
														if destino_column == 'f' and l > 0 and (destino_row == 4 or destino_row == 5):
															bishop_origin_column_posible = True
														else:
															if destino_column == 'c' and l < 7 and (destino_row == 4 or destino_row == 5):
																bishop_origin_column_posible = True
										if bishop_origin_column_posible:
											available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))

						if piece_to_use == 'tmp_R' or piece_to_use == 'tmp_Q':
							tmp_str = str(piece_to_use) + str(capture) + str(destino_column) + str(destino_row)
							if not tmp_str in available_movements:
								available_movements.append(tmp_str)
							for l in range(len(self.columns)):
								tmp_str = str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row)
								if not tmp_str in available_movements:
									available_movements.append(tmp_str)
							for n in range(len(self.rows)):
								if destino_row != 1 and destino_row != 8:
									tmp_str = str(piece_to_use) + str(self.rows[n]) + str(capture) + str(destino_column) + str(destino_row)
									if not tmp_str in available_movements:
										available_movements.append(tmp_str)
						
						if piece_to_use == 'N':
							#available_movements.append(str(piece_to_use) + str(origin_column) + str(capture) + str(destino_column) + str(destino_row))
							for l in range(len(self.columns)):
								if (self.columns[l] != destino_column) and 0:
									if destino_column == 'a' and (self.columns[l] == 'b' or self.columns[l] == 'c'):
										available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
									else:
										if destino_column == 'b' and (self.columns[l] == 'a' or self.columns[l] == 'c' or self.columns[l] == 'd'):
											available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
										else:
											if destino_column == 'c' and (self.columns[l] == 'a' or self.columns[l] == 'b' or self.columns[l] == 'd' or self.columns[l] == 'e'):
												available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
											else:
												if destino_column == 'd' and (self.columns[l] == 'b' or self.columns[l] == 'c' or self.columns[l] == 'e' or self.columns[l] == 'f'):
													available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
												else:
													if destino_column == 'e' and (self.columns[l] == 'c' or self.columns[l] == 'd' or self.columns[l] == 'f' or self.columns[l] == 'g'):
														available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
													else:
														if destino_column == 'f' and (self.columns[l] == 'd' or self.columns[l] == 'e' or self.columns[l] == 'g' or self.columns[l] == 'h'):
															available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
														else:
															if destino_column == 'g' and (self.columns[l] == 'e' or self.columns[l] == 'f' or self.columns[l] == 'h'):
																available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
															else:
																if destino_column == 'h' and (self.columns[l] == 'f' or self.columns[l] == 'g'):
																	available_movements.append(str(piece_to_use) + self.columns[l] + str(capture) + str(destino_column) + str(destino_row))
						
						if piece_to_use == 'tmp_K':
							available_movements.append(str(piece_to_use) + str(origin_column) + str(capture) + str(destino_column) + str(destino_row))
						if piece_to_use == 'tmp_Q':
							available_movements.append(str(piece_to_use) + str(origin_column) + str(capture) + str(destino_column) + str(destino_row))
		
		print("Line 290 (board.py): En available_movements(). available_movements == " + str(available_movements))
	@classmethod
	def movimientosAlAzar(self, cantidad): # Agregar coronación y enroque.
		lista = ""
		i = 0
		failed = 0
		__matrizColumnas = ["a", "b", "c", "d", "e", "f", "g", "h"]
		__matrizInicialesPiezas = ["", "R", "N", "B", "K", "Q"]
		while i < cantidad:
			__f = random.randint(1, 8)
			__x = random.randint(0, 1)
			__j = random.randint(0, 1)
			
			if __x == 1:
				__x = "x"
			else:
				__x = ""

			if __j == 1:
				__j = "b"
			else:
				__j = "w"

			__c = random.randint(0, 7)
			__c = __matrizColumnas[__c]

			__p = random.randint(0, 5)
			__p = __matrizInicialesPiezas[__p]

			__movimiento = __p + __x + __c + str(__f)

			#if __p == "C":
				#print("Knight " + __j + " -->" + __movimiento)
			print("El movimiento enviado fue: " + __movimiento)
			print("\n" + self.__repr__())
			if self.mover(__movimiento) == True:
				i += 1
				#self.movimientosToFile(__movimiento, __j)
				#print("\n" + self.__repr__())
				#input()
			else:
				failed += 1
				print("Failed: " + __movimiento)

				if failed == 1000:
					print("	Aviso: 1000 fallas\n" + self.__repr__())
					input()
					failed = 0
	@classmethod
	def __repr__(self):
		retorno = "\t\t\t\t\t  =======================\n\t\t\t\t\t"

		row = 8
		for i in range(8):
			retorno += str(row) + " "
			row -= 1
			for j in range(8):
				__elementoAux = self.matrizBoard[i][j]
				retorno += str(__elementoAux) + "-"
			retorno += "\n\t\t\t\t\t"
		retorno += "  a  b  c  d  e  f  g  h"
		return retorno

	@classmethod
	def reiniciar(self):
		print('Line 196 (tablero.py): En reiniciar()')
		self.matrizBoard = []
		self.__matrizPiezas = []
		self.reglamento.turno = 'w'

		self.inicializarPiezas()
		self.colocarPiezas()

	def __init__(self):
		0