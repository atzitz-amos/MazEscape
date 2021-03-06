import tkinter


class Tile:
    
    id = 0
    
    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        
        x -= 80
        y -= 80

        self.wall_size = 50
        self.path_size = 60

        ws = self.wall_size
        ps = self.path_size

        self.walls = [(x,y,x + self.wall_size,y + self.wall_size),\
                      (x + ws + ps,y,x + 2 * ws + ps,y + ws),\
                      (x,y + ws + ps,x + ws,y + 2 * ws + ps),\
                      (x + ws + ps,y + ws + ps,x + 2 * ws + ps,y + 2 * ws + ps)]

    def show(self) -> None:
        self.img = tkinter.PhotoImage(file=f'.\\res\\textures\\tiles\\tile_{self.id}.png').zoom(10)
        print(self.img.width(),self.img.height())
        self.screen.create_image(self.x,self.y,image=self.img)
    
    def isInWall(self,bbox:list) -> bool:
        x,y,x2,y2 = bbox
        v = 10
        c1 = x + (x2 - x) / 2,y + v
        c2 = x + v,y + (y2 - y) / 2
        c3 = x + (x2 - x) / 2,y2 - v
        c4 = x2 - v,y + (y2 - y) / 2
        for w in self.walls:
            wx,wy,wx2,wy2 = w
            for i,(px,py) in enumerate([c1,c2,c3,c4]):
                if px >= wx and px <= wx2 and py >= wy and py <= wy2:
                    print('in')
                    return True,i
        return False,None

