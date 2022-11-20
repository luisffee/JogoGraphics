from graphics import *
from settings import *


class Player:
    def __init__(self, main):
        self.win = main
        self.lastKey = ''

    def drawP(self, key):
        self.key = key

        with open('components/position.txt', 'r+') as file2:
            data = file2.read()
            data = data.split(':')

        self.listaIdleLeft = []
        for i in range(1, 10):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Idle/Idle_left ({i}).png')
            self.listaIdleLeft.append(img)
        self.listaIdleRight = []
        for i in range(1, 10):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Idle/Idle_right ({i}).png')
            self.listaIdleRight.append(img)
        self.listaWalkRight = []
        for i in range(1, 11):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Walk/Walk_right ({i}).png')
            self.listaWalkRight.append(img)
        self.listaWalkLeft = []
        for i in range(1, 11):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Walk/Walk_left ({i}).png')
            self.listaWalkLeft.append(img)
        self.listaWalkUp = []
        for i in range(1, 11):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Walk/Walk_up ({i}).png')
            self.listaWalkUp.append(img)
        if self.key == 'w' or self.key == 's' or self.key == 'a' or self.key == 'd':
            if self.key == 'd':
                for img in self.listaWalkRight:
                    img.draw(self.win)
                    update()
                    time.sleep(0.07)
                    img.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()
                    self.lastKey = 'd'
            else:
                for img in self.listaWalkLeft:
                    img.draw(self.win)
                    update()
                    time.sleep(0.07)
                    img.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()
                    self.lastKey = 'a'
            '''if self.key == 'w':
                for img in self.listaWalkUp:
                    img.draw(self.win)
                    update()
                    time.sleep(0.07)
                    img.undraw()
                    self.lastKey = 'w'
                    '''
        else:

            if self.lastKey == 'a':
                for imgs in self.listaIdleLeft:
                    imgs.draw(self.win)
                    update()
                    time.sleep(0.07)
                    imgs.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()
            else:
                for imgs in self.listaIdleRight:
                    imgs.draw(self.win)
                    update()
                    time.sleep(0.07)
                    imgs.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()

    def input(self, key):
        self.key = key
        with open('components/position.txt', 'r+') as file:
            data = file.read()
            data = data.split(':')
            x = int(data[0])
            y = int(data[1])
        if self.key == 'w':
            '''y -= 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            return 'Up'
        if self.key == 's':
            '''y += 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            return 'Down'
        if self.key == 'd':
            '''x += 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            return 'Right'
        if self.key == 'a':
            '''x -= 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            return 'Left'

    def drawR(self):

        x1 = (WIDTH // 2) - (self.w // 2) + 12
        y1 = (HEIGHT // 2) - (self.h // 2) + 58
        x2 = (WIDTH // 2) + (self.w // 2) - 12
        y2 = (HEIGHT // 2) + (self.h // 2) + 2

        self.rec = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rec.draw(self.win)
        recpoints = []
        recpoints.append(self.rec.getP1())
        recpoints.append(self.rec.getP2())
        return recpoints

    def update(self, key):
        self.drawP(key)
        self.input(key)
