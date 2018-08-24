import random
from clases.piezas.peon import Peon
from clases.piezas.king import King
from clases.piezas.queen import Queen
from clases.piezas.alfil import Alfil
from clases.piezas.caballo import Caballo
from clases.piezas.torre import Torre
from clases.casillero import Casillero

class Reglamento:
	__matrizColumnas = ["a", "b", "c", "d", "e", "f", "g", "h"]
	__matrizFilas = [8, 7, 6, 5, 4, 3, 2, 1]
	
	@property
	def turno(self):
		return self.__turno
	@turno.setter
	def turno(self, value):
		self.__turno = value

	@classmethod
	def esCaptura(self, __movimiento, __nombreMetodo):
		retorno = False
		if __nombreMetodo == "moverPeon" and __movimiento[0] == "x":
			retorno = True
		else:
			if (__nombreMetodo == "moverTorre" or __nombreMetodo == "moverCaballo" or __nombreMetodo == "moverAlfil" or __nombreMetodo == "moverKing") and __movimiento[1] == "x":
				retorno = True
		return retorno

	@classmethod
	def verificarFilaColumna(self, __movimiento, __nombreMetodo):
		retorno = False

		if __nombreMetodo == "moverPeon":
			if self.esCaptura(__movimiento, __nombreMetodo):
				if __movimiento[1] in self.__matrizColumnas and int(__movimiento[2]) >= 1 and int(__movimiento[2]) <= 8:
					retorno = "12"
			else:
				if __movimiento[0] in self.__matrizColumnas and int(__movimiento[1]) >= 1 and int(__movimiento[1]) <= 8:
					retorno = "01"
		else:
			if __nombreMetodo == "moverTorre" or __nombreMetodo == "moverCaballo" or __nombreMetodo == "moverAlfil" or __nombreMetodo == "moverKing":
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
		return __d

	@classmethod
	def esCapturable(self, __movimiento, __jugador, __d, matrizTablero):
		retorno = False
		if __jugador == "b":
			if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c" and matrizTablero[int(__d[0])][int(__d[1])].color == "n":
				retorno = True
		else:
			if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c" and matrizTablero[int(__d[0])][int(__d[1])].color == "b":		
				retorno = True
		return retorno

	@classmethod
	def capturarConPeon(self, __movimiento, __jugador, __d, matrizTablero):
		retorno = False
		
		if __jugador == "b":
			if (int(__d[1]) - 1) > -1 and (int(__d[0]) + 1) < 8:
				if matrizTablero[int(__d[0]) + 1][int(__d[1]) - 1].tipo == "P" and matrizTablero[int(__d[0]) + 1][int(__d[1]) - 1].color == "b":
					retorno = str(int(__d[0]) + 1) + str(int(__d[1]) - 1) + " " + __d
				else:
					if (int(__d[1]) + 1) < 8 and (int(__d[0]) + 1) < 8:
						if matrizTablero[int(__d[0]) + 1][int(__d[1]) + 1].tipo == "P" and matrizTablero[int(__d[0]) + 1][int(__d[1]) + 1].color == "b":
							retorno = str(int(__d[0]) + 1) + str(int(__d[1]) + 1) + " " + __d				
		else:
			if matrizTablero[int(__d[0])][int(__d[1])].tipo != "c" and matrizTablero[int(__d[0])][int(__d[1])].color == "b":
				if (int(__d[0]) - 1) > -1 and (int(__d[1]) + 1) < 8:
					if matrizTablero[int(__d[0]) - 1][int(__d[1]) + 1].tipo == "P" and matrizTablero[int(__d[0]) - 1][int(__d[1]) + 1].color == "n":
							retorno = str(int(__d[0]) - 1) + str(int(__d[1]) + 1) + " " + __d
					else:
						if (int(__d[1]) - 1) != -1 and (int(__d[0]) - 1) != -1:
							if matrizTablero[int(__d[0]) - 1][int(__d[1]) - 1].tipo == "P" and matrizTablero[int(__d[0]) - 1][int(__d[1]) - 1].color == "n":
								retorno = str(int(__d[0]) - 1) + str(int(__d[1]) - 1) + " " + __d

		return retorno

	@classmethod
	def capturar(self, __movimiento, __jugador, __d, matrizTablero, __nombreMetodo):
		retorno = False
		
		if __nombreMetodo == "moverPeon":
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
						if __nombreMetodo == "moverKing":
							retorno = self.movimiento(__jugador, __d, matrizTablero, "moverKing", __movimiento, 1)

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
		if True:
			if __nombreMetodo == "moverTorre":
				if __sd[0] == "B":
					for j in range((int(__sd[1]) + overridePieza), (int(__d[0]) + 1)):
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
			else:
				if __nombreMetodo == "moverAlfil":
					#print("En piezaEnIntervalo: __sd = " + __sd)
					if __sd[0] == "S":
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
					else:
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
								print("En " + str(i) + str(l))
								print("tipo: " + matrizTablero[i][l].tipo)
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
			#print("...")
			retorno = self.piezaEnDestino(__d, matrizTablero)
		return retorno
	
	@classmethod
	def accesibleParaKing(self, __d, __jugador, matrizTablero):
		retorno = False
		# Parecido al caballo.
	
	@classmethod
	def accesibleParaCaballo(self, __d, __jugador, matrizTablero):
		retorno = False

		if ((int(__d[0]) + 2) <= 7 and (int(__d[1]) + 1) <= 7):
			if (matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) + 1)].tipo == "C" and matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) + 1)].color == __jugador):
				retorno = str((int(__d[0]) + 2)) + str((int(__d[1]) + 1))
		else:
			if ((int(__d[0]) + 2) <= 7 and (int(__d[1]) - 1) >= 0):
				if (matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) - 1)].tipo == "C" and matrizTablero[(int(__d[0]) + 2)][(int(__d[1]) - 1)].color == __jugador):
					retorno = str((int(__d[0]) + 2)) + str((int(__d[1]) - 1))
			else:
				if ((int(__d[0]) - 2) >= 0 and (int(__d[1]) + 1) <= 7):
					if (matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) + 1)].tipo == "C" and matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) + 1)].color == __jugador):
						retorno = str((int(__d[0]) - 2)) + str((int(__d[1]) + 1))
				else:
					if ((int(__d[0]) - 2) >= 0 and (int(__d[1]) - 1) >= 0):
						if (matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)].tipo == "C" and matrizTablero[(int(__d[0]) - 2)][(int(__d[1]) - 1)].color == __jugador):
							retorno = str((int(__d[0]) - 2)) + str((int(__d[1]) - 1))
					else:
						if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) + 2) <= 7):
							if (matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 2)].tipo == "C" and matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) + 2)].color == __jugador):
								retorno = str((int(__d[0]) + 1)) + str((int(__d[1]) + 2))
						else:
							if ((int(__d[0]) + 1) <= 7 and (int(__d[1]) - 2) >= 0):
								if (matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 2)].tipo == "C" and matrizTablero[(int(__d[0]) + 1)][(int(__d[1]) - 2)].color == __jugador):
									retorno = str((int(__d[0]) + 1)) + str((int(__d[1]) - 2))
							else:
								if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) + 2) <= 7):
									if (matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 2)].tipo == "C" and matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) + 2)].color == __jugador):
										retorno = str((int(__d[0]) - 1)) + str((int(__d[1]) + 2))
								else:
									if ((int(__d[0]) - 1) >= 0 and (int(__d[1]) - 2) >= 0):
										if (matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 2)].tipo == "C" and matrizTablero[(int(__d[0]) - 1)][(int(__d[1]) - 2)].color == __jugador):
											retorno = str((int(__d[0]) - 1)) + str((int(__d[1]) - 2))
		return retorno

	@classmethod
	def sentidoDireccion(self, __movimiento, __jugador, matrizTablero, __d):
		# S, B, I, D
		retorno = False

		# Ver que pasa si por ejemplo 2 Torres están en la misma fila o columna y una puede moverse a un punto determinado y otra no puede.
		# Podría concatenar las ubicaciones de las piezas similares (D3 I7)

		__p = self.identificarPieza(__movimiento, __jugador, matrizTablero)

		if __p == "A":
			print("La pieza es: " + __p + "\nEl destino es: " + __d)
			r = int(__d[1]) # r = derecha
			l = int(__d[1]) # l = izquierda
			for i in range(int(__d[0]), 8):
				if i != int(__d[0]):
					if r < 7 and l > 0:
						r += 1
					#if l > 0:
						l -= 1
				print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
				if matrizTablero[i][r].tipo == __p and matrizTablero[i][r].color == __jugador:
					retorno = "SD" + str(i) + str(r)
				else:
					if matrizTablero[i][l].tipo == __p and matrizTablero[i][l].color == __jugador:
						retorno = "SI" + str(i) + str(l)
			
			r = int(__d[1]) # r = derecha
			l = int(__d[1]) # l = izquierda
			#matrizTablero[int(__d[0])][int(__d[1])] = King()
			#print("D: " + __d)
			i = int(__d[0])
			while i >= 0:
				if i != int(__d[0]):
					if r < 7 and l > 0:
						r += 1
					#if l > 0:
						l -= 1
				#print("R: " + str(i) + str(r) + "\nL: " + str(i) + str(l))
				#matrizTablero[i][r] = King()
				#matrizTablero[i][l] = Caballo()
				#print("Tipo: " + matrizTablero[i][r].tipo)
				if matrizTablero[i][r].tipo == __p and matrizTablero[i][r].color == __jugador:
					retorno = "BD" + str(i) + str(r)
				else:
					if matrizTablero[i][l].tipo == __p and matrizTablero[i][l].color == __jugador:
						retorno = "BI" + str(i) + str(l)

				i -= 1
			#self.mostrar(matrizTablero)
			#input()

		else:
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
						i -= 1
					if not retorno:
						for i in range(int(__d[1]), 8):
							if matrizTablero[int(__d[0])][i].tipo == __p and matrizTablero[int(__d[0])][i].color == __jugador:
								retorno = "I" + str(i)		
		return retorno

	@classmethod
	def movimiento(self, __jugador, __d, matrizTablero, __nombreMetodo, __movimiento, overridePieza):
		retorno = False

		if __nombreMetodo == "moverPeon":
			if __jugador == "b":
				print("El jugador es: " + __jugador)
				for i in range(8):
					if i >= int(__d[0]) and i <= 7:
						#print("Revisando en: " + str(i) + __d[1])
						if matrizTablero[i][int(__d[1])].tipo == "P" and matrizTablero[i][int(__d[1])].color == "b":
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
					if matrizTablero[i][int(__d[1])].tipo == "P" and matrizTablero[i][int(__d[1])].color == "n":
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
					if type(__o) != type(bool()):
						if not overridePieza:
							if not self.piezaEnDestino(__d, matrizTablero):
								retorno = __o + " " + __d
						else:
							#print("...")
							retorno = __o + " " + __d
				else:
					if __nombreMetodo == "moverAlfil":
						__sd = self.sentidoDireccion(__movimiento, __jugador, matrizTablero, __d)
						if type(__sd) != type(bool()):
							print("El sentidoDireccion retornó: " + __sd)
							if not self.piezaEnIntervalo(__d, __sd, matrizTablero, __nombreMetodo, overridePieza):
								#print("...")
								retorno = __sd[2] + __sd[3] + " " + __d
							else:
								0
					else:
						if __nombreMetodo == "moverKing":
							__o = self.accesibleParaKing(__d, __jugador, matrizTablero)
							if type(__o) != type(bool()):
								if not overridePieza:
									if not self.piezaEnDestino(__d, matrizTablero):
										retorno = __o + " " + __d
									else:
										retorno = __o + " " + __d
		return retorno

	@classmethod
	def moverPeon(self, __movimiento, __jugador, matrizTablero):
		retorno = False
		
		__d = self.obtenerFilaColumna(__movimiento, "moverPeon")
		print("El obtenerFilaColumna retornó: " + __d)
		
		if self.esCaptura(__movimiento, "moverPeon"):
			if bool(__d):
				if self.esCapturable(__movimiento, __jugador, __d, matrizTablero):
					retorno = self.capturar(__movimiento, __jugador, __d, matrizTablero, "moverPeon")
		else:
			retorno = self.movimiento(__jugador, __d, matrizTablero, "moverPeon", __movimiento, 0)
			print("El movimiento retornó: " + str(retorno))

		return retorno

	@classmethod
	def moverAlfil(self, __movimiento, __jugador, matrizTablero):
		print("En moverAlfil.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moverAlfil")
		print("El obtenerFilaColumna retornó: " + str(__d))

		if self.esCaptura(__movimiento, "moverAlfil"):
			if bool(__d):
				if self.esCapturable(__movimiento, __jugador, __d, matrizTablero):
					#print("...")
					retorno = self.capturar(__movimiento, __jugador, __d, matrizTablero, "moverAlfil")
		else:
			print("En moverAlfil. esCaptura == False.")
			
			retorno = self.movimiento(__jugador, __d, matrizTablero, "moverAlfil", __movimiento, 0)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (retorno[0] + retorno[1] == retorno[3] + retorno[4]):
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
				if self.esCapturable(__movimiento, __jugador, __d, matrizTablero):
					retorno = self.capturar(__movimiento, __jugador, __d, matrizTablero, "moverTorre")
		else:
			print("En moverTorre. esCaptura == False.")
			
			retorno = self.movimiento(__jugador, __d, matrizTablero, "moverTorre", __movimiento, 0)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (retorno[0] + retorno[1] == retorno[3] + retorno[4]):
			retorno = False
		return retorno

	# Copiar este.
	@classmethod
	def moverCaballo(self, __movimiento, __jugador, matrizTablero):
		print("En moverCaballo.")
		retorno = False
		__d = self.obtenerFilaColumna(__movimiento, "moverCaballo")
		print("El obtenerFilaColumna retornó: " + str(__d))

		if self.esCaptura(__movimiento, "moverCaballo"):
			if self.esCapturable(__movimiento, __jugador, __d, matrizTablero):
				retorno = self.capturar(__movimiento, __jugador, __d, matrizTablero, "moverCaballo")
		else:
			print("En moverCaballo. esCaptura == False.")
			
			retorno = self.movimiento(__jugador, __d, matrizTablero, "moverCaballo", __movimiento, 0)
			print("El movimiento retornó: " + str(retorno))

		if type(retorno) == type(str()) and (retorno[0] + retorno[1] == retorno[3] + retorno[4]): # Revisa que no sea el mismo lugar donde está.
			retorno = False

		return retorno

	@classmethod
	def verificarTurno(self, __jugador):
		retorno = False
		if __jugador == self.turno:
			retorno = True
		return retorno

	@classmethod
	def cambiarTurno(self, __jugador):
		if __jugador == "b":
			self.turno = "n"
		else:
			self.turno = "b"

	@classmethod
	def identificarPieza(self, __movimiento, __jugador, matrizTablero):
		retorno = "P"

		__matrizInicialesPiezas = ["T", "C", "A", "K", "Q"]
		if __movimiento[0] in __matrizInicialesPiezas:
			if __movimiento[0] == "T":
					retorno = "T"
			else:
				if __movimiento[0] == "C":
					retorno = "C"
				else:
					if __movimiento[0] == "A":
						retorno = "A"
					else:
						if __movimiento[0] == "K":
							retorno = "K"
						else:
							if __movimiento[0] == "Q":
								retorno = "Q"
		return retorno

	@classmethod
	def identificarMoverPieza(self, __movimiento, __jugador, matrizTablero):
		retorno = False

		__matrizInicialesPiezas = ["T", "C", "A", "K", "Q"]
		if __movimiento[0] in __matrizInicialesPiezas:
			if __movimiento[0] == "T":
				retorno = self.moverTorre(__movimiento, __jugador, matrizTablero)
			else:
				if __movimiento[0] == "C":
					retorno = self.moverCaballo(__movimiento, __jugador, matrizTablero)
				else:
					if __movimiento[0] == "A":
						retorno = self.moverAlfil(__movimiento, __jugador, matrizTablero)
					else:
						if __movimiento[0] == "K":
							retorno = self.moverKing(__movimiento, __jugador, matrizTablero)
						else:
							if __movimiento[0] == "Q":
								retorno = self.moverQueen(__movimiento, __jugador, matrizTablero)
		else:
			retorno = self.moverPeon(__movimiento, __jugador, matrizTablero)
			print("El moverPeon retornó: " + str(retorno))

		return retorno

	@classmethod
	def mover(self, __movimiento, __jugador, matrizTablero, __turno):
		retorno = False
		
		self.turno = __turno
		
		if self.verificarTurno(__jugador):
			retorno = self.identificarMoverPieza(__movimiento, __jugador, matrizTablero)
			print("El identificarMoverPieza retornó: " + str(retorno))
			if retorno:
				self.cambiarTurno(__jugador)
		return retorno

	def __init__(self):
		self.__turno = "b"