#http://www.123ajedrez.com/reglas-basicas/notacin
print("Hola.")
from clases.tablero import Tablero
#if __name__ == '__main__':
# Inicializar tablero, colocar piezas y mostrar.

tablero = Tablero()
tablero.inicializarPiezas()
tablero.colocarPiezas()

#print(tablero)

tablero.mover("d4", "w")
tablero.mover("e5", "b")
tablero.mover("d5", "w")
tablero.mover("e4", "b")
tablero.mover("d6", "w")
tablero.mover("e3", "b")
tablero.mover("Bd2", "w")
tablero.mover("Be7", "b")
tablero.mover("dxe7", "w")
tablero.mover("exf2", "b")
tablero.mover("exd8Q", "w")
tablero.mover("fxe1Q", "b")

#print("\n" + str(tablero))

# SD --> Funciona.
# SI --> Funciona.
# BI --> Funciona.
# BD --> Funciona.
# SD con pieza en medio. --> 
# SI con pieza en destino. --> Funciona.
# SD con pieza en destino. --> Funciona.
# BD con pieza en medio. --> 
# BD con pieza en destino. --> Funciona.
# BI con pieza en medio. --> Funciona.
# BI con pieza en destino. --> Funciona.

# Movimientos al azar.
#tablero.movimientosAlAzar(1000)
print("\n" + str(tablero))
