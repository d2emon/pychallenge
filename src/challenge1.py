import pygame
import random

from game import Game
from mathgen import TwoPoint


WIDTH = 1024
HEIGHT = 1024

MAX_SIZE = 4
SPEED = 50
STARS = 2048
STAR_COLOR = (255, 255, 255)


def translate(x, y):
    x0 = WIDTH / 2
    y0 = HEIGHT / 2

    return int(x + x0), int(y + y0)


def map_value(percent, min_value=0, max_value=100):
    if min_value > max_value:
        percent = 1 - percent
        min_value, max_value = max_value, min_value
    return percent * (max_value - min_value) + min_value


class Star:
    def __init__(self):
        self.x, self.y = self.random_point()
        self.z = random.randrange(WIDTH)

    @classmethod
    def random_point(cls):
        x = random.randrange(-WIDTH, WIDTH)
        y = random.randrange(-HEIGHT, HEIGHT)
        return x, y

    def update(self, speed=1):
        self.z -= speed
        if self.z < 1:
            self.x, self.y = self.random_point()
            self.z = WIDTH

    def draw(self, window):
        x = int(map_value(self.x / self.z, max_value=WIDTH))
        y = int(map_value(self.y / self.z, max_value=HEIGHT))
        r = int(map_value(self.z / WIDTH, MAX_SIZE, 0))

        pygame.draw.circle(window, STAR_COLOR, translate(x, y), r)


class Starfield(Game):
    def __init__(self):
        super().__init__("Caustic", (WIDTH, HEIGHT))

        self.stars = [Star() for _ in range(STARS)]

    def draw(self):
        super().draw()

        for star in self.stars:
            star.update(SPEED)
            star.draw(self.window)


def main():
    game = Starfield()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
