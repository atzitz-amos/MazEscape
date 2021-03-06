import tkinter as tk
from player import Player
import tiles
from tiles.tile_0 import Tile0


class Screen(tk.Canvas):

    def __init__(self, master):

        tk.Canvas.__init__(self,master=master)

        master.update()
        self['width'] = self.width = master.winfo_screenwidth() 
        self['height'] = self.height = master.winfo_screenheight()
        self['bg'] = "white"

        self.focus_get()

        self.pack_propagate(0)
        self.pack()

        self.tiles = []
        self.generate()

        self.player = Player(self)
        self.player.show()
        
        
        
    def getSpeed(self):
        return 2
    
    def generate(self):
        t = Tile0(self,self.width / 2,self.height / 2)
        t.show()
        self.tiles.append(t)
