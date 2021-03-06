

class Player:

    def __init__(self, screen):
        self.screen = screen

        self.x = self.screen.width / 2
        self.y = self.screen.height / 2

        self._player = None
        self.size = 20

        self._movW = False
        self._movS = False
        self._movA = False
        self._movD = False

        self.screen.after(10,self._move)

        self.screen.master.bind('<KeyPress-w>',lambda e: self.foreward())
        self.screen.master.bind('<KeyPress-s>',lambda e: self.backward())
        self.screen.master.bind('<KeyPress-a>',lambda e: self.left())
        self.screen.master.bind('<KeyPress-d>',lambda e: self.right())

        self.screen.master.bind('<KeyRelease-w>',lambda e: self.Rforeward())
        self.screen.master.bind('<KeyRelease-s>',lambda e: self.Rbackward())
        self.screen.master.bind('<KeyRelease-a>',lambda e: self.Rleft())
        self.screen.master.bind('<KeyRelease-d>',lambda e: self.Rright())

    def show(self, image=None):
        self._player = self.screen.create_oval(self.x - self.size / 2,self.y - self.size / 2,self.x + self.size / 2,self.y + self.size / 2,fill='blue')

    def update(self):
        self.screen.coords(self._player,self.x - self.size / 2,self.y - self.size / 2,self.x + self.size / 2,self.y + self.size / 2)

    def _move(self):
        if self._movA:
            self.x -= self.screen.getSpeed()
        elif self._movD:
            self.x += self.screen.getSpeed()
        if self._movW:
            self.y -= self.screen.getSpeed()
        elif self._movS:
            self.y += self.screen.getSpeed()
        self.update()
        self.screen.after(50,self._move)

    def foreward(self):
        self._movW = True

    def backward(self):
        self._movS = True

    def left(self):
        self._movA = True

    def right(self):
        self._movD = True

    def Rforeward(self):
        self._movW = False

    def Rbackward(self):
        self._movS = False

    def Rleft(self):
        self._movA = False

    def Rright(self):
        self._movD = False
