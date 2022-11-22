from graphics import *
from settings import *
from player import Player
from tile import Tile


class Level:
    def __init__(self, main):

        # get the display surface
        self.win = main
        self.tiles = []
        self.recs = []
        self.Player = Player(self.win)
        self.speed = 5

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

        upd1 = self.collision('Vertical', collision)  # y += 1 or y += -1
        upd2 = self.collision('Horizontal', collision)  # x += 1 or x += -1
        for img in self.tiles:
            img.move((x + upd2) * self.speed, (y + upd1) * self.speed)
        for img in self.recs:
            img.move((x + upd2) * self.speed, (y + upd1) * self.speed)

        '''for recs in self.recs:
            #recs.move(10, 0)
            p1 = recs.getP1()
            p2 = recs.getP2()
            if collision[0].x < p2.x:
                if p1.y > collision[0].y > p2.y:
                    break
            else:
                recs.move(10, 0)'''

    def collision(self, direction, playerRecs):
        pp1 = playerRecs[0]
        pp2 = playerRecs[1]

        if direction == 'Horizontal':
            for recs in self.recs:
                pr1 = recs.getP1()
                pr2 = recs.getP2()
                #print(pr2.x, pp2.x, pr1.x)
                if pp2.x < pr2.x < pp1.x and pp1.y > pr2.y > pp2.y:
                    print('Collison Right')
                if pr1.x > pp1.x > pr1.x and pr2.y > pp1.y > pr1.y:
                    print('Collison Right')

        if direction == 'Vertical':
            return 0
        else:
            return 0

    def update(self, key):
        self.Player.update(key)
        recpoints = self.Player.drawR()
        self.move_map(self.Player.input(key), recpoints)
