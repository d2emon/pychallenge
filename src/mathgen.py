import random
import math


def decart(r, a):
    return r * math.cos(a), r * math.sin(a)


def middle(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    x = int((x1 + x2) / 2)
    y = int((y1 + y2) / 2)
    return x, y


def diffuse(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    p = random.randrange(100) / 100
    p = p / 2
    if random.randrange(2):
        p = -p
    p += .5

    return int(x1 + p * dx), int(y1 + p * dy)


class TwoPoint:
    def __init__(self, a1=None, a2=None):
        self.a1 = a1 or (random.randrange(1, 255), random.randrange(8))
        self.a2 = a2 or (random.randrange(1, 512), random.randrange(8))

        print(self.a1, self.a2)

    def calculate(self, t):
        p1 = decart(self.a1[0], self.a1[1] * t)
        p2 = decart(self.a2[0], self.a2[1] * t)
        return diffuse(p1, p2)

    def generate(self):
        t = random.randrange(1024)
        return self.calculate(t)

    def point(self):
        t = random.randrange(1000)
        p1 = decart(self.a1[0], self.a1[1] * t)
        p2 = decart(self.a2[0], self.a2[1] * t)
        return diffuse(p1, p2)
