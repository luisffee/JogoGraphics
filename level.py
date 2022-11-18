from graphics import *
from settings import *
from player import Player


class Level:
    def __init__(self, main):

        # get the display surface
        self.win = main
        self.tiles = []
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
                    self.tiles.append(img)
                if col == 'p':
                    pass

    def move_map(self, direction):
        if direction == 'Right':
            for img in self.tiles:
                img.move(-10, 0)
        if direction == 'Left':
            for img in self.tiles:
                img.move(10, 0)
        if direction == 'Up':
            for img in self.tiles:
                img.move(0, 10)
        if direction == 'Down':
            for img in self.tiles:
                img.move(0, -10)

    def update(self, key):
        self.Player.update(key)
        self.move_map(self.Player.input(key))
