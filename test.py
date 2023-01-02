from graphics import *
from settings import *
import time
from threading import Thread

screen = GraphWin(f'{GAMENAME}', WIDTH, HEIGHT, autoflush=False)

start_time = time.time()


class a():
    def i(self):

        listaIdleLeft = []
        for i in range(1, 10):
            img = Image(Point(WIDTH//2, HEIGHT//2),
                        f'src/sprites/Zombies/Wild Zombie/Idle/Idle_left ({i}).png')
            listaIdleLeft.append(img)
        for img in listaIdleLeft:
            img.draw(screen)
            update()
            time.sleep(0.07)
            img.undraw()


ass = a()
while True:

    ass.i()
