from graphics import *
from settings import *
from player import Player
from tile import Tile
from ui import UI


class Level:
    def __init__(self, main):

        # get the display surface
        self.win = main
        self.tiles = []
        self.recs = []
        self.Player = Player(self.win)
        self.ui = UI(self.win)
        self.speed = 7

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
                    pos = [x, y]
                    tile = Tile(self.win, pos)
                    self.tiles.append(tile.img)
                    self.recs.append(tile.rec)
                if col == 'p':
                    pass

    def move_map(self, direction, collision):
        x = direction[0]
        y = direction[1]

        for img in self.tiles:
            img.move((x) * self.speed, (y) * self.speed)
        for img in self.recs:
            img.move((x) * self.speed, (y) * self.speed)
        if self.collision(collision, x, y):
            self.ui.move()

    def collision(self, playerRecs, x=None, y=None):

        pp1 = playerRecs[0]
        pp2 = playerRecs[1]
        px = []
        py = []

        for i in range(int(pp1.x), int(pp2.x+1)):
            px.append(i)
        for i in range(int(pp1.y), int(pp2.y+1)):
            py.append(i)
        for rec in self.recs:
            rx = []
            ry = []
            r1 = rec.getP1()
            r2 = rec.getP2()
            for i in range(int(r1.x), int(r2.x+1)):
                rx.append(i)
            for i in range(int(r1.y), int(r2.y+1)):
                ry.append(i)
            a = set(px)
            b = set(rx)
            c = set(py)
            d = set(ry)
            if (a & b) and (c & d):
                for img in self.tiles:
                    img.move((x * -1) * self.speed, (y * -1) * self.speed)
                for img in self.recs:
                    img.move((x * -1) * self.speed, (y * -1) * self.speed)
                return True
        return False

    def update(self, key):
        self.Player.update(key)
        recpoints = self.Player.drawR()
        self.move_map(self.Player.input(key), recpoints)
        self.ui.update()
