import random
from src_python.pieces.pawn import Pawn
from src_python.pieces.king import King
from src_python.pieces.queen import Queen
from src_python.pieces.bishop import Bishop
from src_python.pieces.knight import Knight
from src_python.pieces.rook import Rook
from src_python.square import Square

class Reglamento:
	__matrizColumns = ["a", "b", "c", "d", "e", "f", "g", "h"]
	__matrizRows = [8, 7, 6, 5, 4, 3, 2, 1]
	__history = []
	
	@classmethod
	def add_to_history(self, m, j, r):
		# "00 00" --> castling.
		self.__history.append([m, j, r])
	@property
	def history(self):
		return self.__history
	
	@property
	def turno(self):
		return self.__turno
	@turno.setter
	def turno(self, value):
		self.__turno = value

	@classmethod
	def is_in_check(self, player, matrizBoard):
		is_in_check = False

		for i in range(8):
			for j in range(8):
				if ((matrizBoard[i][j].piece_type == 'K') and (matrizBoard[i][j].color == player)):
					print("Line 36 (reglamento.py): En is_in_check(). Se encontró el Rey '" + player + "' en " + str(i) + str(j))

					player_aux = 'w'
					if player == 'w':
						player_aux = 'b'

					if self.accesibleParaCaballo(str(i) + str(j), player_aux, matrizBoard):
						print("Line 42 (reglamento.py): En is_in_check(). Caballo haciendo check hacia: " + str(i) + str(j))
					else:
						flag_vertical_down = True
						flag_diagonal_right_down = True
						flag_diagonal_left_down = True
						flag_diagonal_right_up = True
						flag_diagonal_left_up = True
						flag_vertical_up = True
						flag_horizontal_left = True
						flag_horizontal_right = True
						
						l = j
						m = j
						n = i
						k = i

						while flag_vertical_down or flag_diagonal_right_down or flag_diagonal_left_down or flag_diagonal_right_up or flag_diagonal_left_up or flag_vertical_up or flag_horizontal_left or flag_horizontal_right:
							if l < 7:
								l += 1
							else:
								flag_diagonal_right_down = False
								flag_diagonal_right_up = False
								flag_horizontal_right = False
							if m > 0:
								m -= 1
							else:
								flag_diagonal_left_up = False
								flag_diagonal_left_down = False
								flag_horizontal_left = False
							if n > 0:
								n -= 1
							else:
								flag_diagonal_right_up = False
								flag_diagonal_left_up = False
								flag_vertical_up = False
							if k < 7:
								k += 1
							else:
								flag_vertical_down = False
								flag_diagonal_right_down = False
								flag_diagonal_left_down = False

							print("Line 84 (reglamento.py): En is_in_check(). l == " + str(l) + ", m == " + str(m) + ", n == " + str(n) + ", k == " + str(k))

							if matrizBoard[k][j].piece_type != 'c':
								if (not is_in_check) and flag_vertical_down:
									print("Line 55 (reglamento.py): En is_in_check(). (flag_vertical_down) Se encontró un " + matrizBoard[k][j].piece_type + " en " + str(k) + str(j))
									if ((k == (i + 1)) and (matrizBoard[k][j].piece_type == 'K')):
											print("Line 51 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											return True
									else:
										if (matrizBoard[k][j].piece_type == 'R') or (matrizBoard[k][j].piece_type == 'Q'):
											if (matrizBoard[k][j].color == player_aux):
												flag_vertical_down = False
												return True
												print("Line 64 (reglamento.py): En is_in_check(). " + matrizBoard[k][j].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_vertical_down = False
											print("Line 66 (reglamento.py): En is_in_check(). flag_vertical_down == " + str(flag_vertical_down))
							if matrizBoard[k][l].piece_type != 'c':
								if (not is_in_check) and flag_diagonal_right_down:
									print("Line 56 (reglamento.py): En is_in_check(). (flag_diagonal_right_down) Se encontró un " + matrizBoard[k][l].piece_type + " en " + str(k) + str(l))
									if (k == (i + 1)):
										if (matrizBoard[k][l].piece_type == 'K'):
											print("Line 70 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
										else:
											if (matrizBoard[k][l].piece_type == 'P') and (matrizBoard[k][l].color == 'w'):
												if (matrizBoard[k][l].color == player_aux):
													flag_diagonal_right_down = False
													return True
													print("Line 78 (reglamento.py): En is_in_check(). " + matrizBoard[k][l].piece_type + " haciendo check hacia: " + str(i) + str(j))
									else:
										if (matrizBoard[k][l].piece_type == 'B') or (matrizBoard[k][l].piece_type == 'Q'):
											if (matrizBoard[k][l].color == player_aux):
												flag_diagonal_right_down = False
												return True
												print("Line 84 (reglamento.py): En is_in_check(). " + matrizBoard[k][l].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_diagonal_right_down = False
											print("Line 87 (reglamento.py): En is_in_check(). flag_diagonal_right_down == " + str(flag_diagonal_right_down))
							if matrizBoard[k][m].piece_type != 'c':
								if (not is_in_check) and flag_diagonal_left_down:
									print("Line 57 (reglamento.py): En is_in_check(). (flag_diagonal_left_down) Se encontró un " + matrizBoard[k][m].piece_type + " en " + str(k) + str(m))
									if (k == (i + 1)):
										if (matrizBoard[k][m].piece_type == 'K'):
											print("Line 70 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
										else:
											if (matrizBoard[k][m].piece_type == 'P') and (matrizBoard[k][m].color == 'w'):
												if (matrizBoard[k][m].color == player_aux):
													flag_diagonal_left_down = False
													return True
													print("Line 102 (reglamento.py): En is_in_check(). " + matrizBoard[k][m].piece_type + " haciendo check hacia: " + str(i) + str(j))
									else:
										if (matrizBoard[k][m].piece_type == 'B') or (matrizBoard[k][m].piece_type == 'Q'):
											if (matrizBoard[k][m].color == player_aux):
												flag_diagonal_left_down = False
												return True
												print("Line 108 (reglamento.py): En is_in_check(). " + matrizBoard[k][m].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_diagonal_left_down = False
											print("Line 111 (reglamento.py): En is_in_check(). flag_diagonal_left_down == " + str(flag_diagonal_left_down))
							if matrizBoard[n][l].piece_type != 'c':
								if (not is_in_check) and flag_diagonal_right_up:
									print("Line 58 (reglamento.py): En is_in_check(). (flag_diagonal_right_up) Se encontró un " + matrizBoard[n][l].piece_type + " en " + str(n) + str(l))
									if (k == (i + 1)):
										if (matrizBoard[n][l].piece_type == 'K'):
											print("Line 118 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
										else:
											if (matrizBoard[n][l].piece_type == 'P'):
												if (matrizBoard[n][l].color == 'b') and (matrizBoard[n][l].color == player_aux):
													flag_diagonal_right_up = False
													return True
													print("Line 125 (reglamento.py): En is_in_check(). " + matrizBoard[n][l].piece_type + " haciendo check hacia: " + str(i) + str(j))
									if (not is_in_check):
										if (matrizBoard[n][l].piece_type == 'B') or (matrizBoard[n][l].piece_type == 'Q'):
											if (matrizBoard[n][l].color == player_aux):
												flag_diagonal_right_up = False
												return True
												print("Line 131 (reglamento.py): En is_in_check(). " + matrizBoard[n][l].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_diagonal_right_up = False
											print("Line 134 (reglamento.py): En is_in_check(). flag_diagonal_right_up == " + str(flag_diagonal_right_up))
							if matrizBoard[n][m].piece_type != 'c':
								if (not is_in_check) and flag_diagonal_left_up:
									print("Line 58 (reglamento.py): En is_in_check(). (flag_diagonal_left_up) Se encontró un " + matrizBoard[n][m].piece_type + " en " + str(n) + str(m))
									if (k == (i + 1)):
										if (matrizBoard[n][m].piece_type == 'K'):
											print("Line 70 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
										else:
											if (matrizBoard[n][m].piece_type == 'P') and (matrizBoard[n][m].color == 'w'):
												if (matrizBoard[n][m].color == player_aux):
													flag_diagonal_left_up = False
													return True
													print("Line 78 (reglamento.py): En is_in_check(). " + matrizBoard[n][m].piece_type + " haciendo check hacia: " + str(i) + str(j))
									if (not is_in_check):
										if (matrizBoard[n][m].piece_type == 'B') or (matrizBoard[n][m].piece_type == 'Q'):
											if (matrizBoard[n][m].color == player_aux):
												flag_diagonal_left_up = False
												return True
												print("Line 84 (reglamento.py): En is_in_check(). " + matrizBoard[n][m].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_diagonal_left_up = False
											print("Line 87 (reglamento.py): En is_in_check(). flag_diagonal_left_up == " + str(flag_diagonal_left_up))
							if matrizBoard[n][j].piece_type != 'c':
								if (not is_in_check) and flag_vertical_up:
									print("Line 58 (reglamento.py): En is_in_check(). (flag_vertical_up) Se encontró un " + matrizBoard[n][j].piece_type + " en " + str(n) + str(j))
									if ((k == (i + 1)) and (matrizBoard[n][j].piece_type == 'K')):
											print("Line 51 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
									else:
										if (matrizBoard[n][j].piece_type == 'R') or (matrizBoard[n][j].piece_type == 'Q'):
											if (matrizBoard[n][j].color == player_aux):
												flag_vertical_up = False
												return True
												print("Line 64 (reglamento.py): En is_in_check(). " + matrizBoard[n][j].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_vertical_up = False
											print("Line 66 (reglamento.py): En is_in_check(). flag_vertical_up == " + str(flag_vertical_up))
							if matrizBoard[i][m].piece_type != 'c':
								if (not is_in_check) and flag_horizontal_left:
									print("Line 58 (reglamento.py): En is_in_check(). (flag_horizontal_left) Se encontró un " + matrizBoard[i][m].piece_type + " en " + str(i) + str(m))
									if ((k == (i + 1)) and (matrizBoard[i][m].piece_type == 'K')):
											print("Line 51 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
									else:
										if (matrizBoard[i][m].piece_type == 'R') or (matrizBoard[i][m].piece_type == 'Q'):
											if (matrizBoard[i][m].color == player_aux):
												flag_horizontal_left = False
												return True
												print("Line 64 (reglamento.py): En is_in_check(). " + matrizBoard[i][m].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_horizontal_left = False
											print("Line 66 (reglamento.py): En is_in_check(). flag_horizontal_left == " + str(flag_horizontal_left))
							if matrizBoard[i][l].piece_type != 'c':
								if (not is_in_check) and flag_horizontal_right:
									print("Line 58 (reglamento.py): En is_in_check(). (flag_horizontal_right) Se encontró un " + matrizBoard[i][l].piece_type + " en " + str(i) + str(l))
									if ((k == (i + 1)) and (matrizBoard[i][l].piece_type == 'K')):
											print("Line 51 (reglamento.py): En is_in_check(). Movimiento ilegal.")
											break
									else:
										if (matrizBoard[i][l].piece_type == 'R') or (matrizBoard[i][l].piece_type == 'Q'):
											if (matrizBoard[i][l].color == player_aux):
												flag_horizontal_right = False
												return True
												print("Line 64 (reglamento.py): En is_in_check(). " + matrizBoard[i][l].piece_type + " haciendo check hacia: " + str(i) + str(j))
										else:
											flag_horizontal_right = False
											print("Line 66 (reglamento.py): En is_in_check(). flag_horizontal_right == " + str(flag_horizontal_right))

	@classmethod
	def is_capture(self, movement, piece_type):
		response = False
		if piece_type == 'P' and movement[1] == "x": # Ejemplo: dxe5
			response = True
		else:
			if (piece_type == 'R' or piece_type == 'N' or piece_type == 'B' or piece_type == 'K' or piece_type == 'Q') and movement[1] == "x":
				response = True
		return response

	@classmethod
	def verify_row_column(self, movement, piece_type):
		response = False

		if piece_type == 'P':
			if self.is_capture(movement, piece_type):
				if movement[2] in self.__matrizColumns and int(movement[3]) >= 1 and int(movement[3]) <= 8:
					response = "23"
					print("Line 39.\nMovimiento = " + movement)
			else:
				if movement[0] in self.__matrizColumns and int(movement[1]) >= 1 and int(movement[1]) <= 8:
					response = "01"
		else:
			if piece_type == 'R' or piece_type == 'N' or piece_type == 'B' or piece_type == 'K' or piece_type == 'Q':
				if self.is_capture(movement, piece_type):
					if movement[2] in self.__matrizColumns and int(movement[3]) >= 1 and int(movement[3]) <= 8:
						response = "23"
				else:
					if movement[1] in self.__matrizColumns and int(movement[2]) >= 1 and int(movement[2]) <= 8:
						response = "12"
		return response

	@classmethod
	def getRowColumn(self, movement, piece_type): # Coordenadas del casillero destino.
		__d = False
		responseAux = self.verify_row_column(movement, piece_type)
		if bool(responseAux):
			__d = str(self.__matrizRows.index(int(movement[int(responseAux[1])])))
			__d += str(self.__matrizColumns.index(movement[int(responseAux[0])]))
		print("Line 60.\n__d = " + __d)
		return __d

	@classmethod
	def canBeCaptured(self, player, __d, matrizBoard):
		response = False
		if player == "w":
			if matrizBoard[int(__d[0])][int(__d[1])].piece_type != "c" and matrizBoard[int(__d[0])][int(__d[1])].color == "b":
				response = True
		else:
			if matrizBoard[int(__d[0])][int(__d[1])].piece_type != "c" and matrizBoard[int(__d[0])][int(__d[1])].color == "w":		
				response = True
		return response

	@classmethod
	def capturarConPeon(self, movement, player, __d, matrizBoard):
		response = False
		print("Line 77.")
		# Ejemplo: dxe5
		c = self.__matrizColumns.index(movement[0])
		print("La columna de origen es: " + str(c))
		if player == "w":
			#if movement == "xa7":
				#print("Revisando: " + str(int(__d[0]) + 1) + str(int(__d[1]) - 1))

			if (int(__d[0]) + 1) < 8:
				print("Revisando en: " + str(int(__d[0]) + 1) + str(c))
				#if matrizBoard[int(__d[0]) + 1][int(__d[1]) - 1].piece_type == "P" and matrizBoard[int(__d[0]) + 1][int(__d[1]) - 1].color == "w":
				if matrizBoard[int(__d[0]) + 1][c].piece_type == "P" and matrizBoard[int(__d[0]) + 1][c].color == "w":
					response = str(int(__d[0]) + 1) + str(c) + " " + __d
				#else:
			#if (int(__d[1]) + 1) < 8 and (int(__d[0]) + 1) < 8:
				#print("Revisando en: " + str(int(__d[0]) + 1) + str(int(__d[1]) + 1))
				#if matrizBoard[int(__d[0]) + 1][int(__d[1]) + 1].piece_type == "P" and matrizBoard[int(__d[0]) + 1][int(__d[1]) + 1].color == "w":
					#response = str(int(__d[0]) + 1) + str(int(__d[1]) + 1) + " " + __d				
		else:
			#if matrizBoard[int(__d[0])][int(__d[1])].piece_type != "c" and matrizBoard[int(__d[0])][int(__d[1])].color == "w":
				
			if (int(__d[0]) - 1) > -1:
				print("Revisando en: " + str(int(__d[0]) - 1) + str(c))
				if matrizBoard[int(__d[0]) - 1][c].piece_type == "P" and matrizBoard[int(__d[0]) - 1][c].color == "b":
						response = str(int(__d[0]) - 1) + str(c) + " " + __d
				#else:
			#if (int(__d[0]) - 1) != -1:
				#if matrizBoard[int(__d[0]) - 1][c].piece_type == "P" and matrizBoard[int(__d[0]) - 1][c].color == "b":
					#response = str(int(__d[0]) - 1) + str(c) + " " + __d

		return response

	@classmethod
	def capturar(self, movement, player, __d, matrizBoard, piece_type):
		response = False
		
		if piece_type == 'P':
			print("Line 107.")
			response = self.capturarConPeon(movement, player, __d, matrizBoard)
		else:
			if piece_type == 'R':
				response = self.movement(player, __d, matrizBoard, 'R', movement, 1)
			else:
				if piece_type == 'N':
					#print("...")
					response = self.movement(player, __d, matrizBoard, 'N', movement, 1)
				else:
					if piece_type == 'B':
						response = self.movement(player, __d, matrizBoard, 'B', movement, 1)
					else:
						if piece_type == 'K':
							response = self.movement(player, __d, matrizBoard, 'K', movement, 1)
						else:
							if piece_type == 'Q':
								response = self.movement(player, __d, matrizBoard, 'Q', movement, 1)

		return response

	@classmethod
	def mostrar(self, matrizBoard):
		response = "=======================\n"

		for i in range(8):
			for j in range(8):
				__elementoAux = matrizBoard[i][j]
				response += str(__elementoAux) + "-"
			response += "\n"
		return response

	@classmethod
	def piezaEnDestino(self, __d, matrizBoard):
		response = False

		if matrizBoard[int(__d[0])][int(__d[1])].piece_type != "c":
			#print("...")
			response = True

		return response

	@classmethod
	def piezaEnIntervalo(self, __d, __sd, matrizBoard, piece_type, overridePieza):
		response = False
		
		#print(str(overridePieza))
		print("En piezaEnIntervalo: __sd = " + __sd + "\npiezaEnDestino retorna: " + str(self.piezaEnDestino(__d, matrizBoard)))
		#if (not overridePieza and (not self.piezaEnDestino(__d, matrizBoard))):
		#if True:
		if len(__sd) <= 2 and (piece_type == 'R' or piece_type == 'Q'):
			if __sd[0] == "B":
				print("__sd = " + __sd + " hasta --> " + str(int(__d[0])))
				for j in range((int(__sd[1]) + overridePieza), int(__d[0])):
					
					if not overridePieza and self.piezaEnDestino(__d, matrizBoard):
						response = True
						break

					print("overridePieza = " + str(overridePieza))
					print("En " + str(j) + __d[1])
					print("Tipo: " + matrizBoard[j][int(__d[1])].piece_type)
					if j != int(__sd[1]) and matrizBoard[j][int(__d[1])].piece_type != "c":
						response = True
						break
			else:
				if __sd[0] == "S":
					for j in range((int(__d[0]) + overridePieza), int(__sd[1])):
						#print("Revisando: " + str(j) + __d[1])
						#print(self.mostrar(matrizBoard))
						#input()

						if matrizBoard[j][int(__d[1])].piece_type != "c":
							response = True
							break
				else:
					if __sd[0] == "I":
						for j in range((int(__d[1]) + overridePieza), int(__sd[1])):
							#print("Revisando: " + str(j) + __d[1])
							if matrizBoard[int(__d[0])][j].piece_type != "c":
								response = True
								break
					else:
						if __sd[0] == "D":
							for j in range((int(__sd[1]) + overridePieza), (int(__d[1]) + 1)):
								#print("Revisando: " + __d[0] + str(j))
								if j != int(__sd[1]) and matrizBoard[int(__d[0])][j].piece_type != "c":
									response = True
									break
			#else:
		#print("Line 179.\nresponse = " + str(response))
		if piece_type == 'B' or piece_type == 'Q':
			#print("En piezaEnIntervalo: __sd = " + __sd)
			try:
				if __sd[0] == "B":
					r = int(__sd[3]) # r = derecha
					l = int(__sd[3]) # l = izquierda
					
					for i in range((int(__sd[2]) + overridePieza), int(__d[0])):
					
						if not overridePieza and self.piezaEnDestino(__d, matrizBoard):
							response = True
							break
					
						#print("overridePieza = " + str(overridePieza))
						if i != int(__sd[2]):
							if l < 7:
								l += 1
							if r >= 0:
								r -= 1
						if __sd[1] == "I":
							#matrizBoard[i][r] = King()
							#print("En " + str(i) + str(l))
							#print("tipo: " + matrizBoard[i][l].piece_type)
							if i != int(__sd[2]) and matrizBoard[i][l].piece_type != "c":
								#print("Hay un " + matrizBoard[i][l].piece_type)
								#matrizBoard[i][r] = King()
								response = True
							#response = "SD" + str(i) + str(r)
						else:
							print("En " + str(i) + str(r))
							print("Tipo: " + matrizBoard[i][r].piece_type)
							if i != int(__sd[2]) and matrizBoard[i][r].piece_type != "c":
								print("Hay un " + matrizBoard[i][r].piece_type)
								#print("...")
								response = True
								#if overridePieza:
				else:
					r = int(__d[1]) # r = derecha
					l = int(__d[1]) # l = izquierda
					
					# Fuera de rango en ocasiones.
					for i in range((int(__d[0]) + overridePieza), int(__sd[2])):
						#print("En " + str(i) + str(r))
						#print("tipo: " + matrizBoard[i][r].piece_type)
						if i != int(__d[0]):
								r += 1
								l -= 1
						if __sd[1] == "I":
							if l >= 0:
								print("SI --> " + str(i) + str(l))
								if matrizBoard[i][l].piece_type != "c":
									response = True
						else:
							#print("...")
							#matrizBoard[i][r] = Torre()
							if r <= 7:
								if matrizBoard[i][r].piece_type != "c":
									response = True
			except:
				print("Line 238.\nSurgió un error.")

			

		#else:
			#print("...")
			#response = self.piezaEnDestino(__d, matrizBoard)
		print("Line 245.\nresponse = " + str(response))
		return response
	
	@classmethod
	def accesibleForTheKing(self, __d, player, matrizBoard):
		response = False
		print("Método: accesibleForTheKing")
		#[(int(__d[0]) - 1)][(int(__d[1]) - 1)] [(int(__d[0]) - 1)][int(__d[1])] [(int(__d[0]) - 1)][(int(__d[1]) + 1)]
		#   [int(__d[0])][(int(__d[1]) - 1)]                 (__d)                  [int(__d[0])][(int(__d[1]) + 1)]
		#[(int(__d[0]) + 1)][(int(__d[1]) - 1)] [(int(__d[0]) + 1)][int(__d[1])] [(int(__d[0]) + 1)][(int(__d[1]) + 1)]

		#matrizBoard[(int(__d[0]) + 1)][int(__d[1])] = Torre()

		if ((int(__d[1]) - 1) >= 0):
			if (matrizBoard[int(__d[0])][(int(__d[1]) - 1)].piece_type == "K" and matrizBoard[int(__d[0])][(int(__d[1]) - 1)].color == player):
				response = __d[0] + str((int(__d[1]) - 1))

			if ((int(__d[1]) + 1) <= 7):
				if (matrizBoard[int(__d[0])][(int(__d[1]) + 1)].piece_type == "K" and matrizBoard[int(__d[0])][(int(__d[1]) + 1)].color == player):
					response = __d[0] + str((int(__d[1]) + 1))

			if ((int(__d[0]) - 1) >= 0):
				if (matrizBoard[(int(__d[0]) - 1)][int(__d[1])].piece_type == "K" and matrizBoard[(int(__d[0]) - 1)][int(__d[1])].color == player):
					response = str((int(__d[0]) - 1)) + __d[1]

			if ((int(__d[0]) + 1) <= 7):
				if (matrizBoard[(int(__d[0]) + 1)][int(__d[1])].piece_type == "K" and matrizBoard[(int(__d[0]) + 1)][int(__d[1])].color == player):
					response = str((int(__d[0]) + 1)) + __d[1]

			if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) - 1) >= 0):
				if (matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) - 1)].piece_type == "K" and matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) - 1)].color == player):
					response = str((int(__d[0]) + 1)) + str((int(__d[1]) - 1))

			if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) + 1) <= 7):
				if (matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) + 1)].piece_type == "K" and matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) + 1)].color == player):
					response = str((int(__d[0]) - 1)) + str((int(__d[1]) + 1))

			if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) + 1) <= 7):
				if (matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) + 1)].piece_type == "K" and matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) + 1)].color == player):
					response = str((int(__d[0]) + 1)) + str((int(__d[1]) + 1))

			if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) - 1) >= 0):
				if (matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) - 1)].piece_type == "K" and matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) - 1)].color == player):
					response = str((int(__d[0]) - 1)) + str((int(__d[1]) - 1))

		return response
	
	@classmethod
	def accesibleParaCaballo(self, __d, player, matrizBoard):
		response = False
	
		print("Line 349 (reglamento.py): En accesibleParaCaballo(). __d == " + __d)

		if ((int(__d[0]) + 2) <= 7 and (int(__d[1]) + 1) <= 7):
			if (matrizBoard[(int(__d[0]) + 2)][(int(__d[1]) + 1)].piece_type == "N" and matrizBoard[(int(__d[0]) + 2)][(int(__d[1]) + 1)].color == player):
				response = str((int(__d[0]) + 2)) + str((int(__d[1]) + 1))
		if ((int(__d[0]) + 2) <= 7 and (int(__d[1]) - 1) >= 0):
			if (matrizBoard[(int(__d[0]) + 2)][(int(__d[1]) - 1)].piece_type == "N" and matrizBoard[(int(__d[0]) + 2)][(int(__d[1]) - 1)].color == player):
				response = str((int(__d[0]) + 2)) + str((int(__d[1]) - 1))
		if ((int(__d[0]) - 2) >= 0 and (int(__d[1]) + 1) <= 7):
			if (matrizBoard[(int(__d[0]) - 2)][(int(__d[1]) + 1)].piece_type == "N" and matrizBoard[(int(__d[0]) - 2)][(int(__d[1]) + 1)].color == player):
				response = str((int(__d[0]) - 2)) + str((int(__d[1]) + 1))
		if ((int(__d[0]) - 2) >= 0 and (int(__d[1]) - 1) >= 0):
			if (matrizBoard[(int(__d[0]) - 2)][(int(__d[1]) - 1)].piece_type == "N" and matrizBoard[(int(__d[0]) - 2)][(int(__d[1]) - 1)].color == player):
				response = str((int(__d[0]) - 2)) + str((int(__d[1]) - 1))
		if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) + 2) <= 7):
			if (matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) + 2)].piece_type == "N" and matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) + 2)].color == player):
				response = str((int(__d[0]) + 1)) + str((int(__d[1]) + 2))
		if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) - 2) >= 0):
			if (matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) - 2)].piece_type == "N" and matrizBoard[(int(__d[0]) + 1)][(int(__d[1]) - 2)].color == player):
				response = str((int(__d[0]) + 1)) + str((int(__d[1]) - 2))
		if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) + 2) <= 7):
			if (matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) + 2)].piece_type == "N" and matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) + 2)].color == player):
				response = str((int(__d[0]) - 1)) + str((int(__d[1]) + 2))
		if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) - 2) >= 0):
			if (matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) - 2)].piece_type == "N" and matrizBoard[(int(__d[0]) - 1)][(int(__d[1]) - 2)].color == player):
					response = str((int(__d[0]) - 1)) + str((int(__d[1]) - 2))
		return response

	@classmethod
	def sentidoDireccion(self, movement, player, matrizBoard, __d):
		# S, B, I, D
		response = False

		# Ver que pasa si por ejemplo 2 Torres están en la misma fila o columna y una puede moverse a un punto determinado y otra no puede.
		# Podría concatenar las ubicaciones de las piezas similares (D3 I7)

		__p = self.identificarPieza(movement, player, matrizBoard)

		if __p == "B":
			#print("...")
			#print("La pieza es: " + __p + "\nEl destino es: " + __d)
			r = int(__d[1]) # r = derecha
			l = int(__d[1]) # l = izquierda
			for i in range(int(__d[0]), 8):
				if i != int(__d[0]):
					#if r < 7 and l > 0:
					r += 1
					l -= 1
				#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
				if r <= 7:
					if matrizBoard[i][r].piece_type == __p and matrizBoard[i][r].color == player:
						response = "SD" + str(i) + str(r)
				if l >= 0:
					if matrizBoard[i][l].piece_type == __p and matrizBoard[i][l].color == player:
						response = "SI" + str(i) + str(l)
			
			r = int(__d[1]) # r = derecha
			l = int(__d[1]) # l = izquierda
			#matrizBoard[int(__d[0])][int(__d[1])] = King()
			#print("D: " + __d)
			i = int(__d[0])
			while i >= 0:
				if i != int(__d[0]):
					r += 1
					l -= 1
				#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
				#matrizBoard[i][r] = King()
				#matrizBoard[i][l] = Caballo()
				#print("Tipo: " + matrizBoard[i][r].piece_type)
				if r <= 7:
					if matrizBoard[i][r].piece_type == __p and matrizBoard[i][r].color == player:
						response = "BD" + str(i) + str(r)
				if l >= 0:
					if matrizBoard[i][l].piece_type == __p and matrizBoard[i][l].color == player:
						response = "BI" + str(i) + str(l)

				i -= 1
			#self.mostrar(matrizBoard)
			#input()
		else:
			if __p == "R":
				#print("response = " + str(response))
				for i in range(int(__d[0]), 8):
					if matrizBoard[i][int(__d[1])].piece_type == __p and matrizBoard[i][int(__d[1])].color == player:
						response = "S" + str(i)
				if not response:
					i = int(__d[0])
					while i >= 0:
						if matrizBoard[i][int(__d[1])].piece_type == __p and matrizBoard[i][int(__d[1])].color == player:
							response = "B" + str(i)
						i -= 1
					if not response:
						i = int(__d[1])
						while i >= 0:
							if matrizBoard[int(__d[0])][i].piece_type == __p and matrizBoard[int(__d[0])][i].color == player:
								response = "D" + str(i)
								#print("...")
							i -= 1
						if not response:
							for i in range(int(__d[1]), 8):
								if matrizBoard[int(__d[0])][i].piece_type == __p and matrizBoard[int(__d[0])][i].color == player:
									response = "I" + str(i)
									#print("...")
			else:
				if __p == "Q":
					#print("Line 405.\nresponse = " + str(response))
					for i in range(int(__d[0]), 8):
						if matrizBoard[i][int(__d[1])].piece_type == __p and matrizBoard[i][int(__d[1])].color == player:
							response = "S" + str(i)
					if not response:
						i = int(__d[0])
						while i >= 0:
							if matrizBoard[i][int(__d[1])].piece_type == __p and matrizBoard[i][int(__d[1])].color == player:
								response = "B" + str(i)
							i -= 1
						if not response:
							i = int(__d[1])
							while i >= 0:
								if matrizBoard[int(__d[0])][i].piece_type == __p and matrizBoard[int(__d[0])][i].color == player:
									response = "D" + str(i)

									#if movement == "Qf1":
										#print("Line 422.\nTipo = " + matrizBoard[int(__d[0])][i].piece_type + " en " + __d[0] + str(i))
									#print("...")
									#matrizBoard[int(__d[0])][i] = Caballo()
								i -= 1
							if not response:
								for i in range(int(__d[1]), 8):
									if matrizBoard[int(__d[0])][i].piece_type == __p and matrizBoard[int(__d[0])][i].color == player:
										response = "I" + str(i)
										#print("...")
					print("Line 427.\nresponse = " + str(response))
					if not response:
						print("Line 429.")
						r = int(__d[1]) # r = derecha
						l = int(__d[1]) # l = izquierda
						for i in range(int(__d[0]), 8):
							if i != int(__d[0]):
								#if r < 7 and l > 0:
								r += 1
								l -= 1
							#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
							if r <= 7:
								if matrizBoard[i][r].piece_type == __p and matrizBoard[i][r].color == player:
									response = "SD" + str(i) + str(r)
							if l >= 0:
								if matrizBoard[i][l].piece_type == __p and matrizBoard[i][l].color == player:
									response = "SI" + str(i) + str(l)
						
						r = int(__d[1]) # r = derecha
						l = int(__d[1]) # l = izquierda
						#matrizBoard[int(__d[0])][int(__d[1])] = King()
						#print("D: " + __d)
						i = int(__d[0])
						while i >= 0:
							if i != int(__d[0]):
								r += 1
								l -= 1
							#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
							#matrizBoard[i][r] = King()
							#matrizBoard[i][l] = Caballo()
							#print("Tipo: " + matrizBoard[i][r].piece_type)
							if r <= 7:
								if matrizBoard[i][r].piece_type == __p and matrizBoard[i][r].color == player:
									response = "BD" + str(i) + str(r)
							if l >= 0:
								if matrizBoard[i][l].piece_type == __p and matrizBoard[i][l].color == player:
									response = "BI" + str(i) + str(l)

							i -= 1
					print("Line 467.\nresponse = " + str(response))
		return response

	@classmethod
	def movement(self, player, __d, matrizBoard, piece_type, movement, overridePieza):
		response = False

		if piece_type == 'P':
			if player == "w":
				print("El jugador es: " + player)
				for i in range(8):
					if i >= int(__d[0]) and i <= 7:
						print("Line 539 (reglamento.py): En movement(), revisando en: " + str(i) + __d[1] + ', piece_type = ' + matrizBoard[i][int(__d[1])].piece_type)
						#matrizBoard[i][int(__d[1])] = Rook()
						#matrizBoard[i][int(__d[1])].color = 'w'
						if matrizBoard[i][int(__d[1])].piece_type == "P" and matrizBoard[i][int(__d[1])].color == "w":
							print("Se encontró un Pb en:" + str(i) + __d[1])
							if (int(__d[0]) == (i-1)) or (int(__d[0]) == (i-2) and i == 6): # Movimiento simple o doble.
								print("Es un movement simple o doble de un peón.")
								print("El destino es: " + __d)
								response = str(i) + __d[1] + " " + __d
								break
						else:
							if matrizBoard[i][int(__d[1])].piece_type != "c":
								break
			else:
				i = int(__d[0])
				while i >= 0:
					if matrizBoard[i][int(__d[1])].piece_type == "P" and matrizBoard[i][int(__d[1])].color == "b":
						if (int(__d[0]) == (i+1)) or (int(__d[0]) == (i+2) and i == 1): # Movimiento simple de a un casillero.
								response = str(i) + __d[1] + " " + __d
						break
					else:
						if matrizBoard[i][int(__d[1])].piece_type != "c": #Hay una pieza en el camino, el peón no puede saltarla.
							break
					i -= 1
		else:
			if piece_type == 'R':
				__sd = self.sentidoDireccion(movement, player, matrizBoard, __d)
				if type(__sd) != type(bool()):
					print("El sentidoDireccion retornó: " + __sd)
					if not self.piezaEnIntervalo(__d, __sd, matrizBoard, piece_type, overridePieza):
						if __sd[0] == "S" or __sd[0] == "B":
							response = __sd[1] + __d[1] + " " + __d
						else:
							if __sd[0] == "I" or __sd[0] == "D":
								response = __d[0] + __sd[1] + " " + __d
			else:
				if piece_type == 'N':
					__o = self.accesibleParaCaballo(__d, player, matrizBoard)
					print("Line 534.\n __o == " + str(__o))
					if type(__o) != type(bool()):
						if not overridePieza:
							if not self.piezaEnDestino(__d, matrizBoard):
								response = __o + " " + __d
						else:
							#print("...")
							response = __o + " " + __d
				else:
					if piece_type == 'B':
						print("piece_type = " + piece_type)
						__sd = self.sentidoDireccion(movement, player, matrizBoard, __d)
						if type(__sd) != type(bool()):
							print("El sentidoDireccion retornó: " + __sd)
							if not self.piezaEnIntervalo(__d, __sd, matrizBoard, piece_type, overridePieza):
								#print("Line 464.")
								response = __sd[2] + __sd[3] + " " + __d
							else:
								0
					else:
						if piece_type == 'K':
							__o = self.accesibleForTheKing(__d, player, matrizBoard)
							print("accesibleForTheKing retornó: " + str(__o))
							if type(__o) != type(bool()):
								print("overridePieza = " + str(overridePieza))
								if not overridePieza:
									if not self.piezaEnDestino(__d, matrizBoard):
										response = __o + " " + __d
								else:
									if self.piezaEnDestino(__d, matrizBoard):
										response = __o + " " + __d
						else:
							if piece_type == 'Q':
								__sd = self.sentidoDireccion(movement, player, matrizBoard, __d)
								print("El sentidoDireccion retornó: " + str(__sd))
								#input()
								if (type(__sd) != type(bool())):
									print("Line 554.")
									if len(__sd) == 2:
										#print("El sentidoDireccion retornó: " + __sd)
										if not self.piezaEnIntervalo(__d, __sd, matrizBoard, piece_type, overridePieza):
											print("No hay pieza en intervalo.")
											if __sd[0] == "S" or __sd[0] == "B":
												response = __sd[1] + __d[1] + " " + __d
											else:
												if __sd[0] == "I" or __sd[0] == "D":
													response = __d[0] + __sd[1] + " " + __d
										else:
											print("Hay pieza en intervalo.")
									else:
										if not response:
											print("No mueve como torre.")
											#__sd = self.sentidoDireccion(movement, player, matrizBoard, __d)
											if type(__sd) != type(bool()):
												print("Line 561.\nEl sentidoDireccion retornó: " + __sd)
												if not self.piezaEnIntervalo(__d, __sd, matrizBoard, piece_type, overridePieza):
													#print("Line 464.")
													response = __sd[2] + __sd[3] + " " + __d
										else:
											print("Mueve como torre.")
		return response

	@classmethod
	def moverPeon(self, movement, player, matrizBoard):
		response = False

		print("Line 641.\nplayer == " + str(player))

		matrizInicialesPiezas = ["R", "N", "B", "K", "Q"]
		
		__d = self.getRowColumn(movement, 'P')
		print("El getRowColumn retornó: " + __d)
		
		if self.is_capture(movement, 'P'):
			if bool(__d):
				if self.canBeCaptured(player, __d, matrizBoard):
					if (((movement[3] == '1' and player == 'b') or (movement[3] == '8' and player == 'w')) and (not '=' in movement)):
						print("Line 653 (reglamento.py): En moverPeon(). movement[3] == " + movement[3] + ", player == " + player)
						response = False
					else:
						response = self.capturar(movement, player, __d, matrizBoard, 'P')
		else:
			if (((movement[1] == '1' and player == 'b') or (movement[1] == '8' and player == 'w')) and (not '=' in movement)):
				print("Line 660 (reglamento.py): En moverPeon(). movement[1] == " + movement[1] + ", player == " + player)
				response = False
			else:
				response = self.movement(player, __d, matrizBoard, 'P', movement, 0)
			print("El movement retornó: " + str(response))

		if response and "=" in movement: # Este bloque realiza la promoción del Peon.
			if self.is_capture(movement, 'P'):
				print("Line 647.")
				if len(movement) == 6: # La longitud requerida para que sea una promoción.
					if (movement[5] in matrizInicialesPiezas) and (movement[5] != 'K'):
						matrizBoard[int(response[0])][int(response[1])].piece_type = movement[5]
						#print("El tipo es: " + matrizBoard[int(response[0])][int(response[1])].piece_type)
					else:
						response = False
				else:
					response = False
					#if len(movement) == 4 and ((movement[3] == "8" and player == "w") or (movement[3] == "1" and player == "b")):
						#response = False
			else:
				if (len(movement) == 4) and (movement[3] in matrizInicialesPiezas) and (movement[3] != 'K'):
					matrizBoard[int(response[0])][int(response[1])].piece_type = movement[3]
				else:
					print("Line 672 (reglamento.py): En moverPeon(). movement[3] == " + movement[3])
					response = False
					#if len(movement) == 2 and ((movement[1] == "8" and player == "w") or (movement[1] == "1" and player == "b")):
						#response = False
		else: # Este bloque realiza la captura al paso.
			if self.is_capture(movement, 'P'):
				if len(movement) == 8: # La longitud requerida para que sea una captura al paso.
					if movement[4] == 'e' and movement[5] == '.' and movement[6] == 'p' and movement[7] == '.':
						print("Line 665.\nes captura al paso...")
						c = self.__matrizColumns.index(movement[0])
						print("Line 680 (reglamento.py): En moverPeon(). La columna de origen es: " + str(c))
						if player == "w":
							if (int(__d[0]) + 1) < 8:
								print("Line 683 (reglamento.py): En moverPeon(). En: " + str(int(__d[0])) + str(c) + " hay un: "  + matrizBoard[int(__d[0])][c].piece_type)
								#matrizBoard[int(__d[0]) + 1][int(__d[1])] = Pawn()
								if matrizBoard[int(__d[0])][c].piece_type == "P" and matrizBoard[int(__d[0])][c].color == "w":
									if matrizBoard[int(__d[0])][int(__d[1])].piece_type == "P" and matrizBoard[int(__d[0])][int(__d[1])].color == "b":
										if self.ultimateMovementWas(movement[2] + movement[3] ,"double_movement"):
											print("Line 693 (reglamento.py): En moverPeon(). El último movimiento fue 'double_movement'.")
											if matrizBoard[int(__d[0]) + 1][c].piece_type == "c":
												matrizBoard[int(__d[0])][int(__d[1])] = Square()

												direccion = 1
												if int(__d[1]) == (c - 1):
													direccion = -1
												response = str(int(__d[0])) + str(c) + " " + str(int(__d[0]) - 1) + str(c + direccion)
										print("Line 691 (reglamento.py): En moverPeon(). response == " + str(response))
						else:
							if (int(__d[0]) - 1) > -1:
								print("Line 699 (reglamento.py): En moverPeon(). En: " + str(int(__d[0])) + str(c) + " hay un: "  + matrizBoard[int(__d[0])][c].piece_type)
								#matrizBoard[int(__d[0]) + 1][int(__d[1])] = Pawn()
								if matrizBoard[int(__d[0])][c].piece_type == "P" and matrizBoard[int(__d[0])][c].color == "b":
									if matrizBoard[int(__d[0])][int(__d[1])].piece_type == "P" and matrizBoard[int(__d[0])][int(__d[1])].color == "w":
										if self.ultimateMovementWas(movement[2] + movement[3] ,"double_movement"):
											print("Line 709 (reglamento.py): En moverPeon(). El último movimiento fue 'double_movement'.")
											if matrizBoard[int(__d[0]) + 1][c].piece_type == "c":
												matrizBoard[int(__d[0])][int(__d[1])] = Square()
												
												direccion = 1
												if int(__d[1]) == (c - 1):
													direccion = -1
												
												response = str(int(__d[0])) + str(c) + " " + str(int(__d[0]) + 1) + str(c + direccion)

										print("Line 714 (reglamento.py): En moverPeon(). response == " + str(response))

		return response

	@classmethod
	def ultimateMovementWas(self, notation, description = None):
		descriptions = ['double_movement']
		print("Line 726 (reglamento.py): En ultimateMovementWas(). self.__history[len(self.__history) - 1][0] == " + str(self.__history[len(self.__history) - 1][0]))
		if notation == self.__history[len(self.__history) - 1][0]:
			if (description != None) and (description in descriptions):
				return True

		return False

	@classmethod
	def moverAlfil(self, movement, player, matrizBoard):
		print("En moverAlfil.")
		response = False
		__d = self.getRowColumn(movement, 'B')
		print("El getRowColumn retornó: " + str(__d))

		if self.is_capture(movement, 'B'):
			if bool(__d):
				if self.canBeCaptured(player, __d, matrizBoard):
					#print("...")
					response = self.capturar(
						movement, player, 
						__d, matrizBoard, 'B'
					)
		else:
			print("En moverAlfil. is_capture == False.")
			
			response = self.movement(
				player, __d, matrizBoard, 'B', movement, 0
				)
			print("El movement retornó: " + str(response))

		if type(response) == type(str()) and (
				response[0] + response[1] == response[3] + response[4]):
			response = False

		return response

	@classmethod
	def moverTorre(self, movement, player, matrizBoard):
		print("En moverTorre.")
		response = False
		__d = self.getRowColumn(movement, 'R')
		print("El getRowColumn retornó: " + str(__d))
		
		if self.is_capture(movement, 'R'):
			if bool(__d):
				if self.canBeCaptured(player, __d, matrizBoard):
					response = self.capturar(
						movement, player, 
						__d, matrizBoard, 'R'
					)
		else:
			print("En moverTorre. is_capture == False.")
			
			response = self.movement(
				player, __d, matrizBoard, 'R', movement, 0
				)
			print("El movement retornó: " + str(response))

		if type(response) == type(str()) and (
				response[0] + response[1] == response[3] + response[4]):
			response = False
		return response

	@classmethod
	def moveQueen(self, movement, player, matrizBoard):
		print("En moveQueen.")
		response = False
		__d = self.getRowColumn(movement, 'Q')
		print("El getRowColumn retornó: " + str(__d))

		#f = self.find("Q", player)

		#matrizBoard[int(f[0])][int(f[1])].piece_type = "A"

		if self.is_capture(movement, 'Q'):
			if self.canBeCaptured(player, __d, matrizBoard):
				print("Line 655.\nLa pieza es capturable.")
				response = self.capturar(
					movement, player, __d, matrizBoard, 'Q'
					)
		else:
			print("En moveQueen. is_capture == False.")
			
			response = self.movement(
				player, __d, matrizBoard, 'Q', movement, 0
				)
			print("El movement retornó: " + str(response))

		if type(response) == type(str()) and (
				response[0] + response[1] == response[3] + response[4]): # Revisa que no sea el mismo lugar donde está.
			response = False

		return response

	@classmethod
	def moveKing(self, movement, player, matrizBoard):
		print("En moveKing.")
		response = False
		__d = self.getRowColumn(movement, 'K')
		print("El getRowColumn retornó: " + str(__d))

		if self.is_capture(movement, 'K'):
			if self.canBeCaptured(player, __d, matrizBoard):
				response = self.capturar(
					movement, player, __d, matrizBoard, 'K'
					)
		else:
			print("En moveKing. is_capture == False.")
			
			response = self.movement(
				player, __d, matrizBoard, 'K', movement, 0
				)
			print("El movement retornó: " + str(response))

		if type(response) == type(str()) and (
				response[0] + response[1] == response[3] + response[4]): # Revisa que no sea el mismo lugar donde está.
			response = False

		return response

	@classmethod
	def moverCaballo(self, movement, player, matrizBoard):
		print("En moverCaballo.")
		response = False
		__d = self.getRowColumn(movement, 'N')
		print("El getRowColumn retornó: " + str(__d))

		if self.is_capture(movement, 'N'):
			if self.canBeCaptured(player, __d, matrizBoard):
				response = self.capturar(movement, player, __d, matrizBoard, 'N')
		else:
			print("En moverCaballo. is_capture == False.")
			
			response = self.movement(
				player, __d, matrizBoard, 'N', movement, 0
				)
			print("El movement retornó: " + str(response))

		if type(response) == type(str()) and (
				response[0] + response[1] == response[3] + response[4]): # Revisa que no sea el mismo lugar donde está.
			response = False

		return response

	@classmethod
	def castling(self, movement, player, matrizBoard): # enroque.
		response = False

		if player == "w":
			if len(movement) == 3: # 0-0
				if (
						matrizBoard[7][7].piece_type == "R" and matrizBoard[7][7].color == player and matrizBoard[7][6].piece_type == "c" and matrizBoard[7][5].piece_type == "c" and matrizBoard[7][4].piece_type == "K" and matrizBoard[7][4].color == player):
					response = "00 00" # Este response se hace para que en tablero.moverOD no haga cambios.

					matrizBoard[7][5] = matrizBoard[7][7]
					matrizBoard[7][7] = Square()

					matrizBoard[7][6] = matrizBoard[7][4]
					matrizBoard[7][4] = Square()
			else:
				if len(movement) == 5: # 0-0-0
					if (
							matrizBoard[7][0].piece_type == "R" and matrizBoard[7][0].color == player and matrizBoard[7][1].piece_type == "c" and matrizBoard[7][2].piece_type == "c" and matrizBoard[7][3].piece_type == "Q" and matrizBoard[7][3].color == player):
						response = "00 00" # Este response se hace para que en tablero.moverOD no haga cambios.

						matrizBoard[7][2] = matrizBoard[7][3]
						matrizBoard[7][3] = Square()

						matrizBoard[7][3] = matrizBoard[7][0]
						matrizBoard[7][0] = Square()
		else:
			if len(movement) == 3: # 0-0
				if (
						matrizBoard[0][7].piece_type == "R" and matrizBoard[0][7].color == player and matrizBoard[0][6].piece_type == "c" and matrizBoard[0][5].piece_type == "c" and matrizBoard[0][4].piece_type == "K" and matrizBoard[0][4].color == player):
					response = "00 00" # Este response se hace para que en tablero.moverOD no haga cambios.

					matrizBoard[0][5] = matrizBoard[0][7]
					matrizBoard[0][7] = Square()

					matrizBoard[0][6] = matrizBoard[0][4]
					matrizBoard[0][4] = Square()
			else:
				if len(movement) == 5: # 0-0-0
					if (
							matrizBoard[0][0].piece_type == "R" and matrizBoard[0][0].color == player and matrizBoard[0][1].piece_type == "c" and matrizBoard[0][2].piece_type == "c" and matrizBoard[0][3].piece_type == "Q" and matrizBoard[0][3].color == player):
						
						response = "00 00" # Este response se hace para que en tablero.moverOD no haga cambios.

						matrizBoard[0][2] = matrizBoard[0][3]
						matrizBoard[0][3] = Square()

						matrizBoard[0][3] = matrizBoard[0][0]
						matrizBoard[0][0] = Square()

		if response:
			self.cambiarTurno(player)
		return response

	@classmethod
	def verifyTurno(self, jugador):
		response = False
		if jugador == self.turno:
			response = True
		return response

	@classmethod
	def cambiarTurno(self, player):
		print('Line 901 (reglamento.py): En cambiarTurno(), player == ' + player)
		if player == "w":
			self.turno = "b"
			#print('Line 904 (reglamento.py): En cambiarTurno(), se cambió el turno a:' + self.turno)
		else:
			self.turno = "w"

	@classmethod
	def identificarPieza(self, movement, player, matrizBoard):
		response = "P"

		__matrizInicialesPiezas = ["R", "N", "B", "K", "Q"]
		if movement[0] in __matrizInicialesPiezas:
			if movement[0] == "R":
					response = "R"
			else:
				if movement[0] == "N":
					response = "N"
				else:
					if movement[0] == "B":
						response = "B"
					else:
						if movement[0] == "K":
							response = "K"
						else:
							if movement[0] == "Q":
								response = "Q"
		return response

	@classmethod
	def identificarMoverPieza(self, movement, jugador, matrizBoard):
		response = False

		__matrizInicialesPiezas = ["R", "N", "B", "K", "Q"]
		if movement[0] in __matrizInicialesPiezas:
			if movement[0] == "R":
				response = self.moverTorre(
					movement, jugador, matrizBoard
					)
			else:
				if movement[0] == "N":
					response = self.moverCaballo(
						movement, jugador, matrizBoard
						)
				else:
					if movement[0] == "B":
						response = self.moverAlfil(
							movement, jugador, matrizBoard
							)
					else:
						if movement[0] == "K":
							response = self.moveKing(
								movement, jugador, matrizBoard
								)
						else:
							if movement[0] == "Q":
								response = self.moveQueen(
									movement, jugador, matrizBoard
									)
		else:
			print("Line 919.")
			if movement == "0-0" or movement == "0-0-0":
				response = self.castling(movement, jugador, matrizBoard)
			else:
				print("Line 923.")
				response = self.moverPeon(movement, jugador, matrizBoard)
				print("El moverPeon retornó: " + str(response))

		return response

	@classmethod
	def verifySintaxis(self, m, p):
		# p = player, m = movement.
		response = True

		#if len(m) == 3: # Corresponde a la captura de un peon o a ...print('Line 995 (reglamento.py): En mover(), se cambió el turno a: ' + self.turno)
			#if m[0] == "x": # Corresponde a la captura de un peon.

			#if m[0] in self.__matrizColumns: # Es una columna válida.
		return response

	@classmethod
	def mover(self, movement, turno, matrizBoard):
		response = False
		
		#self.turno = turno
		
		#if self.verifySintaxis(movement, jugador):

		response = self.identificarMoverPieza(movement, turno, matrizBoard)
		print("El identificarMoverPieza retornó: " + str(response))
		if response:

			#self.is_in_check(turno, matrizBoard)
			#self.history.append(movement, self.turno, response)
			self.add_to_history(movement, self.turno, response)
			self.cambiarTurno(turno)
			print('Line 1219 (reglamento.py): En mover(), se cambió el turno a: ' + self.turno)
				
		return response

	def __init__(self):
		print('Line 1224 (reglamento.py): En __init__().')
		self.__turno = 'w'