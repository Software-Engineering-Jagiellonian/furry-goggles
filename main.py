import kivy
from kivy.app import App  # klasa App
#from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

import random

kivy.require('1.9.0') # największa kompatybilność wsteczna

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generuj_liczbe(self):
        self.random_label.text = str(random.randint(0, 1000))

class RandomCat(App):    # RandomCat dziedziczy po App

    def build(self):
        #return Label(text="RandomCat")
        #return BoxLayout()
        return MyRoot()

randomCat = RandomCat()
randomCat.run()