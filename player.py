import tkinter



class Player:

    def __init__(self, screen):
        self.screen = screen

        self.x = self.screen.width / 2
        self.y = self.screen.height / 2

        self._player = None
        self.size = 40

        self.image = None

        self._movW = False
        self._movS = False
        self._movA = False
        self._movD = False

        self.screen.after(15,self._move)

        self.screen.master.bind('<KeyPress-w>',lambda e: self.foreward())
        self.screen.master.bind('<KeyPress-s>',lambda e: self.backward())
        self.screen.master.bind('<KeyPress-a>',lambda e: self.left())
        self.screen.master.bind('<KeyPress-d>',lambda e: self.right())

        self.screen.master.bind('<KeyRelease-w>',lambda e: self.Rforeward())
        self.screen.master.bind('<KeyRelease-s>',lambda e: self.Rbackward())
        self.screen.master.bind('<KeyRelease-a>',lambda e: self.Rleft())
        self.screen.master.bind('<KeyRelease-d>',lambda e: self.Rright())

    def create_image(self,path):
        del self.image
        self.image = tkinter.PhotoImage(file=path)

    def show(self):
        self.create_image(".\\res\\textures\\player_walk\\player_walk_n_0.png")
        self._player = self.screen.create_image(self.x - self.size / 2,self.y - self.size / 2, image=self.image)

    def update(self):
        self.screen.coords(self._player,self.x - self.size / 2,self.y - self.size / 2)

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
        self.create_image("./res/textures/player_walk/player_walk_n_0.png")

    def backward(self):
        self._movS = True
        self.create_image("./res/textures/player_walk/player_walk_s_0.png")

    def left(self):
        self._movA = True
        self.create_image("./res/textures/player_walk/player_walk_w_0.png")

    def right(self):
        self._movD = True
        self.create_image("./res/textures/player_walk/player_walk_e_0.png")

    def Rforeward(self):
        self._movW = False

    def Rbackward(self):
        self._movS = False

    def Rleft(self):
        self._movA = False

    def Rright(self):
        self._movD = False
