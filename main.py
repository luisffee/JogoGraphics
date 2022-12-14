from graphics import *
from settings import *
from level import Level
from player import Player
import _thread


class Game:
    def __init__(self):
        self.screen = GraphWin(f'{GAMENAME}', WIDTH, HEIGHT, autoflush=False)
        self.level = Level(self.screen)
        # pass

    def run(self):
        while True:
            self.key = self.screen.checkKey()
            self.level.update(self.key)

            if 'Escape' in self.key:
                break
        self.screen.close()


if __name__ == '__main__':
    exe = Game()
    exe.run()
