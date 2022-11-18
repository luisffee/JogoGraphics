from graphics import *
from settings import *
from level import Level
from player import Player


class Game:
    def __init__(self):
        self.screen = GraphWin(f'{GAMENAME}', WIDTH, HEIGHT, autoflush=False)
        self.level = Level(self.screen)
        self.player = Player(self.screen)
        # pass

    def run(self):
        while True:
            self.key = self.screen.checkKey()
            self.player.drawP(self.key)
            self.level.move_map(self.player.input(self.key))

            if 'Escape' in self.key:
                break
        self.screen.close()


if __name__ == '__main__':
    exe = Game()
    exe.run()
