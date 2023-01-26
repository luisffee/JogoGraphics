from graphics import *
from settings import *


class UI():
    def __init__(self, main):
        self.win = main

        self.health_def = 100
        self.max_rec = WIDTH//2 + 98
        self.health_text_size = 20
        self.score_text = 0

        self.health_bar_rect = Rectangle(
            Point(WIDTH//2 - 100, HEIGHT-50), Point(WIDTH//2 + 100, HEIGHT - 5))
        self.dinamic_health_bar = Rectangle(
            Point(WIDTH//2 - 98, HEIGHT-48), Point(self.max_rec, HEIGHT - 7))
        center = self.dinamic_health_bar.getCenter()
        self.health_text = Text(
            Point(center.x, center.y+5), f'{self.health_def}%')
        self.health_text.setSize(int(self.health_text_size))

        self.score_txt = Text(
            Point(WIDTH//2, HEIGHT-500), f'{self.score_text}')

        self.dinamic_health_bar.setFill('red')
        # self.dinamic_health_bar.draw(self.win)
        self.score_txt.setSize(24)
        self.score_txt.setStyle('bold')
        # self.health_bar_rect.draw(self.win)
        # self.health_text.draw(self.win)
        self.score_txt.draw(self.win)

    def score(self):
        # Score do player
        if self.attack == True:
            self.score_txt.undraw()
            self.score_text += 50
            self.score_txt = Text(
                Point(WIDTH//2, HEIGHT-500), f'{self.score_text}')
            self.score_txt.setSize(24)
            self.score_txt.setStyle('bold')
            self.score_txt.draw(self.win)

    def move(self):
        # Barra de vida do player
        if self.dinamic_health_bar.getP2().x < self.dinamic_health_bar.getP1().x:
            return False
        if True in self.damage:
            for zombie_attack in self.damage:
                if zombie_attack == True:
                    self.dinamic_health_bar.undraw()
                    self.health_text.undraw()
                    self.health_text_size -= 0.5
                    self.health_def -= 5
                    self.max_rec -= 5

                    self.dinamic_health_bar = Rectangle(
                        Point(WIDTH//2 - 98, HEIGHT-48), Point(self.max_rec, HEIGHT - 7))
                    center = self.dinamic_health_bar.getCenter()
                    self.health_text = Text(
                        Point(center.x, center.y+5), f'{self.health_def}%')
                    if self.health_text_size > 5:
                        self.health_text.setSize(int(self.health_text_size))

                    self.dinamic_health_bar.setFill('red')
                    self.dinamic_health_bar.draw(self.win)
                    self.health_text.draw(self.win)
                    self.dead()
                    # print('hey')

    def dead(self):
        # Texto de morto do player
        if self.health_def == 0:
            dead_text = Text(Point(WIDTH//2, HEIGHT//2 - 20),
                             'You Are DEAD !!!')
            # dead_text.setSize(40)
            dead_text.setTextColor('red')
            # dead_text.setStyle('bold')
            dead_text.draw(self.win)
            return True

    def update(self, damage, attack):
        self.damage = damage
        self.attack = attack
        # self.move()
        self.score()
