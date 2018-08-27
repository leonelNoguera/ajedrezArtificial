#http://www.123ajedrez.com/reglas-basicas/notacin
from clases.tablero import Tablero

# Inicializar tablero, colocar piezas y mostrar.
tablero = Tablero()
tablero.inicializarPiezas()
tablero.colocarPiezas()
print(tablero)

tablero.mover('h3', 'b')
tablero.mover('c6', 'n')
tablero.mover('Th2', 'b')
tablero.mover('f6', 'n')
tablero.mover('f3', 'b')
tablero.mover('f5', 'n')
tablero.mover('g3', 'b')
tablero.mover('c5', 'n')
tablero.mover('Kf2', 'b')
tablero.mover('b5', 'n')
tablero.mover('Ke1', 'b')
tablero.mover('c4', 'n')
tablero.mover('Kf2', 'b')
tablero.mover('Ab7', 'n')
tablero.mover('e3', 'b')
tablero.mover('Axf3', 'n')
tablero.mover('Ae2', 'b')
tablero.mover('b4', 'n')
tablero.mover('Qf1', 'b')
tablero.mover('Qa5', 'n')
tablero.mover('Qg2', 'b')
tablero.mover('Qxa2', 'n')
tablero.mover('Qxf3', 'b')
tablero.mover('Qxb1', 'n')
tablero.mover('Qxa8', 'b')

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
