from graphics import *
from settings import *
import time
import threading


class a():

    def __init__(self):
        self.screen = GraphWin(f'{GAMENAME}', WIDTH, HEIGHT, autoflush=False)
        self.circle = Circle(Point(200, 300), 30)
        self.circle.draw(self.screen)

    def i(self):
        listaIdleLeft = []

        for i in range(1, 10):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Idle/Idle_left_{i}.png')
            listaIdleLeft.append(img)
        for img in listaIdleLeft:
            img.draw(self.screen)
            update()
            # time.sleep(0.07)
            img.undraw()
            self.screen.after(5000, self.i)

    def move(self, key):
        if key == 'a':
            self.circle.setFill('red')
        if key == 'd':
            self.circle.setFill('blue')
        if key == 'w':
            self.circle.setFill('black')
        if key == 's':
            self.circle.setFill('yellow')

    def count(self):
        for _ in range(10):
            self.circle.move(5, 0)

    def update(self, key):
        self.i()
        self.move(key)


assi = a()
while True:

    key = assi.screen.checkKey()
    assi.update(key)
