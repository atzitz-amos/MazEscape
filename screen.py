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

        self.generate()

    def getSpeed(self):
        return 3
    
    def generate(self):
        cx,cy = self.width / 2,self.height / 2
        self.img = tk.PhotoImage(file='.\\res\\textures\\tiles\\tile_0.png').zoom(10)
        size = self.img.width()
        self.create_image(cx - size / 2,cy - size / 2,image=self.img)
