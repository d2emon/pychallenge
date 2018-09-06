import pygame
import random

from game import Game


WIDTH = 1024
HEIGHT = 1024

COLOR = (255, 255, 255)

def translate(x, y):
    x0 = WIDTH / 2
    y0 = HEIGHT / 2

    return int(x + x0), int(y + y0)


def map_value(percent, min_value=0, max_value=100):
    if min_value > max_value:
        percent = 1 - percent
        min_value, max_value = max_value, min_value
    return percent * (max_value - min_value) + min_value


def menger(window, width, pos=(0, 0)):
    if width <= 2:
        pygame.draw.circle(window, COLOR, pos, 1)
        return

    part = int(width / 3)
    for y in range(3):
        for x in range(3):
            if x == y == 1:
                continue
            menger(window, part, (pos[0] + part * x, pos[1] + part * y))


class Menger(Game):
    def __init__(self):
        super().__init__("Menger", (WIDTH, HEIGHT))

    def draw(self):
        super().draw()

        menger(self.window, WIDTH)


def main():
    game = Menger()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
