from graphics import *
from settings import *
from support import *
from entity import Entities
import math
from time import perf_counter


class Enemy(Entities):

    def __init__(self, main, position, type):
        self.win = main
        self.pos = position
        self.type = type
        self.status = 'Idle'
        self.actual_count = 0
        self.cooldown = False
        self.attacked = [False]

        # self.import_graphics(type)
        # self.draw()

    '''def draw(self):
        x = self.pos[0]
        y = self.pos[1]
        if self.type == 'Wild Zombie':
            if self.status == 'Attack':
                for status in self.animations.items():
                    for self.img in status[1]:
                        self.img.draw(self.win)
                        update()
                        time.sleep(0.07)
                        self.img.undraw()
            if self.status == 'Idle':
                self.img = Image(
                    Point(self.pos[0], self.pos[1]), wild_zombie_idle_left)
                self.img.draw(self.win)

        #self.img = Rectangle(Point(x-32, y-32), Point(x+32, y+32))
        # self.img.draw(self.win)
        # self.img.setState('hidden')'''

    def pattern(self):
        # Geral do Inimigo

        for zombie in self.listofenemies:

            self.directx = 0
            self.directy = 0
            if self.cooldown == True:
                if self.actual_count >= 0.3:
                    self.actual_count = 0
                    self.cooldown = False
                    self.attacked = [False]
            cou1 = perf_counter()

            if zombie.getAnchor().x - WIDTH//2 > 0:
                self.directx = -1

            else:
                self.directx = 1
            if zombie.getAnchor().y - HEIGHT//2 > 0:
                self.directy = -1
            else:
                self.directy = 1
            self.distvector = int(math.hypot(
                zombie.getAnchor().x - WIDTH//2, zombie.getAnchor().y - HEIGHT//2))
            # Movimento atrás do player
            if (self.distvector <= enemy_data['wild_zombie']['detect_range']):
                if self.distvector > 35:
                    zombie.move(
                        enemy_data['wild_zombie']['speed'] * self.directx, enemy_data['wild_zombie']['speed'] * self.directy)
            # Ataque caso na range
            if self.distvector <= enemy_data['wild_zombie']['attack_range']:
                if self.damage != True:
                    if self.cooldown != True:
                        self.attacked.append(True)
                        pos = zombie.getAnchor()
                        if self.directx == -1:
                            listaAttackLeft = []
                            for i in range(1, 5):
                                img = Image(pos,
                                            f'src/sprites/Zombies/Wild Zombie/Attack/Attack_left_{i}.png')
                                listaAttackLeft.append(img)
                            zombie.setState('hidden')
                            for img in listaAttackLeft:
                                img.draw(self.win)
                                update()
                                time.sleep(0.07)
                                img.undraw()
                        else:
                            listaAttackRight = []
                            for i in range(1, 5):
                                img = Image(pos,
                                            f'src/sprites/Zombies/Wild Zombie/Attack/Attack_right_{i}.png')
                                listaAttackRight.append(img)
                            zombie.setState('hidden')
                            for img in listaAttackRight:
                                img.draw(self.win)
                                update()
                                time.sleep(0.07)
                                img.undraw()
                        zombie.setState('normal')
                        self.cooldown = True
                        # print(self.attacked)
            self.attacked.append(False)
            cou2 = perf_counter()
            self.actual_count += cou2 - cou1

    def attack(self):
        return self.attacked

    def update(self, listofenemies, damage):
        self.listofenemies = listofenemies
        self.damage = damage
        self.pattern()
        # print(self.attacked)
        pass
