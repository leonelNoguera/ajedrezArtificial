from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from clases.tablero import Tablero

# Página 71.

class TableroScreen(GridLayout): 
	#def btn_pressed(self, instance, pos):
		#tablero.mover("c4", "w")
		#self.lbl.text = str(self.tablero)
	
	def __init__(self, ** kwargs):
		super(TableroScreen, self).__init__(** kwargs)
		self.tablero = Tablero()
		self.tablero.inicializarPiezas()
		self.tablero.colocarPiezas()
		self.lbl = Label()
		self.lbl.text = str(self.tablero)

		self.btn = Button()
		self.btn.text = "Siguiente."
		
		#self.btn.bind(pressed=self.btn_pressed)

		self.rows = 2
		self.add_widget(self.lbl)
		self.add_widget(self.btn)
	
class TableroApp(App):
	def build(self):
		return TableroScreen()


TableroApp().run()