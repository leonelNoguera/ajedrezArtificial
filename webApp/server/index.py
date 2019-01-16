from http.server import HTTPServer, SimpleHTTPRequestHandler
from io import BytesIO
import json

from clases_py.tablero import Tablero

tablero = Tablero()
tableroIsInit = False

class ChessHandler(SimpleHTTPRequestHandler):
	#def __init__(self):
		#self.c = 0
	#def do_get():
		#pass
	def end_headers(self):
		self.send_header('Access-Control-Allow-Origin', '*')
		SimpleHTTPRequestHandler.end_headers(self)

	def do_POST(self):
		#c = c + 1
		content_length = int(self.headers['Content-Length'])
		body = self.rfile.read(content_length)

		self.send_response(200)
		self.end_headers()

		#response = BytesIO()
		#response.write(b'Recibido: ' + body)

		#self.wfile.write(body)

		#f = open("query.json", 'r')
		#json_str = f.read()
		#f.close()

		#id = 0

		#dec = json.JSONDecoder()
		#try:
			#jsonObj = dec.decode(json_str.replace("\'", "\""))
			#id = int(jsonObj["id"]) + 1
		#except Exception as e:
			#id = 0

		#jsonObj = 0

		#if len(json_str):
			#id = id + 1
		#if json_str.find("'id': 0") > 0:
			#id = id + 1
		#else:
			#if len(json_str):
				#id = id + 1

		#en = json.JSONEncoder()

		comando = str(body)
		comando = comando.replace("b'comando=", "")
		comando = comando.replace("'", "")

		#respuesta = ''

		#if tableroIsInit == False and comando == 'init':

		if comando == 'init':
			tablero.inicializarPiezas()
			tablero.colocarPiezas()
			#tableroIsInit = True
		else:
			if comando == 'random':
				tablero.movimientosAlAzar(1)
			else:
				tablero.mover(comando)

		respuesta = tablero.matrizTablero

		#movimiento = body

		#jsonObj = en.encode({"id":+id, "comando":comando})

		#print(str(body) + " -- " + str(comando) + " -- " + str(jsonObj))
		#m = Main()
		#print(tablero)

		#self.wfile.write(bytes(json_str, 'utf-8'))
		self.wfile.write(bytes(str(respuesta), 'utf-8'))
		
		#f = open("query.json", 'w')
		#f.write(str(jsonObj))
		#f.close()
		

	#def do_GET(self):
		#content_length = int(self.headers['Content-Length'])
		#body = self.rfile.read(content_length)

		#self.send_response(200)
		#self.end_headers()

		#response = BytesIO()
		#response.write(b'Recibido: ' + body)

		#self.wfile.write(body)

httpd = HTTPServer(('localhost', 8080), ChessHandler)
#httpd.serve_forever()
while 1:
	httpd.handle_request()
