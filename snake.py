from config import Config

import random

class Snake():
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    HEAD = 0

    def __int__(self):
        self.x = random.randint(5, Config.CELLWIDTH - 6)
        self.y = random.randint(5, Config.CELLHEIGHT - 6)
        self.direction = self.RIGHT
        self.snakeCoords = [{'x': self.x, "y": self.y}, {'x': self.x - 1, 'y': self.y}, {'x': self.x - 2, 'y': self.y}]