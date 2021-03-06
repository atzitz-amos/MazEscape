import tkinter as tk

class Player():
    def __init__(self, screen):
        self.screen = screen
        self.x = self.y = 0

    def show(self, image=None):
        self.x = self.screen.width / 2
        self.y = self.screen.height / 2
        self.screen.create_oval(self.x,self.y,self.x+20,self.y+20,fill='blue')