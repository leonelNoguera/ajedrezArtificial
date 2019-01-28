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
	def mover(self, movimiento):
		print('Line 43: El turno actual es: ' + self.reglamento.turno)
		#__retornoReglamento = self.__reglamento.mover(__movimiento, __jugador, self.matrizBoard, self.__reglamento.turno)
		retornoReglamento = self.reglamento.mover(
			movimiento, self.reglamento.turno, self.matrizBoard
			)
		print("El reglamento retornó: " + str(retornoReglamento))
		if type(retornoReglamento) == type(str()):
			self.moverOD(retornoReglamento)
			return True
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
			if self.mover(__movimiento, __j) == True:
				i += 1
				self.movimientosToFile(__movimiento, __j)
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
		retorno = "=======================\n"

		for i in range(8):		
			for j in range(8):
				__elementoAux = self.matrizBoard[i][j]
				retorno += str(__elementoAux) + "-"
			retorno += "\n"
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