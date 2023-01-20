from graphics import *
from settings import *
from support import *
from player import Player
from tile import Tile
from ui import UI
from enemy import Enemy


class Level:
    def __init__(self, main):

        # get the display surface
        self.win = main
        self.tiles = []
        self.recs = []
        self.enemies = []
        self.Player = Player(self.win)

        self.speed = 7

        self.create_map()
        self.ui = UI(self.win)

    def create_map(self):
        self.bg = Image(Point(2208, 2208),
                        'src/tilesets/Tilemap/base.png')
        self.bg.draw(self.win)
        layouts = {
            'border': import_csv_layout('src/tilesets/Tilemap/border.csv'),
            'object': import_csv_layout('src/tilesets/Tilemap/objects.csv'),
            'enemies': import_csv_layout('src/tilesets/Tilemap/enemies.csv')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = (col_index * TILESIZE)
                        y = (row_index * TILESIZE)
                        pos = [x, y]
                        if style == 'border':
                            tile = Tile(self.win, pos, 'border')
                            # self.tiles.append(tile.img)
                            self.recs.append(tile.img)
                        if style == 'object':
                            tile = Tile(self.win, pos, 'object')
                            # self.tiles.append(tile.img)
                            self.recs.append(tile.img)
                        if style == 'enemies':
                            self.enemy = Enemy(self.win, pos, 'Wild Zombie')

                            self.img = Image(
                                Point(pos[0], pos[1]), wild_zombie_idle_left)
                            self.img.draw(self.win)
                            self.enemies.append(self.img)

    def move_map(self, direction, collision):
        x = direction[0]
        y = direction[1]
        self.bg.move((x) * self.speed, (y) * self.speed)
        for img in self.tiles:
            img.move((x) * self.speed, (y) * self.speed)
        for img in self.recs:
            img.move((x) * self.speed, (y) * self.speed)
        for img in self.enemies:
            img.move((x) * self.speed, (y) * self.speed)
        if self.collision(collision, x, y):
            pass
            # self.ui.move()

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
                self.bg.move((x * -1) * self.speed, (y * -1) * self.speed)
                for img in self.tiles:
                    img.move((x * -1) * self.speed, (y * -1) * self.speed)
                for img in self.recs:
                    img.move((x * -1) * self.speed, (y * -1) * self.speed)
                for img in self.enemies:
                    img.move((x * -1) * self.speed, (y * -1) * self.speed)
                return True
        return False

    def update(self, key, mouse):
        self.Player.update(key, mouse, self.enemies)
        damage = self.Player.attack(self.enemies)
        # self.win.getKey()
        recpoints = self.Player.drawR()
        self.move_map(self.Player.input(key), recpoints)

        self.enemy.update(self.enemies, damage)
        self.ui.update(self.enemy.attack(), damage)
