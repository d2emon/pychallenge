import pygame
import random

from game import Game


WIDTH = 1024
HEIGHT = 1024

MAX_SIZE = 4
SPEED = 10
STARS = 4096
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
        self.z = random.randrange(1, 2 * WIDTH)
        self.pz = self.z

    @classmethod
    def random_point(cls):
        x = random.randrange(-WIDTH, WIDTH)
        y = random.randrange(-HEIGHT, HEIGHT)
        return x, y

    def update(self, speed=1):
        self.pz = self.z

        self.z -= speed
        if self.z < 1:
            self.x, self.y = self.random_point()
            self.z = 2 * WIDTH
            self.pz = self.z
        elif self.z > 2 * WIDTH:
            self.x, self.y = self.random_point()
            self.z = 1
            self.pz = self.z

    def draw(self, window):
        if self.z > WIDTH:
            return

        x = int(map_value(self.x / self.z, max_value=WIDTH))
        y = int(map_value(self.y / self.z, max_value=HEIGHT))
        r = int(map_value(self.z / WIDTH, MAX_SIZE, 0))

        pygame.draw.circle(window, STAR_COLOR, translate(x, y), r)

        px = int(map_value(self.x / self.pz, max_value=WIDTH))
        py = int(map_value(self.y / self.pz, max_value=HEIGHT))
        pygame.draw.line(window, STAR_COLOR, translate(px, py), translate(x, y))


class Starfield(Game):
    def __init__(self):
        super().__init__("Caustic", (WIDTH, HEIGHT))

        self.stars = [Star() for _ in range(STARS)]
        self.speed = SPEED

    def draw(self):
        super().draw()

        for star in self.stars:
            star.update(self.speed)
            star.draw(self.window)

    def key_event(self, keys):
        if keys[pygame.K_UP]:
            self.speed += 1
        if keys[pygame.K_DOWN]:
            self.speed -= 1
        if keys[pygame.K_SPACE]:
            self.speed = 0


def main():
    game = Starfield()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
