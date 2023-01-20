from graphics import *
from settings import *


class Tile():
    def __init__(self, main, position, type):
        self.win = main
        self.pos = position
        self.type = type
        self.draw()

    def draw(self):
        obj = {
            'border': 'src/sprites/rock.png',
            'object': 'src/sprites/Tree1.png'
        }
        x = self.pos[0]
        y = self.pos[1]
        if self.type == 'object':
            self.img = Rectangle(Point(x-32, y-32), Point(x+32, y+32))
            self.img.draw(self.win)
            #self.Rec(x, y, self.img)
            self.img.setState('hidden')
        if self.type == 'border':
            self.img = Rectangle(Point(x-32, y-32), Point(x+32, y+32))
            self.img.draw(self.win)
            self.img.setState('hidden')

    def Rec(self, x, y, img):
        w = img.getWidth()
        h = img.getHeight()
        self.rec = Rectangle(Point(x - (w/2), y - (h/2)),
                             Point(x + (w/2), y + (w/2)))
        self.rec.setState('hidden')
        self.rec.draw(self.win)
        self.p1 = self.rec.getP1()
        self.p2 = self.rec.getP2()
        points = [self.p1, self.p2]
        return points
