from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from clases.tablero import Tablero

# Página 71.

tablero = Tablero()
tablero.inicializarPiezas()
tablero.colocarPiezas()

class BtnS(Button):

	#def on_touch_down(self, touch):
		#if self.collide_point( *touch.pos):
			#self.pressed = touch.pos
			#return True
		#return super(Button, self).on_touch_down(touch)
	@property
	def outputItem(self):
		return self.__outputItem

	@outputItem.setter
	def outputItem(self, value):
		self.__outputItem = value

	@property
	def tablero(self):
		return self.__tablero

	@tablero.setter
	def tablero(self, value):
		self.__tablero = value
	
	@classmethod
	def setTablero(self, tablero):
		self.tablero = tablero

	@classmethod
	def setOutputItem(self, outputItem):
		self.outputItem = outputItem

	def on_pressed(self, instance):
		tablero.mover("b4", "w")
		outputItem.text = str(self.tablero)
		#print (’pressed at {pos}’.format(pos=pos))

	def __init__(self, ** kwargs):
		self.pressed = ListProperty([0, 0])
		#self.__tablero = ""
		super(Button, self).__init__(** kwargs)

class TableroScreen(GridLayout): 
	#def btn_pressed(self, instance, pos):
		#tablero.mover("", "")
		#self.lbl.text = str(self.tablero)
	
	def __init__(self, ** kwargs):
		super(TableroScreen, self).__init__(** kwargs)
		self.tablero = Tablero()
		self.tablero.inicializarPiezas()
		self.tablero.colocarPiezas()
		#self.tablero.mover("c4", "w")
		self.lbl = Label()
		self.lbl.text = str(self.tablero)

		#self.btn = Button()
		#self.btn.text = "Siguiente."

		self.btnS = BtnS()
		
		self.btnS.setTablero(self.tablero)
		self.btnS.setOutputItem(self.lbl)

		self.lbl.text = str(self.tablero)

		self.btnS.text = "Siguiente."
		
		#self.btnS.bind(pressed=self.btn_pressed)

		self.rows = 2
		self.files = 2
		self.add_widget(self.lbl)
		#self.add_widget(self.btn)
		self.add_widget(self.btnS)

class TableroApp(App):
	def build(self):
		return TableroScreen()


TableroApp().run()