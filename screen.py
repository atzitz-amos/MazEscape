import tkinter as tk
from player import Player

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

        self.player = Player(self)
        self.player.show()

    def getSpeed(self):
        return 2
