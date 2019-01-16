# --- 20180811_0012 --- #
Archivo: tablero.py
Clase: Tablero
Descripción: Esta clase representa el tablero del ajedrez.

Métodos:
	
	def __init__(self):
	
	# Es el constructor de la clase. LLama a self.pintarCasilleros().

	@classmethod
	def __repr__(self):
	
	# Muestra el tablero en pantalla.
	# Recorre self.matrizTablero[i][j] Siendo el atributo que contiene todos los casilleros y elementos derivados.
	# j corresponde a la filas, las cuales son recorrida desde el elemento 0 al 7. Luego se incrementa i.
	# i corresponde a la columnas, las cuales son recorridas desde el elemento 0 al 7.
	# Concatena cada elemento al retorno usando el __repr__ de cada uno.

	@classmethod
	def mover(self, movimiento):

		

	@classmethod
	def moverOD(self, od):

		Variables:
			od
			# Esta variable siempre es tipo str y contiene las coordenadas de origen y destino de la pieza.
			# Ejemplo: '13 33'. Mueve una pieza de 'd7' a 'd5'.
			# En el caso especial de que el movimiento sea castling, od == '00 00'. Con esto no se realiza intercambio de piezas.

		# Por último llama a: self.pintarCasilleros().

...

Archivo: reglamento.py
Clase: Reglamento
Descripción: Esta clase se encarga de la mayoría de las cosas en el juego. Contiene las reglas del ajedrez.
Métodos:
	def __init__(self):
	
	# Es el constructor de la clase. Inicializa self.__turno en "b".

	@classmethod
	def mover(self, __movimiento, __jugador, matrizTablero, __turno):
	
	# Verifica que sea el turno del jugador actual son self.verificarTurno(__jugador).
	# En caso de ser el turno correcto, llama a self.identificarMoverPieza(__movimiento, __jugador, matrizTablero) el cual retorna False o algo como "01 03".
		
...

	@classmethod
	def sentidoDireccion(self, __movimiento, __jugador, matrizTablero, __d):

	# Indica desde donde se va a mover la pieza.
	# Sn: "Subir desde n" - Bn: "Bajar desde n" - In: "Izquierda desde n" - Dn: "Derecha desde n".
	# 

...

	@classmethod
	def piezaEnIntervalo(self, __d, __sd, matrizTablero, __nombreMetodo):

	# Retorna True si hay una pieza en el intervalo.
	# Revisa por fila o columna según indique __sd[0]. 

...

	@classmethod
	def obtenerFilaColumna(self, __movimiento, __nombreMetodo):

	# Retorna las coordenadas del casillero destino.


















Ejemplo de jugadas.
------------------
tablero.mover("g4", "b")
tablero.mover("h5", "n")
tablero.mover("h4", "b")
tablero.mover("g5", "n")

tablero.mover("xg5", "b")
tablero.mover("xg4", "n")

tablero.mover("b4", "b")
tablero.mover("a5", "n")
tablero.mover("a4", "b")
tablero.mover("b5", "n")

tablero.mover("xb5", "b")
tablero.mover("xb4", "n")

tablero.mover("Ta3", "b")
tablero.mover("Ta6", "n") # Mueve un Alfil.

------------------

tablero.mover("Ta6", "n")

tablero --> def mover(self, __movimiento, __jugador)

self.__reglamento.mover(__movimiento, __jugador, self.matrizTablero, self.__reglamento.turno) --> retorna: 05 20 (Alfil en 05).

reglamento --> def mover(self, __movimiento, __jugador, matrizTablero, __turno)

self.identificarMoverPieza(__movimiento, __jugador, matrizTablero) --> retorna: 05 20.

def identificarMoverPieza(self, __movimiento, __jugador, matrizTablero)

self.moverTorre(__movimiento, __jugador, matrizTablero) --> retorna: 05 20.

self.obtenerFilaColumna(__movimiento, "moverTorre") --> retorna: 20.

self.movimiento(__jugador, __d, matrizTablero, "moverTorre", __movimiento) --> retorna: 05 20.

self.sentidoDireccion(__movimiento, __jugador, matrizTablero, __d) --> retorna: B7 (bajar desde el 7).











