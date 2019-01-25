# Ajedrez Artificial

Instrucciones de uso:
--------------------

Para utilizar con el modo de juego real (con las reglas del ajedrez según la F.I.D.E.) es necesario seguir los siguientes pasos:

1)_ Ir al directorio 'ajedrezArtificial/webApp/server/'.
2)_ Desde la terminal o la consola de comandos ejecutar el comando: python3 index.py
	Esto dará inicio al servidor del juego. Recibirá los comandos por medio de POST desde un cliente.

3)_ Abrir el archivo 'ajedrezArtificial/webApp/web_client/index.html' desde el navegador.

4)_ A la derecha del tablero observará un cuadro de texto. En este cuadro se pueden insertar los comandos que serán enviados al servidor del juego. Puede copiar y pegar el siguiente ejemplo en dicho cuadro:

init
a4
b5
Nf3
Ba6
e3
bxa4
Rxa4
Bxf1
Kxf1
Nf6
Ne5
Nc6
c4
h5
f4
h4
c5
Rh5
Qxh5

El comando 'init' inicia el juego. Los que restan corresponden a la notación algebraica en inglés.

5)_ Para probar esos comandos precione el botón 'Iniciar' y luego el botón '-->' varias veces. Observará entonces el movimiento de las piezas en el tablero.

Para utilizar con el modo de juego libre (sin las reglas) es necesario seguir los siguientes pasos:

1)_ Abrir el archivo 'ajedrezArtificial/webApp/web_client/index.html' desde el navegador.
2)_ Precione el botón 'Juego libre'. Esto llenará el tablero con las piezas.
3)_ Haga click en alguna pieza y luego en alguna casilla libre u ocupada. La pieza cambiará de casilla.
4)_ Para eliminar una pieza haga click 2 veces en la misma.
5)_ Para reponer las piezas en el tablero puede utilizar las que están debajo del tablero o precionar nuévamente el botón 'Juego libre'.