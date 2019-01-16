#!/usr/bin/python
#print ("...")
#http://www.123ajedrez.com/reglas-basicas/notacin

from clases_py.tablero import Tablero
# Inicializar tablero, colocar piezas y mostrar.

tablero = Tablero()
tablero.inicializarPiezas()
tablero.colocarPiezas()

#while 1:
	#tablero.mover(input())
	#print("\n" + str(tablero))

#tablero.mover("d4")
#tablero.mover("a6")

#print(tablero)

movimientos = []

movimientos.append("d4")
movimientos.append("e5")
movimientos.append("d5")
movimientos.append("e4")
movimientos.append("d6")
movimientos.append("e3")
movimientos.append("Bd2")
movimientos.append("Be7")
movimientos.append("dxe7")
movimientos.append("exf2")
movimientos.append("exd8Q")
movimientos.append("fxe1Q") # b

movimientos.append("b4")
movimientos.append("f5")
movimientos.append("b5")
movimientos.append("f4") # b
movimientos.append("g4")

#movimientos.append("fxg3a.p.") # b

#movimientos.append("e4")
#movimientos.append("c6") # b
#movimientos.append("e5")
#movimientos.append("c5")
#movimientos.append("bxc6a.p.") # No debería mover.

tablero.partida(movimientos)

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
#print("\n" + str(tablero))
