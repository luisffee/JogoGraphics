from graphics import *
from settings import *
from player import Player


class Level:
    def __init__(self, main):

        # get the display surface
        self.win = main
        self.tiles = []
        self.recs = []
        self.Player = Player(self.win)

        self.create_map()

    def create_map(self):
        with open('components/position.txt', 'r+') as file2:
            data = file2.read()
            data = data.split(':')
        self.center = [int(data[0]), int(data[1])]

        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = (col_index * TILESIZE)
                y = (row_index * TILESIZE)
                if col == 'x':
                    img = Image(Point(x, y), 'src/sprites/rock.png')
                    img.draw(self.win)
                    w = img.getWidth()
                    h = img.getHeight()
                    rec = Rectangle(Point(x - (w/2), y - (h/2)),
                                    Point(x + (w/2), y + (w/2)))
                    rec.draw(self.win)
                    self.tiles.append(img)
                    self.recs.append(rec)
                if col == 'p':
                    pass

    def move_map(self, direction, collision):
        if direction == 'Right':
            for img in self.tiles:
                img.move(-10, 0)

        if direction == 'Left':
            '''for img in self.tiles:
                img.move(10, 0)'''
            for recs in self.recs:
                #recs.move(10, 0)
                p1 = recs.getP1()
                p2 = recs.getP2()
                if collision[0].x < p2.x:
                    if p1.y > collision[0].y > p2.y:
                        break
                else:
                    recs.move(10, 0)
        if direction == 'Up':
            for img in self.tiles:
                img.move(0, 10)

        if direction == 'Down':
            for img in self.tiles:
                img.move(0, -10)

    def update(self, key):
        self.Player.update(key)
        self.move_map(self.Player.input(key))
