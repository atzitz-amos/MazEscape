import tkinter as tk
import screen

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.screen = screen.Screen(self)
        self.attributes('-fullscreen',1)
        self.title("MazEscape")

if __name__ == '__main__':
    w = Window()
    w.mainloop()