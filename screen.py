import tkinter as tk
from player import Player

class Screen(tk.Canvas):
    def __init__(self, master):
        super().__init__(master=master)
        master.update()
        self['width'] = self.width = master.winfo_screenwidth() 
        self['height'] = self.height = master.winfo_screenheight()
        self['bg'] = "white"
        self.pack_propagate(0)
        self.pack()
        self.player = Player(self)
        self.player.show()