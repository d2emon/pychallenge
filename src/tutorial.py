import pygame
import time

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

    def turn(self, direction):
        if direction == self.LEFT:
            self.x -= self.SPEED
        elif direction == self.RIGHT:
            self.x += self.SPEED

        if self.x < MIN_X or self.x > MAX_X - self.width:
            self.state = self.STATE_GAME_OVER

    def draw(self, window, x, y):
        window.blit(self.image, (x, y))


class Tutorial(Game):
    def __init__(self):
        super().__init__(CAPTION, (WIDTH, HEIGHT))
        self.fps = FPS
        self.bg_color = WHITE
        Resource.load({
            'car': "res/racecar.png",
        })

        self.car = Car()

    def run(self):
        self.car = Car()
        super().run()

    def key_event(self, keys):
        if keys[pygame.K_RIGHT]:
            self.car.turn(self.car.RIGHT)
        if keys[pygame.K_LEFT]:
            self.car.turn(self.car.LEFT)

    def draw(self):
        super().draw()

        if self.car.state == self.car.STATE_GAME_OVER:
            self.game_over()

        self.car.draw(self.window, self.car.x, self.car.y)

    def game_over(self):
        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Game Over", pos, BLACK)

        super().game_over()

        time.sleep(2)
        self.run()


def main():
    game = Tutorial()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
