from graphics import *
from settings import *


class UI():
    def __init__(self, main):
        self.win = main

        self.health_def = 100
        self.max_rec = WIDTH//2 + 98
        self.health_text_size = 20

        self.health_bar_rect = Rectangle(
            Point(WIDTH//2 - 100, HEIGHT-50), Point(WIDTH//2 + 100, HEIGHT - 5))
        self.dinamic_health_bar = Rectangle(
            Point(WIDTH//2 - 98, HEIGHT-48), Point(self.max_rec, HEIGHT - 7))
        center = self.dinamic_health_bar.getCenter()
        self.health_text = Text(
            Point(center.x, center.y+5), f'{self.health_def}%')
        self.health_text.setSize(int(self.health_text_size))

        self.dinamic_health_bar.setFill('red')
        self.dinamic_health_bar.draw(self.win)
        self.health_bar_rect.draw(self.win)
        self.health_text.draw(self.win)

    def draw(self):
        pass

    def move(self):

        if self.dinamic_health_bar.getP2().x < self.dinamic_health_bar.getP1().x:
            return False
        self.dinamic_health_bar.undraw()
        self.health_text.undraw()
        self.health_text_size -= 0.5
        self.health_def -= 5
        self.max_rec -= 10

        self.dinamic_health_bar = Rectangle(
            Point(WIDTH//2 - 98, HEIGHT-48), Point(self.max_rec, HEIGHT - 7))
        center = self.dinamic_health_bar.getCenter()
        self.health_text = Text(
            Point(center.x, center.y+5), f'{self.health_def}%')
        self.health_text.setSize(int(self.health_text_size))

        self.dinamic_health_bar.setFill('red')
        self.dinamic_health_bar.draw(self.win)
        self.health_text.draw(self.win)

    def dead(self):
        if self.health_def == 0:
            dead_text = Text(Point(WIDTH//2, HEIGHT//2), 'You Are DEAD !!!')
            # dead_text.setSize(40)
            dead_text.setTextColor('red')
            # dead_text.setStyle('bold')
            dead_text.draw(self.win)

    def update(self):
        self.draw()
        self.dead()
        # self.move(colli)
