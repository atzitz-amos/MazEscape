import tkinter


class Player:

    def __init__(self, screen):
        self.screen = screen

        self.x = self.screen.width / 2
        self.y = self.screen.height / 2

        self._player = None
        self.size = 40

        self.image = None
        self.idle_path = None
        self.path = None
        self.mode = 0

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
        self.image = tkinter.PhotoImage(file=path + ".png").zoom(2)
        self.screen.delete(self._player)
        self._player = self.screen.create_image(self.x,self.y,image=self.image)

    def release(self):
        print('release')
        if self._movW:
            self.path = ".\\res\\textures\\player_walk\\player_walk_n_"
            self.idle_path = ".\\res\\textures\\player_idle\\player_idle_n"
        elif self._movA:
            self.path=".\\res\\textures\\player_walk\\player_walk_w_"
            self.idle_path = ".\\res\\textures\\player_idle\\player_idle_w"
        elif self._movD:
            self.path=".\\res\\textures\\player_walk\\player_walk_e_"
            self.idle_path = ".\\res\\textures\\player_idle\\player_idle_e"
        elif self._movS:
            self.path = ".\\res\\textures\\player_walk\\player_walk_s_"
            self.idle_path = ".\\res\\textures\\player_idle\\player_idle_s"
        else:
            self.path = None
            self.create_image(self.idle_path)

    def show(self):
        self.create_image(".\\res\\textures\\player_idle\\player_idle_n")

    def update(self):
        self.screen.coords(self._player,self.x,self.y)

    def _move(self):
        if self.path and (self._movA or self._movD or self._movS or self._movW):
            self.create_image(self.path + ("0" if self.mode <= 6 else "1"))
            if self.mode == 12:
                self.mode = 0
            self.mode += 1
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
        self.path = ".\\res\\textures\\player_walk\\player_walk_n_"
        self.idle_path = ".\\res\\textures\\player_idle\\player_idle_n"

    def backward(self):
        self._movS = True
        self.path = "res/textures/player_walk/player_walk_s_"
        self.idle_path = ".\\res\\textures\\player_idle\\player_idle_s"

    def left(self):
        self._movA = True
        self.path = "./res/textures/player_walk/player_walk_w_"
        self.idle_path = ".\\res\\textures\\player_idle\\player_idle_w"

    def right(self):
        self._movD = True
        self.path = "res/textures/player_walk/player_walk_e_"
        self.idle_path = ".\\res\\textures\\player_idle\\player_idle_e"

    def Rforeward(self):
        self._movW = False
        self.release()

    def Rbackward(self):
        self._movS = False
        self.release()

    def Rleft(self):
        self._movA = False
        self.release()

    def Rright(self):
        self._movD = False
        self.release()
