import pygame
import time
import random

from game import Game, STATE_GAME_OVER
from resource import Resource


WIDTH = 512
HEIGHT = 512
CAPTION = "Tutorial"

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

MIN_X = 32
MAX_X = WIDTH - 32


class Thing:
    def __init__(self):
        self.x = random.randrange(WIDTH)
        self.y = -600
        self.width = 100
        self.height = 100

        self.speed = 8

        self.color = BLACK

        self.count = 0

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def reset(self):
        self.y = -self.height
        self.x = random.randrange(WIDTH)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.count += 1
            # self.speed += 1
            self.width += (self.count * 1.2)
            self.reset()


class Car:
    LEFT = 0
    RIGHT = 1

    SPEED = 5

    STATE_PLAY = 0
    STATE_GAME_OVER = STATE_GAME_OVER

    def __init__(self):
        self.image = Resource.image('car')
        self.x = WIDTH * .48
        self.y = HEIGHT * .8

        self.width = 73

        self.state = self.STATE_PLAY

    def move(self, direction):
        if direction == self.LEFT:
            self.x -= self.SPEED
        elif direction == self.RIGHT:
            self.x += self.SPEED

    def collision(self, thing):
        if self.x < MIN_X or self.x > MAX_X - self.width:
            return True

        if self.y >= thing.y + thing.height:
            return False
        if self.x + self.width < thing.x:
            return False
        return self.x < thing.x + thing.width

    def draw(self, window, x, y):
        window.blit(self.image, (x, y))

    def game_over(self):
        self.state = self.STATE_GAME_OVER


class Tutorial(Game):
    def __init__(self):
        super().__init__(CAPTION, (WIDTH, HEIGHT))
        self.fps = FPS
        self.bg_color = WHITE
        Resource.load({
            'car': "res/racecar.png",
        })

        self.car = Car()
        self.thing = Thing()

    def run(self):
        self.car = Car()
        self.thing = Thing()

        super().run()

    def key_event(self, keys):
        if keys[pygame.K_RIGHT]:
            self.car.move(self.car.RIGHT)
        if keys[pygame.K_LEFT]:
            self.car.move(self.car.LEFT)

    def draw(self):
        super().draw()

        self.thing.move()
        if self.car.collision(self.thing):
            self.car.game_over()

        self.car.draw(self.window, self.car.x, self.car.y)
        self.thing.draw(self.window)
        self.dodged(self.thing.count)

        if self.car.state == self.car.STATE_GAME_OVER:
            self.game_over()

    def game_over(self):
        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Game Over", pos, BLACK)

        super().game_over()

        time.sleep(2)
        self.run()

    def dodged(self, count):
        text = self.sys_font.render("Dodged: {}".format(count), True, BLACK)
        self.window.blit(text, (0, 0))


def main():
    game = Tutorial()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
