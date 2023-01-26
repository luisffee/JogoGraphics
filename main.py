from graphics import *
from settings import *
from level import Level
from player import Player


class Game:
    def __init__(self):
        self.screen = GraphWin(f'{GAMENAME}', WIDTH, HEIGHT, autoflush=False)
        self.level = Level(self.screen)
        # pass

    def run(self):
        # Game Loop

        while True:
            self.key = self.screen.checkKey()
            self.click = self.screen.checkMouse()
            self.level.update(self.key, self.click)

            if 'Escape' in self.key:
                if self.menu():
                    break
                else:
                    pass
                pass

        self.screen.close()

    def menu(self):
        # Esc Menu

        recbg = Rectangle(Point(0, 0), Point(800, 600))
        bg = color_rgb(100, 100, 100)
        recbg.setFill(bg)
        recbg.draw(self.screen)

        recEsc = Rectangle(Point(300, 200), Point(500, 250))
        recEsc.setFill('Red')
        recEsc.draw(self.screen)

        recEscCenter = recEsc.getCenter()

        escText = Text(recEscCenter, 'Fechar Jogo')
        escText.setSize(18)
        escText.setStyle('bold')
        escText.draw(self.screen)

        recCon = Rectangle(Point(300, 300), Point(500, 350))
        recCon.setFill('Blue')
        recCon.draw(self.screen)

        recConCenter = recCon.getCenter()

        ConText = Text(recConCenter, 'Continuar')
        ConText.setSize(18)
        ConText.setStyle('bold')
        ConText.draw(self.screen)

        a = self.screen.getMouse()
        if (300 < a.x < 500) and (200 < a.y < 250):
            return True
        if (300 < a.x < 500) and (300 < a.y < 350):
            recbg.undraw()
            recEsc.undraw()
            escText.undraw()
            recCon.undraw()
            ConText.undraw()
            return False


if __name__ == '__main__':
    exe = Game()
    exe.run()
