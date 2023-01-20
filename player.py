from graphics import *
from settings import *
from entity import Entities


class Player(Entities):
    def __init__(self, main):
        self.win = main
        self.lastKey = ''
        self.attackrec()

    def drawP(self, key, mouse):
        self.key = key
        self.click = mouse

        with open('components/position.txt', 'r+') as file2:
            data = file2.read()
            data = data.split(':')

        self.listaIdleLeft = []
        for i in range(1, 10):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Idle/Idle_left_{i}.png')
            self.listaIdleLeft.append(img)
        self.listaIdleRight = []
        for i in range(1, 10):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Idle/Idle_right_{i}.png')
            self.listaIdleRight.append(img)
        self.listaWalkRight = []
        for i in range(1, 11):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Walk/Walk_right_{i}.png')
            self.listaWalkRight.append(img)
        self.listaWalkLeft = []
        for i in range(1, 11):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Walk/Walk_left_{i}.png')
            self.listaWalkLeft.append(img)
        self.listaWalkUp = []
        for i in range(1, 11):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Walk/Walk_right_{i}.png')
            self.listaWalkUp.append(img)
        self.listaAttackRight = []
        for i in range(1, 5):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Attack/Attack_right_{i}.png')
            self.listaAttackRight.append(img)
        self.listaAttackLeft = []
        for i in range(1, 5):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Attack/Attack_left_{i}.png')
            self.listaAttackLeft.append(img)

        if self.click:
            if self.lastKey == 'a':
                for img in self.listaAttackLeft:
                    img.draw(self.win)
                    update()
                    time.sleep(0.07)
                    img.undraw()
            if self.lastKey == 'd':
                for img in self.listaAttackRight:
                    img.draw(self.win)
                    update()
                    time.sleep(0.07)
                    img.undraw()

        if self.key == 'w' or self.key == 's' or self.key == 'a' or self.key == 'd':
            if self.key == 'd':
                for img in self.listaWalkRight:
                    img.draw(self.win)
                    update()
                    # time.sleep(0.07)
                    img.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()
                    self.lastKey = 'd'
            else:
                for img in self.listaWalkLeft:
                    img.draw(self.win)
                    update()
                    # time.sleep(0.07)
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
                    # time.sleep(0.07)
                    imgs.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()
            else:
                for imgs in self.listaIdleRight:
                    imgs.draw(self.win)
                    update()
                    # time.sleep(0.07)
                    imgs.undraw()
                    self.w = img.getWidth()
                    self.h = img.getHeight()

    def drawR(self):
        x1 = (WIDTH // 2) - (self.w // 2)
        y1 = (HEIGHT // 2) - (self.h // 2)
        x2 = (WIDTH // 2) + (self.w // 2)
        y2 = (HEIGHT // 2) + (self.h // 2)

        self.rec = Rectangle(Point(x1, y1), Point(
            x2, y2))
        self.rec.setState('hidden')
        self.rec.draw(self.win)
        recpoints = []
        recpoints.append(self.rec.getP1())
        recpoints.append(self.rec.getP2())
        return recpoints

    def attackrec(self):
        self.x1 = (WIDTH // 2) - (64 // 2)
        self.y1 = (HEIGHT // 2) - (64 // 2)
        self.x2 = (WIDTH // 2) + (64 // 2)
        self.y2 = (HEIGHT // 2) + (64 // 2)

        rec = Rectangle(Point(self.x1 - 50, self.y1 - 50),
                        Point(self.x2 + 50, self.y2 + 50))
        rec.draw(self.win)

    def attack(self, enemies):
        px = []
        py = []

        for i in range(int(self.x1 - 50), int(self.x2 + 50)):
            px.append(i)
        for i in range(int(self.y1 - 50), int(self.y2 + 50)):
            py.append(i)

        for zombie in enemies:
            x = zombie.getAnchor().x
            y = zombie.getAnchor().y
            rx = [x]
            ry = [y]
            a = set(px)
            b = set(rx)
            c = set(py)
            d = set(ry)

            if (a & b) and (c & d):
                if self.click:
                    zombie.undraw()
                    return True

    def update(self, key, mouse, enemies):
        self.drawP(key, mouse)
        self.attack(enemies)
