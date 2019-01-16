import random
from clases_py.piezas.pawn import Pawn
from clases_py.piezas.king import King
from clases_py.piezas.queen import Queen
from clases_py.piezas.bishop import Bishop
from clases_py.piezas.knight import Knight
from clases_py.piezas.root import Root
from clases_py.casillero import Casillero

class Reglamento:
	__matrizColumnas = ["a", "b", "c", "d", "e", "f", "g", "h"]
	__matrizFilas = [8, 7, 6, 5, 4, 3, 2, 1]
	__history = []
	
	@classmethod
	def addToHistory(self, m, j, r):
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
	def esCaptura(self, __movimiento, __nombreMetodo):
		retorno = False
		if __nombreMetodo == "moverPeon" and __movimiento[1] == "x": # Ejemplo: dxe5
			retorno = True
		else:
			if (__nombreMetodo == "moverTorre" or __nombreMetodo == "moverCaballo" or __nombreMetodo == "moverAlfil" or __nombreMetodo == "moveKing" or __nombreMetodo == "moveQueen") and __movimiento[1] == "x":
				retorno = True
		return retorno

	@classmethod
	def verificarFilaColumna(self, __movimiento, __nombreMetodo):
		retorno = False

		if __nombreMetodo == "moverPeon":
			if self.esCaptura(__movimiento, __nombreMetodo):
				if __movimiento[2] in self.__matrizColumnas and int(__movimiento[3]) >= 1 and int(__movimiento[3]) <= 8:
					retorno = "23"
					print("Line 39.\nMovimiento = " + __movimiento)
			else:
				if __movimiento[0] in self.__matrizColumnas and int(__movimiento[1]) >= 1 and int(__movimiento[1]) <= 8:
					retorno = "01"
		else:
			if __nombreMetodo == "moverTorre" or __nombreMetodo == "moverCaballo" or __nombreMetodo == "moverAlfil" or __nombreMetodo == "moveKing" or __nombreMetodo == "moveQueen":
				if self.esCaptura(__movimiento, __nombreMetodo):
					if __movimiento[2] in self.__matrizColumnas and int(__movimiento[3]) >= 1 and int(__movimiento[3]) <= 8:
						retorno = "23"
				else:
					if __movimiento[1] in self.__matrizColumnas and int(__movimiento[2]) >= 1 and int(__movimiento[2]) <= 8:
						retorno = "12"
		return retorno

	@classmethod
	def obtenerFilaColumna(self, __movimiento, __nombreMetodo): # Coordenadas del casillero destino.
		__d = False
		retornoAux = self.verificarFilaColumna(__movimiento, __nombreMetodo)
		if bool(retornoAux):
			__d = str(self.__matrizFilas.index(int(__movimiento[int(retornoAux[1])])))
			__d += str(self.__matrizColumnas.index(__movimiento[int(retornoAux[0])]))
		print("Line 60.\n__d = " + __d)
		return __d

	@classmethod
	def esCapturable(self, __jugador, __d, matrizTablero):
		retorno = False
		if __jugador == "w":
			if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c" and matrizTablero[int(__d[0])][int(__d[1])].color == "b":
				retorno = True
		else:
			if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c" and matrizTablero[int(__d[0])][int(__d[1])].color == "w":		
				retorno = True
		return retorno

	@classmethod
	def capturarConPeon(self, __movimiento, __jugador, __d, matrizTablero):
		retorno = False
		print("Line 77.")
		# Ejemplo: dxe5
		c = self.__matrizColumnas.index(__movimiento[0])
		print("La columna de origen es: " + str(c))
		if __jugador == "w":
			#if __movimiento == "xa7":
				#print("Revisando: " + str(int(__d[0]) + 1) + str(int(__d[1]) - 1))

			if (int(__d[0]) + 1) < 8:
				print("Revisando en: " + str(int(__d[0]) + 1) + str(c))
				#if matrizTablero[int(__d[0]) + 1][int(__d[1]) - 1].tipo == "P" and matrizTablero[int(__d[0]) + 1][int(__d[1]) - 1].color == "w":
				if matrizTablero[int(__d[0]) + 1][c].tipo == "P" and matrizTablero[int(__d[0]) + 1][c].color == "w":
					retorno = str(int(__d[0]) + 1) + str(c) + " " + __d
				#else:
			#if (int(__d[1]) + 1) < 8 and (int(__d[0]) + 1) < 8:
				#print("Revisando en: " + str(int(__d[0]) + 1) + str(int(__d[1]) + 1))
				#if matrizTablero[int(__d[0]) + 1][int(__d[1]) + 1].tipo == "P" and matrizTablero[int(__d[0]) + 1][int(__d[1]) + 1].color == "w":
					#retorno = str(int(__d[0]) + 1) + str(int(__d[1]) + 1) + " " + __d				
		else:
			#if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c" and matrizTablero[int(__d[0])][int(__d[1])].color == "w":
				
			if (int(__d[0]) - 1) > -1:
				print("Revisando en: " + str(int(__d[0]) - 1) + str(c))
				if matrizTablero[int(__d[0]) - 1][c].tipo == "P" and matrizTablero[int(__d[0]) - 1][c].color == "b":
						retorno = str(int(__d[0]) - 1) + str(c) + " " + __d
				#else:
			#if (int(__d[0]) - 1) != -1:
				#if matrizTablero[int(__d[0]) - 1][c].tipo == "P" and matrizTablero[int(__d[0]) - 1][c].color == "b":
					#retorno = str(int(__d[0]) - 1) + str(c) + " " + __d

		return retorno

	@classmethod
	def capturar(self, __movimiento, __jugador, __d, matrizTablero, __nombreMetodo):
		retorno = False
		
		if __nombreMetodo == "moverPeon":
			print("Line 107.")
			retorno = self.capturarConPeon(__movimiento, __jugador, __d, matrizTablero)
		else:
			if __nombreMetodo == "moverTorre":
				retorno = self.movimiento(__jugador, __d, matrizTablero, "moverTorre", __movimiento, 1)
			else:
				if __nombreMetodo == "moverCaballo":
					#print("...")
					retorno = self.movimiento(__jugador, __d, matrizTablero, "moverCaballo", __movimiento, 1)
				else:
					if __nombreMetodo == "moverAlfil":
						retorno = self.movimiento(__jugador, __d, matrizTablero, "moverAlfil", __movimiento, 1)
					else:
						if __nombreMetodo == "moveKing":
							retorno = self.movimiento(__jugador, __d, matrizTablero, "moveKing", __movimiento, 1)
						else:
							if __nombreMetodo == "moveQueen":
								retorno = self.movimiento(__jugador, __d, matrizTablero, "moveQueen", __movimiento, 1)

		return retorno

	@classmethod
	def mostrar(self, matrizTablero):
		retorno = "=======================\n"

		for i in range(8):
			for j in range(8):
				__elementoAux = matrizTablero[i][j]
				retorno += str(__elementoAux) + "-"
			retorno += "\n"
		return retorno

	@classmethod
	def piezaEnDestino(self, __d, matrizTablero):
		retorno = False

		if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c":
			#print("...")
			retorno = True

		return retorno

	@classmethod
	def piezaEnIntervalo(self, __d, __sd, matrizTablero, __nombreMetodo, overridePieza):
		retorno = False
		
		#print(str(overridePieza))
		print("En piezaEnIntervalo: __sd = " + __sd + "\npiezaEnDestino retorna: " + str(self.piezaEnDestino(__d, matrizTablero)))
		#if (not overridePieza and (not self.piezaEnDestino(__d, matrizTablero))):
		#if True:
		if len(__sd) <= 2 and (__nombreMetodo == "moverTorre" or __nombreMetodo == "moveQueen"):
			if __sd[0] == "B":
				print("__sd = " + __sd + " hasta --> " + str(int(__d[0])))
				for j in range((int(__sd[1]) + overridePieza), int(__d[0])):
					
					if not overridePieza and self.piezaEnDestino(__d, matrizTablero):
						retorno = True
						break

					print("overridePieza = " + str(overridePieza))
					print("En " + str(j) + __d[1])
					print("Tipo: " + matrizTablero[j][int(__d[1])].tipo)
					if j != int(__sd[1]) and matrizTablero[j][int(__d[1])].tipo != "c":
						retorno = True
						break
			else:
				if __sd[0] == "S":
					for j in range((int(__d[0]) + overridePieza), int(__sd[1])):
						#print("Revisando: " + str(j) + __d[1])
						#print(self.mostrar(matrizTablero))
						#input()

						if matrizTablero[j][int(__d[1])].tipo != "c":
							retorno = True
							break
				else:
					if __sd[0] == "I":
						for j in range((int(__d[1]) + overridePieza), int(__sd[1])):
							#print("Revisando: " + str(j) + __d[1])
							if matrizTablero[int(__d[0])][j].tipo != "c":
								retorno = True
								break
					else:
						if __sd[0] == "D":
							for j in range((int(__sd[1]) + overridePieza), (int(__d[1]) + 1)):
								#print("Revisando: " + __d[0] + str(j))
								if j != int(__sd[1]) and matrizTablero[int(__d[0])][j].tipo != "c":
									retorno = True
									break
			#else:
		#print("Line 179.\nretorno = " + str(retorno))
		if __nombreMetodo == "moverAlfil" or __nombreMetodo == "moveQueen":
			#print("En piezaEnIntervalo: __sd = " + __sd)
			try:
				if __sd[0] == "B":
					r = int(__sd[3]) # r = derecha
					l = int(__sd[3]) # l = izquierda
					
					for i in range((int(__sd[2]) + overridePieza), int(__d[0])):
					
						if not overridePieza and self.piezaEnDestino(__d, matrizTablero):
							retorno = True
							break
					
						#print("overridePieza = " + str(overridePieza))
						if i != int(__sd[2]):
							if l < 7:
								l += 1
							if r >= 0:
								r -= 1
						if __sd[1] == "I":
							#matrizTablero[i][r] = King()
							#print("En " + str(i) + str(l))
							#print("tipo: " + matrizTablero[i][l].tipo)
							if i != int(__sd[2]) and matrizTablero[i][l].tipo != "c":
								#print("Hay un " + matrizTablero[i][l].tipo)
								#matrizTablero[i][r] = King()
								retorno = True
							#retorno = "SD" + str(i) + str(r)
						else:
							print("En " + str(i) + str(r))
							print("Tipo: " + matrizTablero[i][r].tipo)
							if i != int(__sd[2]) and matrizTablero[i][r].tipo != "c":
								print("Hay un " + matrizTablero[i][r].tipo)
								#print("...")
								retorno = True
								#if overridePieza:
				else:
					r = int(__d[1]) # r = derecha
					l = int(__d[1]) # l = izquierda
					
					# Fuera de rango en ocasiones.
					for i in range((int(__d[0]) + overridePieza), int(__sd[2])):
						#print("En " + str(i) + str(r))
						#print("tipo: " + matrizTablero[i][r].tipo)
						if i != int(__d[0]):
								r += 1
								l -= 1
						if __sd[1] == "I":
							if l >= 0:
								print("SI --> " + str(i) + str(l))
								if matrizTablero[i][l].tipo != "c":
									retorno = True
						else:
							#print("...")
							#matrizTablero[i][r] = Torre()
							if r <= 7:
								if matrizTablero[i][r].tipo != "c":
									retorno = True
			except:
				print("Line 238.\nSurgió un error.")

			

		#else:
			#print("...")
			#retorno = self.piezaEnDestino(__d, matrizTablero)
		print("Line 245.\nretorno = " + str(retorno))
		return retorno
	
	@classmethod
	def accesibleForTheKing(self, __d, __jugador, matrizTablero):
		retorno = False
		print("Método: accesibleForTheKing")
		#[(int(__d[0]) - 1)][(int(__d[1]) - 1)] [(int(__d[0]) - 1)][int(__d[1])] [(int(__d[0]) - 1)][(int(__d[1]) + 1)]
		#   [int(__d[0])][(int(__d[1]) - 1)]                 (__d)                  [int(__d[0])][(int(__d[1]) + 1)]
		#[(int(__d[0]) + 1)][(int(__d[1]) - 1)] [(int(__d[0]) + 1)][int(__d[1])] [(int(__d[0]) + 1)][(int(__d[1]) + 1)]

		#matrizTablero[(int(__d[0]) + 1)][int(__d[1])] = Torre()

		if ((int(__d[1]) - 1) >= 0):
			if (matrizTablero[int(__d[0])][(int(__d[1]) - 1)].tipo == "K" and matrizTablero[int(__d[0])][(int(__d[1]) - 1)].color == __jugador):
				retorno = __d[0] + str((int(__d[1]) - 1))

			if ((int(__d[1]) + 1) <= 7):
				if (matrizTablero[int(__d[0])][(int(__d[1]) + 1)].tipo == "K" and matrizTablero[int(__d[0])][(int(__d[1]) + 1)].color == __jugador):
					retorno = __d[0] + str((int(__d[1]) + 1))

			if ((int(__d[0]) - 1) >= 0):
				if (matrizTablero[(int(__d[0]) - 1)][int(__d[1])].tipo == "K" and matrizTablero[(int(__d[0]) - 1)][int(__d[1])].color == __jugador):
					retorno = str((int(__d[0]) - 1)) + __d[1]

			if ((int(__d[0]) + 1) <= 7):
				if (matrizTablero[(int(__d[0]) + 1)][int(__d[1])].tipo == "K" and matrizTablero[(int(__d[0]) + 1)][int(__d[1])].color == __jugador):
					retorno = str((int(__d[0]) + 1)) + __d[1]

			if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) - 1) >= 0):
				if (matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 1)].tipo == "K" and matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 1)].color == __jugador):
					retorno = str((int(__d[0]) + 1)) + str((int(__d[1]) - 1))

			if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) + 1) <= 7):
				if (matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 1)].tipo == "K" and matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 1)].color == __jugador):
					retorno = str((int(__d[0]) - 1)) + str((int(__d[1]) + 1))

			if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) + 1) <= 7):
				if (matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 1)].tipo == "K" and matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 1)].color == __jugador):
					retorno = str((int(__d[0]) + 1)) + str((int(__d[1]) + 1))

			if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) - 1) >= 0):
				if (matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 1)].tipo == "K" and matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 1)].color == __jugador):
					retorno = str((int(__d[0]) - 1)) + str((int(__d[1]) - 1))

		return retorno
	
	@classmethod
	def accesibleParaCaballo(self, __d, __jugador, matrizTablero):
		retorno = False

		#print("Revisando en: " + str((int(__d[0]) + 2)) + str((int(__d[1]) + 1)) + "\nTipo: " + matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) + 1)].tipo)
		#print("Revisando en: " + str((int(__d[0]) + 2)) + str((int(__d[1]) - 1)) + "\nTipo: " + matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) - 1)].tipo)
		#print("Revisando en: " + str((int(__d[0]) - 2)) + str((int(__d[1]) + 1)) + "\nTipo: " + matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) + 1)].tipo)
		#print("Revisando en: " + str((int(__d[0]) - 2)) + str((int(__d[1]) - 1)) + "\nTipo: " + matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)].tipo)
		#print("Revisando en: " + str((int(__d[0]) + 1)) + str((int(__d[1]) + 2)) + "\nTipo: " + matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 2)].tipo)
		#print("Revisando en: " + str((int(__d[0]) + 1)) + str((int(__d[1]) - 2)) + "\nTipo: " + matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 2)].tipo)
		#print("Revisando en: " + str((int(__d[0]) - 1)) + str((int(__d[1]) + 2)) + "\nTipo: " + matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 2)].tipo)
		#print("Revisando en: " + str((int(__d[0]) - 1)) + str((int(__d[1]) - 2)) + "\nTipo: " + matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 2)].tipo)

		#matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) - 1)] = Queen()
		#matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)] = Queen()
		#matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 2)] = Queen()
		#matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 2)] = Queen()

		if ((int(__d[0]) + 2) <= 7 and (int(__d[1]) + 1) <= 7):
			if (matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) + 1)].tipo == "N" and matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) + 1)].color == __jugador):
				retorno = str((int(__d[0]) + 2)) + str((int(__d[1]) + 1))
		#else:
			#print("Revisando en: " + str((int(__d[0]) + 2)) + str((int(__d[1]) - 1)))
		if ((int(__d[0]) + 2) <= 7 and (int(__d[1]) - 1) >= 0):
			if (matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) - 1)].tipo == "N" and matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) - 1)].color == __jugador):
				retorno = str((int(__d[0]) + 2)) + str((int(__d[1]) - 1))
		#else:
			#print("Revisando en: " + str((int(__d[0]) - 2)) + str((int(__d[1]) + 1)))
		if ((int(__d[0]) - 2) >= 0 and (int(__d[1]) + 1) <= 7):
			if (matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) + 1)].tipo == "N" and matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) + 1)].color == __jugador):
				retorno = str((int(__d[0]) - 2)) + str((int(__d[1]) + 1))
		#else:
			#print("Revisando en: " + str((int(__d[0]) - 2)) + str((int(__d[1]) - 1)))
			#print("Line 333.\nTipo = " + matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)].tipo)
		if ((int(__d[0]) - 2) >= 0 and (int(__d[1]) - 1) >= 0):
			if (matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)].tipo == "N" and matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)].color == __jugador):
				retorno = str((int(__d[0]) - 2)) + str((int(__d[1]) - 1))
		#else:
			#print("Revisando en: " + str((int(__d[0]) + 1)) + str((int(__d[1]) + 2)))
		if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) + 2) <= 7):
			if (matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 2)].tipo == "N" and matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 2)].color == __jugador):
				retorno = str((int(__d[0]) + 1)) + str((int(__d[1]) + 2))
		#else:
			#print("Revisando en: " + str((int(__d[0]) + 1)) + str((int(__d[1]) - 2)))
		if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) - 2) >= 0):
			if (matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 2)].tipo == "N" and matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 2)].color == __jugador):
				retorno = str((int(__d[0]) + 1)) + str((int(__d[1]) - 2))
		#else:
		if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) + 2) <= 7):
			if (matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 2)].tipo == "N" and matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 2)].color == __jugador):
				retorno = str((int(__d[0]) - 1)) + str((int(__d[1]) + 2))
		#else:
			#print("Revisando en: " + str((int(__d[0]) - 1)) + str((int(__d[1]) - 2)))
		if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) - 2) >= 0):
			if (matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 2)].tipo == "N" and matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 2)].color == __jugador):
					retorno = str((int(__d[0]) - 1)) + str((int(__d[1]) - 2))
		return retorno

	@classmethod
	def sentidoDireccion(self, __movimiento, __jugador, matrizTablero, __d):
		# S, B, I, D
		retorno = False

		# Ver que pasa si por ejemplo 2 Torres están en la misma fila o columna y una puede moverse a un punto determinado y otra no puede.
		# Podría concatenar las ubicaciones de las piezas similares (D3 I7)

		__p = self.identificarPieza(__movimiento, __jugador, matrizTablero)

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
					if matrizTablero[i][r].tipo == __p and matrizTablero[i][r].color == __jugador:
						retorno = "SD" + str(i) + str(r)
				if l >= 0:
					if matrizTablero[i][l].tipo == __p and matrizTablero[i][l].color == __jugador:
						retorno = "SI" + str(i) + str(l)
			
			r = int(__d[1]) # r = derecha
			l = int(__d[1]) # l = izquierda
			#matrizTablero[int(__d[0])][int(__d[1])] = King()
			#print("D: " + __d)
			i = int(__d[0])
			while i >= 0:
				if i != int(__d[0]):
					r += 1
					l -= 1
				#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
				#matrizTablero[i][r] = King()
				#matrizTablero[i][l] = Caballo()
				#print("Tipo: " + matrizTablero[i][r].tipo)
				if r <= 7:
					if matrizTablero[i][r].tipo == __p and matrizTablero[i][r].color == __jugador:
						retorno = "BD" + str(i) + str(r)
				if l >= 0:
					if matrizTablero[i][l].tipo == __p and matrizTablero[i][l].color == __jugador:
						retorno = "BI" + str(i) + str(l)

				i -= 1
			#self.mostrar(matrizTablero)
			#input()
		else:
			if __p == "R":
				#print("retorno = " + str(retorno))
				for i in range(int(__d[0]), 8):
					if matrizTablero[i][int(__d[1])].tipo == __p and matrizTablero[i][int(__d[1])].color == __jugador:
						retorno = "S" + str(i)
				if not retorno:
					i = int(__d[0])
					while i >= 0:
						if matrizTablero[i][int(__d[1])].tipo == __p and matrizTablero[i][int(__d[1])].color == __jugador:
							retorno = "B" + str(i)
						i -= 1
					if not retorno:
						i = int(__d[1])
						while i >= 0:
							if matrizTablero[int(__d[0])][i].tipo == __p and matrizTablero[int(__d[0])][i].color == __jugador:
								retorno = "D" + str(i)
								#print("...")
							i -= 1
						if not retorno:
							for i in range(int(__d[1]), 8):
								if matrizTablero[int(__d[0])][i].tipo == __p and matrizTablero[int(__d[0])][i].color == __jugador:
									retorno = "I" + str(i)
									#print("...")
			else:
				if __p == "Q":
					#print("Line 405.\nretorno = " + str(retorno))
					for i in range(int(__d[0]), 8):
						if matrizTablero[i][int(__d[1])].tipo == __p and matrizTablero[i][int(__d[1])].color == __jugador:
							retorno = "S" + str(i)
					if not retorno:
						i = int(__d[0])
						while i >= 0:
							if matrizTablero[i][int(__d[1])].tipo == __p and matrizTablero[i][int(__d[1])].color == __jugador:
								retorno = "B" + str(i)
							i -= 1
						if not retorno:
							i = int(__d[1])
							while i >= 0:
								if matrizTablero[int(__d[0])][i].tipo == __p and matrizTablero[int(__d[0])][i].color == __jugador:
									retorno = "D" + str(i)

									#if __movimiento == "Qf1":
										#print("Line 422.\nTipo = " + matrizTablero[int(__d[0])][i].tipo + " en " + __d[0] + str(i))
									#print("...")
									#matrizTablero[int(__d[0])][i] = Caballo()
								i -= 1
							if not retorno:
								for i in range(int(__d[1]), 8):
									if matrizTablero[int(__d[0])][i].tipo == __p and matrizTablero[int(__d[0])][i].color == __jugador:
										retorno = "I" + str(i)
										#print("...")
					print("Line 427.\nretorno = " + str(retorno))
					if not retorno:
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
								if matrizTablero[i][r].tipo == __p and matrizTablero[i][r].color == __jugador:
									retorno = "SD" + str(i) + str(r)
							if l >= 0:
								if matrizTablero[i][l].tipo == __p and matrizTablero[i][l].color == __jugador:
									retorno = "SI" + str(i) + str(l)
						
						r = int(__d[1]) # r = derecha
						l = int(__d[1]) # l = izquierda
						#matrizTablero[int(__d[0])][int(__d[1])] = King()
						#print("D: " + __d)
						i = int(__d[0])
						while i >= 0:
							if i != int(__d[0]):
								r += 1
								l -= 1
							#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
							#matrizTablero[i][r] = King()
							#matrizTablero[i][l] = Caballo()
							#print("Tipo: " + matrizTablero[i][r].tipo)
							if r <= 7:
								if matrizTablero[i][r].tipo == __p and matrizTablero[i][r].color == __jugador:
									retorno = "BD" + str(i) + str(r)
							if l >= 0:
								if matrizTablero[i][l].tipo == __p and matrizTablero[i][l].color == __jugador:
									retorno = "BI" + str(i) + str(l)

							i -= 1
					print("Line 467.\nretorno = " + str(retorno))
		return retorno

	@classmethod
	def movimiento(self, __jugador, __d, matrizTablero, __nombreMetodo, __movimiento, overridePieza):
		retorno = False

		if __nombreMetodo == "moverPeon":
			if __jugador == "w":
				print("El jugador es: " + __jugador)
				for i in range(8):
					if i >= int(__d[0]) and i <= 7:
						#print("Revisando en: " + str(i) + __d[1])
						if matrizTablero[i][int(__d[1])].tipo == "P" and matrizTablero[i][int(__d[1])].color == "w":
							print("Se encontró un Pb en:" + str(i) + __d[1])
							if (int(__d[0]) == (i-1)) or (int(__d[0]) == (i-2) and i == 6): # Movimiento simple o doble.
								print("Es un movimiento simple o doble de un peón.")
								print("El destino es: " + __d)
								retorno = str(i) + __d[1] + " " + __d
								break
						else:
							if matrizTablero[i][int(__d[1])].tipo != "c":
								break
			else:
				i = int(__d[0])
				while i >= 0:
					if matrizTablero[i][int(__d[1])].tipo == "P" and matrizTablero[i][int(__d[1])].color == "b":
						if (int(__d[0]) == (i+1)) or (int(__d[0]) == (i+2) and i == 1): # Movimiento simple de a un casillero.
								retorno = str(i) + __d[1] + " " + __d
						break
					else:
						if matrizTablero[i][int(__d[1])].tipo != "c": #Hay una pieza en el camino, el peón no puede saltarla.
							break
					i -= 1
		else:
			if __nombreMetodo == "moverTorre":
				__sd = self.sentidoDireccion(__movimiento, __jugador, matrizTablero, __d)
				if type(__sd) != type(bool()):
					print("El sentidoDireccion retornó: " + __sd)
					if not self.piezaEnIntervalo(__d, __sd, matrizTablero, __nombreMetodo, overridePieza):
						if __sd[0] == "S" or __sd[0] == "B":
							retorno = __sd[1] + __d[1] + " " + __d
						else:
							if __sd[0] == "I" or __sd[0] == "D":
								retorno = __d[0] + __sd[1] + " " + __d
			else:
				if __nombreMetodo == "moverCaballo":
					__o = self.accesibleParaCaballo(__d, __jugador, matrizTablero)
					print("Line 534.\n __o == " + str(__o))
					if type(__o) != type(bool()):
						if not overridePieza:
							if not self.piezaEnDestino(__d, matrizTablero):
								retorno = __o + " " + __d
						else:
							#print("...")
							retorno = __o + " " + __d
				else:
					if __nombreMetodo == "moverAlfil":
						print("__nombreMetodo = " + __nombreMetodo)
						__sd = self.sentidoDireccion(__movimiento, __jugador, matrizTablero, __d)
						if type(__sd) != type(bool()):
							print("El sentidoDireccion retornó: " + __sd)
							if not self.piezaEnIntervalo(__d, __sd, matrizTablero, __nombreMetodo, overridePieza):
								#print("Line 464.")
								retorno = __sd[2] + __sd[3] + " " + __d
							else:
								0
					else:
						if __nombreMetodo == "moveKing":
							__o = self.accesibleForTheKing(__d, __jugador, matrizTablero)
							print("accesibleForTheKing retornó: " + str(__o))
							if type(__o) != type(bool()):
								print("overridePieza = " + str(overridePieza))
								if not overridePieza:
									if not self.piezaEnDestino(__d, matrizTablero):
										retorno = __o + " " + __d
								else:
									if self.piezaEnDestino(__d, matrizTablero):
										retorno = __o + " " + __d
						else:
							if __nombreMetodo == "moveQueen":
								__sd = self.sentidoDireccion(__movimiento, __jugador, matrizTablero, __d)
								print("El sentidoDireccion retornó: " + str(__sd))
								#input()
								if (type(__sd) != type(bool())):
									print("Line 554.")
									if len(__sd) == 2:
										#print("El sentidoDireccion retornó: " + __sd)
										if not self.piezaEnIntervalo(__d, __sd, matrizTablero, __nombreMetodo, overridePieza):
											print("No hay pieza en intervalo.")
											if __sd[0] == "S" or __sd[0] == "B":
												retorno = __sd[1] + __d[1] + " " + __d
											else:
												if __sd[0] == "I" or __sd[0] == "D":
													retorno = __d[0] + __sd[1] + " " + __d
										else:
											print("Hay pieza en intervalo.")
									else:
										if not retorno:
											print("No mueve como torre.")
											#__sd = self.sentidoDireccion(__movimiento, __jugador, matrizTablero, __d)
											if type(__sd) != type(bool()):
												print("Line 561.\nEl sentidoDireccion retornó: " + __sd)
												if not self.piezaEnIntervalo(__d, __sd, matrizTablero, __nombreMetodo, overridePieza):
													#print("Line 464.")
													retorno = __sd[2] + __sd[3] + " " + __d
										else:
											print("Mueve como torre.")
		return retorno

	@classmethod
	def moverPeon(self, __movimiento, __jugador, matrizTablero):
		retorno = False

		print("Line 641.\n__jugador == " + str(__jugador))

		matrizInicialesPiezas = ["R", "N", "B", "K", "Q"]
		
		__d = self.obtenerFilaColumna(__movimiento, "moverPeon")
		print("El obtenerFilaColumna retornó: " + __d)
		
		if self.esCaptura(__movimiento, "moverPeon"):
			if bool(__d):
				if self.esCapturable(__jugador, __d, matrizTablero):
					retorno = self.capturar(__movimiento, __jugador, __d, matrizTablero, "moverPeon")
		else:
			retorno = self.movimiento(__jugador, __d, matrizTablero, "moverPeon", __movimiento, 0)
			print("El movimiento retornó: " + str(retorno))

		if retorno: # Este bloque realiza la promoción del Peon.
			if self.esCaptura(__movimiento, "moverPeon"):
				print("Line 647.")
				if len(__movimiento) == 5: # La longitud requerida para que sea una promoción.
					if __movimiento[4] in matrizInicialesPiezas:
						matrizTablero[int(retorno[0])][int(retorno[1])].tipo = __movimiento[4]
						#print("El tipo es: " + matrizTablero[int(retorno[0])][int(retorno[1])].tipo)
				else:
					if len(__movimiento) == 4 and ((__movimiento[3] == "8" and __jugador == "w") or (__movimiento[3] == "1" and __jugador == "b")):
							retorno = False
			else:
				if len(__movimiento) == 4 and __movimiento[3] in matrizInicialesPiezas:
					matrizTablero[int(retorno[0])][int(retorno[1])].tipo = __movimiento[3]
				else:
					if len(__movimiento) == 2 and ((__movimiento[1] == "8" and __jugador == "w") or (__movimiento[1] == "1" and __jugador == "b")):
							retorno = False
		else: # Este bloque realiza la captura al paso.
			if self.esCaptura(__movimiento, "moverPeon"):
				if len(__movimiento) == 8: # La longitud requerida para que sea una captura al paso.
					if __movimiento[4] == 'a' and __movimiento[5] == '.' and __movimiento[6] == 'p' and __movimiento[7] == '.':
						print("Line 665.\nes captura al paso...")
						c = self.__matrizColumnas.index(__movimiento[0])
						print("La columna de origen es: " + str(c))
						if __jugador == "w":
							if (int(__d[0]) + 1) < 8:
								print("Revisando en: " + str(int(__d[0]) + 1) + str(c))
								if matrizTablero[int(__d[0]) + 1][c].tipo == "P" and matrizTablero[int(__d[0]) + 1][c].color == "w":
									if matrizTablero[int(__d[0]) + 1][int(__d[1])].tipo == "P" and matrizTablero[int(__d[0]) + 1][int(__d[1])].color == "b":
										if matrizTablero[int(__d[0]) + 1][int(__d[1])].ultimateMovementWas(self,"double_movement"):
											matrizTablero[int(__d[0]) + 1][int(__d[1])] = Casillero()
											retorno = str(int(__d[0]) + 1) + str(c) + " " + __d
						else:
							if (int(__d[0]) - 1) > -1:
								print("Revisando en: " + str(int(__d[0]) - 1) + str(c))
								if matrizTablero[int(__d[0]) - 1][c].tipo == "P" and matrizTablero[int(__d[0]) - 1][c].color == "b":
									if matrizTablero[int(__d[0]) - 1][int(__d[1])].tipo == "P" and matrizTablero[int(__d[0]) - 1][int(__d[1])].color == "w":
										# En cuanto esté solucionado el problema del historial, debería verificar.
										if matrizTablero[int(__d[0]) - 1][int(__d[1])].ultimateMovementWas(self, "double_movement"):
											matrizTablero[int(__d[0]) - 1][int(__d[1])] = Casillero()
											retorno = str(int(__d[0]) - 1) + str(c) + " " + __d

						

		return retorno

	@classmethod
	def moverAlfil(self, __movimiento, __jugador, matrizTablero):
		print("En moverAlfil.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moverAlfil")
		print("El obtenerFilaColumna retornó: " + str(__d))

		if self.esCaptura(__movimiento, "moverAlfil"):
			if bool(__d):
				if self.esCapturable(__jugador, __d, matrizTablero):
					#print("...")
					retorno = self.capturar(
						__movimiento, __jugador, 
						__d, matrizTablero, "moverAlfil"
					)
		else:
			print("En moverAlfil. esCaptura == False.")
			
			retorno = self.movimiento(
				__jugador, __d, matrizTablero, "moverAlfil", __movimiento, 0
				)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (
				retorno[0] + retorno[1] == retorno[3] + retorno[4]):
			retorno = False

		return retorno

	@classmethod
	def moverTorre(self, __movimiento, __jugador, matrizTablero):
		print("En moverTorre.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moverTorre")
		print("El obtenerFilaColumna retornó: " + str(__d))
		
		if self.esCaptura(__movimiento, "moverTorre"):
			if bool(__d):
				if self.esCapturable(__jugador, __d, matrizTablero):
					retorno = self.capturar(
						__movimiento, __jugador, 
						__d, matrizTablero, "moverTorre"
					)
		else:
			print("En moverTorre. esCaptura == False.")
			
			retorno = self.movimiento(
				__jugador, __d, matrizTablero, "moverTorre", __movimiento, 0
				)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (
				retorno[0] + retorno[1] == retorno[3] + retorno[4]):
			retorno = False
		return retorno

	@classmethod
	def moveQueen(self, __movimiento, __jugador, matrizTablero):
		print("En moveQueen.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moveQueen")
		print("El obtenerFilaColumna retornó: " + str(__d))

		#f = self.find("Q", __jugador)

		#matrizTablero[int(f[0])][int(f[1])].tipo = "A"

		if self.esCaptura(__movimiento, "moveQueen"):
			if self.esCapturable(__jugador, __d, matrizTablero):
				print("Line 655.\nLa pieza es capturable.")
				retorno = self.capturar(
					__movimiento, __jugador, __d, matrizTablero, "moveQueen"
					)
		else:
			print("En moveQueen. esCaptura == False.")
			
			retorno = self.movimiento(
				__jugador, __d, matrizTablero, "moveQueen", __movimiento, 0
				)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (
				retorno[0] + retorno[1] == retorno[3] + retorno[4]): # Revisa que no sea el mismo lugar donde está.
			retorno = False

		return retorno

	@classmethod
	def moveKing(self, __movimiento, __jugador, matrizTablero):
		print("En moveKing.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moveKing")
		print("El obtenerFilaColumna retornó: " + str(__d))

		if self.esCaptura(__movimiento, "moveKing"):
			if self.esCapturable(__jugador, __d, matrizTablero):
				retorno = self.capturar(
					__movimiento, __jugador, __d, matrizTablero, "moveKing"
					)
		else:
			print("En moveKing. esCaptura == False.")
			
			retorno = self.movimiento(
				__jugador, __d, matrizTablero, "moveKing", __movimiento, 0
				)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (
				retorno[0] + retorno[1] == retorno[3] + retorno[4]): # Revisa que no sea el mismo lugar donde está.
			retorno = False

		return retorno

	@classmethod
	def moverCaballo(self, __movimiento, __jugador, matrizTablero):
		print("En moverCaballo.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moverCaballo")
		print("El obtenerFilaColumna retornó: " + str(__d))

		if self.esCaptura(__movimiento, "moverCaballo"):
			if self.esCapturable(__jugador, __d, matrizTablero):
				retorno = self.capturar(__movimiento, __jugador, __d, matrizTablero, "moverCaballo")
		else:
			print("En moverCaballo. esCaptura == False.")
			
			retorno = self.movimiento(
				__jugador, __d, matrizTablero, "moverCaballo", __movimiento, 0
				)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (
				retorno[0] + retorno[1] == retorno[3] + retorno[4]): # Revisa que no sea el mismo lugar donde está.
			retorno = False

		return retorno

	@classmethod
	def castling(self, __movimiento, __jugador, matrizTablero): # enroque.
		retorno = False

		if __jugador == "w":
			if len(__movimiento) == 3: # 0-0
				if (
						matrizTablero[7][7].tipo == "R" and matrizTablero[7][7].color == __jugador and matrizTablero[7][6].tipo == "c" and matrizTablero[7][5].tipo == "c" and matrizTablero[7][4].tipo == "K" and matrizTablero[7][4].color == __jugador):
					retorno = "00 00" # Este retorno se hace para que en tablero.moverOD no haga cambios.

					matrizTablero[7][5] = matrizTablero[7][7]
					matrizTablero[7][7] = Casillero()

					matrizTablero[7][6] = matrizTablero[7][4]
					matrizTablero[7][4] = Casillero()
			else:
				if len(__movimiento) == 5: # 0-0-0
					if (
							matrizTablero[7][0].tipo == "R" and matrizTablero[7][0].color == __jugador and matrizTablero[7][1].tipo == "c" and matrizTablero[7][2].tipo == "c" and matrizTablero[7][3].tipo == "Q" and matrizTablero[7][3].color == __jugador):
						retorno = "00 00" # Este retorno se hace para que en tablero.moverOD no haga cambios.

						matrizTablero[7][2] = matrizTablero[7][3]
						matrizTablero[7][3] = Casillero()

						matrizTablero[7][3] = matrizTablero[7][0]
						matrizTablero[7][0] = Casillero()
		else:
			if len(__movimiento) == 3: # 0-0
				if (
						matrizTablero[0][7].tipo == "R" and matrizTablero[0][7].color == __jugador and matrizTablero[0][6].tipo == "c" and matrizTablero[0][5].tipo == "c" and matrizTablero[0][4].tipo == "K" and matrizTablero[0][4].color == __jugador):
					retorno = "00 00" # Este retorno se hace para que en tablero.moverOD no haga cambios.

					matrizTablero[0][5] = matrizTablero[0][7]
					matrizTablero[0][7] = Casillero()

					matrizTablero[0][6] = matrizTablero[0][4]
					matrizTablero[0][4] = Casillero()
			else:
				if len(__movimiento) == 5: # 0-0-0
					if (
							matrizTablero[0][0].tipo == "R" and matrizTablero[0][0].color == __jugador and matrizTablero[0][1].tipo == "c" and matrizTablero[0][2].tipo == "c" and matrizTablero[0][3].tipo == "Q" and matrizTablero[0][3].color == __jugador):
						
						retorno = "00 00" # Este retorno se hace para que en tablero.moverOD no haga cambios.

						matrizTablero[0][2] = matrizTablero[0][3]
						matrizTablero[0][3] = Casillero()

						matrizTablero[0][3] = matrizTablero[0][0]
						matrizTablero[0][0] = Casillero()

		if retorno:
			self.cambiarTurno(__jugador)
		return retorno

	@classmethod
	def verificarTurno(self, jugador):
		retorno = False
		if jugador == self.turno:
			retorno = True
		return retorno

	@classmethod
	def cambiarTurno(self, __jugador):
		if __jugador == "w":
			self.turno = "b"
		else:
			self.turno = "w"

	@classmethod
	def identificarPieza(self, __movimiento, __jugador, matrizTablero):
		retorno = "P"

		__matrizInicialesPiezas = ["R", "N", "B", "K", "Q"]
		if __movimiento[0] in __matrizInicialesPiezas:
			if __movimiento[0] == "R":
					retorno = "R"
			else:
				if __movimiento[0] == "N":
					retorno = "N"
				else:
					if __movimiento[0] == "B":
						retorno = "B"
					else:
						if __movimiento[0] == "K":
							retorno = "K"
						else:
							if __movimiento[0] == "Q":
								retorno = "Q"
		return retorno

	@classmethod
	def identificarMoverPieza(self, movimiento, jugador, matrizTablero):
		retorno = False

		__matrizInicialesPiezas = ["R", "N", "B", "K", "Q"]
		if movimiento[0] in __matrizInicialesPiezas:
			if movimiento[0] == "R":
				retorno = self.moverTorre(
					movimiento, jugador, matrizTablero
					)
			else:
				if movimiento[0] == "N":
					retorno = self.moverCaballo(
						movimiento, jugador, matrizTablero
						)
				else:
					if movimiento[0] == "B":
						retorno = self.moverAlfil(
							movimiento, jugador, matrizTablero
							)
					else:
						if movimiento[0] == "K":
							retorno = self.moveKing(
								movimiento, jugador, matrizTablero
								)
						else:
							if movimiento[0] == "Q":
								retorno = self.moveQueen(
									movimiento, jugador, matrizTablero
									)
		else:
			print("Line 919.")
			if movimiento == "0-0" or movimiento == "0-0-0":
				retorno = self.castling(movimiento, jugador, matrizTablero)
			else:
				print("Line 923.")
				retorno = self.moverPeon(movimiento, jugador, matrizTablero)
				print("El moverPeon retornó: " + str(retorno))

		return retorno

	@classmethod
	def verificarSintaxis(self, m, p):
		# p = player, m = movimiento.
		retorno = True

		#if len(m) == 3: # Corresponde a la captura de un peon o a ...
			#if m[0] == "x": # Corresponde a la captura de un peon.

			#if m[0] in self.__matrizColumnas: # Es una columna válida.
		return retorno

	@classmethod
	def mover(self, movimiento, turno, matrizTablero):
		retorno = False
		
		#self.turno = turno
		
		#if self.verificarSintaxis(__movimiento, jugador):

		retorno = self.identificarMoverPieza(movimiento, turno, matrizTablero)
		print("El identificarMoverPieza retornó: " + str(retorno))
		if retorno:
			self.addToHistory(movimiento, self.turno, retorno)
			self.cambiarTurno(turno)
			# Historial de movimientos.
				
		return retorno

	def __init__(self):
		self.__turno = 'w'