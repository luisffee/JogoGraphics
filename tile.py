from graphics import *
from settings import *


class Tile():
    def __init__(self, main, position):
        self.win = main
        self.pos = position
        self.draw()

    def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        self.img = Image(Point(x, y), 'src/sprites/rock.png')
        self.img.draw(self.win)
        self.Rec(x, y)

    def Rec(self, x, y):
        w = self.img.getWidth()
        h = self.img.getHeight()
        self.rec = Rectangle(Point(x - (w/2), y - (h/2)),
                             Point(x + (w/2), y + (w/2)))
        self.rec.draw(self.win)
        self.p1 = self.rec.getP1()
        self.p2 = self.rec.getP2()
        points = [self.p1, self.p2]
        return points
