from graphics import *
from settings import *


class Entities():

    def __init__(self):
        pass

    def input(self, key):
        self.key = key
        with open('components/position.txt', 'r+') as file:
            data = file.read()
            data = data.split(':')
            x = int(data[0])
            y = int(data[1])
        direc = [0, 0]
        if self.key == 'w':
            '''y -= 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            direc[1] += +1
            return direc
        if self.key == 's':
            '''y += 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            direc[1] += -1
            return direc
        if self.key == 'd':
            '''x += 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            direc[0] += -1
            return direc
        if self.key == 'a':
            '''x -= 10
            with open('components/position.txt', 'w+') as file:
                file.write(str(x)+':'+str(y))'''
            direc[0] += +1
            return direc
        return direc
