import random
from clases.reglamento import Reglamento
from clases.piezas.peon import Peon
from clases.piezas.king import King
from clases.piezas.queen import Queen
from clases.piezas.alfil import Alfil
from clases.piezas.caballo import Caballo
from clases.piezas.torre import Torre
from clases.casillero import Casillero

class Tablero:
	matrizTablero = []
	__matrizPiezas = []
	__reglamento = Reglamento()

	@property
	def reglamento(self):
		return self.__reglamento
	
	@classmethod
	def moverOD(self, __od):
		print("Recibido en moverOD: " + __od)
		
		self.matrizTablero[int(__od[3])][int(__od[4])] = self.matrizTablero[int(__od[0])][int(__od[1])]
		self.matrizTablero[int(__od[0])][int(__od[1])] = Casillero()
		self.pintarCasilleros()
	
	@classmethod
	def mover(self, __movimiento, __jugador):
		retorno = False
		__retornoReglamento = self.__reglamento.mover(__movimiento, __jugador, self.matrizTablero, self.__reglamento.turno)
		print("El reglamento retornó: " + str(__retornoReglamento))
		if type(__retornoReglamento) == type(str()):
			self.moverOD(__retornoReglamento)
			retorno = True
		return retorno
		
	@classmethod
	def inicializarPiezas(self):
		self.__matrizPiezas.append([Torre(), Caballo(), Alfil(), Queen(), King(), Alfil(), Caballo(), Torre(),])
		self.__matrizPiezas.append([Peon(), Peon(), Peon(), Peon(), Peon(), Peon(), Peon(), Peon(),])
		self.__matrizPiezas.append([Peon(), Peon(), Peon(), Peon(), Peon(), Peon(), Peon(), Peon(),])
		self.__matrizPiezas.append([Torre(), Caballo(), Alfil(), Queen(), King(), Alfil(), Caballo(), Torre(),])
		for i in range(2):
			for j in range(8):
				self.__matrizPiezas[i][j].color = "n"
				self.__matrizPiezas[i+2][j].color = "b"
				
	@classmethod
	def pintarCasilleros(self):
		__b = Casillero()
		__b.colorCasillero = "b"
		__n = Casillero()
		__n.colorCasillero = "n"
		
		for i in range(8):
			for j in range(8):
				if i % 2:
					if j % 2:
						self.matrizTablero[i][j].colorCasillero = "b"
					else:
						self.matrizTablero[i][j].colorCasillero = "n"
				else:
					if j % 2:
						self.matrizTablero[i][j].colorCasillero = "n"
					else:
						self.matrizTablero[i][j].colorCasillero = "b"
	@classmethod
	def tableroToFile(self):
		f = open("tablero.txt", 'w');
		f.write(str(self.matrizTablero));
	@classmethod
	def movimientosToFile(self, m, j):
		f = open("movimientos.txt", 'a')
		f.write(("tablero.mover(\'" + m + "\', \'" + j + "\')" + "\n"))
		f.close()

	@classmethod
	def colocarPiezas(self):
		__b = Casillero()
		__b.colorCasillero = "b"
		__n = Casillero()
		__n.colorCasillero = "n"
		
		for i in range(8):
			self.matrizTablero.append([Casillero(), Casillero(), Casillero(), Casillero(), Casillero(), Casillero(), Casillero(), Casillero(),])
				
		for i in range(8):
			#Coordenadas en notación: [a-h][8-1]
			# Blancas: 7 y 8
			# Negras: 1 y 2
			# El rey en el casillero de su color.
			self.matrizTablero[0][i] = self.__matrizPiezas[0][i]
			self.matrizTablero[1][i] = self.__matrizPiezas[1][i]
			self.matrizTablero[6][i] = self.__matrizPiezas[2][i]
			self.matrizTablero[7][i] = self.__matrizPiezas[3][i]

		self.pintarCasilleros();
		#self.tableroToFile();
			
	@classmethod
	def movimientosAlAzar(self, cantidad):
		lista = ""
		i = 0
		failed = 0
		__matrizColumnas = ["a", "b", "c", "d", "e", "f", "g", "h"]
		__matrizInicialesPiezas = ["", "T", "C", "A"]
		while i < cantidad:
			__f = random.randint(1, 8)
			__x = random.randint(0, 1)
			__j = random.randint(0, 1)
			
			if __x == 1:
				__x = "x"
			else:
				__x = ""

			if __j == 1:
				__j = "n"
			else:
				__j = "b"

			__c = random.randint(0, 7)
			__c = __matrizColumnas[__c]

			__p = random.randint(0, 3)
			__p = __matrizInicialesPiezas[__p]

			__movimiento = __p + __x + __c + str(__f)

			#if __p == "C":
				#print("Caballo " + __j + " -->" + __movimiento)
			print("El movimiento enviado fue: " + __movimiento)
			print("\n" + self.__repr__())
			if self.mover(__movimiento, __j) == True:
				i += 1
				self.movimientosToFile(__movimiento, __j)
				#print("\n" + self.__repr__())
				#input()
			else:
				failed += 1
				print("Failed: " + __movimiento)

				if failed == 100000:
					print("	Aviso: 100000 fallas\n" + self.__repr__())
					input()
					failed = 0
	@classmethod
	def __repr__(self):
		retorno = "=======================\n"

		for i in range(8):		
			for j in range(8):
				__elementoAux = self.matrizTablero[i][j]
				retorno += str(__elementoAux) + "-"
			retorno += "\n"
		return retorno

	def __init__(self):
		0
		#self.colocarPiezas()