import pygame
import time
import random

from game.game import Game, Screen, Button, STATE_GAME_OVER, STATE_RUN
from game.resource import Resource


WIDTH = 512
HEIGHT = 512
CAPTION = "Tutorial"

FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (128, 0, 0)
GREEN = (0, 128, 0)
BLUE = (0, 0, 255)

BRIGHT_GREEN = (0, 255, 0)
BRIGHT_RED = (255, 0, 0)

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


class GreenButton(Button):
    def __init__(self, game):
        super().__init__()
        self.rect = (50, HEIGHT - 100, 100, 50)
        self.caption = "GO!"

        self.hover_color = BRIGHT_GREEN
        self.color = GREEN


class RedButton(Button):
    def __init__(self, game):
        super().__init__()
        self.rect = (WIDTH - 150, HEIGHT - 100, 100, 50)
        self.caption = "Quit"

        self.hover_color = BRIGHT_RED
        self.color = RED


class Intro(Screen):
    def __init__(self, game):
        super().__init__(game, 15)
        self.bg_color = WHITE

        green_button = GreenButton(self.game)
        green_button.action = self.start

        red_button = RedButton(self.game)
        red_button.action = self.quit

        self.buttons = [
            green_button,
            red_button,
        ]

    def draw(self, window):
        super().draw(window)

        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Race", pos, BLACK)

        for button in self.buttons:
            button.draw(window)

    def mouse_event(self, pos, pressed):
        for button in self.buttons:
            button.mouse_event(pos, pressed)


class MainScreen(Screen):
    def __init__(self, game):
        super().__init__(game, FPS)
        self.bg_color = WHITE

        self.car = Car()
        self.thing = Thing()

        self.start()

    def start(self):
        self.car = Car()
        self.thing = Thing()

    def draw(self, window):
        super().draw(window)

        self.thing.move()
        if self.car.collision(self.thing):
            self.car.game_over()

        self.car.draw(window, self.car.x, self.car.y)
        self.thing.draw(window)

        self.dodged(self.thing.count)

        if self.car.state == self.car.STATE_GAME_OVER:
            self.game_over()

    def key_event(self, keys):
        if keys[pygame.K_RIGHT]:
            self.car.move(self.car.RIGHT)
        if keys[pygame.K_LEFT]:
            self.car.move(self.car.LEFT)

    def game_over(self):
        pos = WIDTH / 2, HEIGHT / 2
        self.message(self.large_text, "Game Over", pos, BLACK)

        self.game.game_over()

    def dodged(self, count):
        text = self.sys_font.render("Dodged: {}".format(count), True, BLACK)
        self.game.window.blit(text, (0, 0))


class Tutorial(Game):
    def __init__(self):
        super().__init__(CAPTION, (WIDTH, HEIGHT))
        Resource.load({
            'car': "res/racecar.png",
        })

        self.intro = Intro(self)
        self.main = MainScreen(self)

    def game_over(self):
        super().game_over()
        time.sleep(2)

        self.main = MainScreen(self)
        self.state == STATE_RUN


class TutorialScreen(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.bg_color = BLACK

    def draw(self, window):
        super().draw(window)

        pixels = pygame.PixelArray(window)

        import math
        for t in range(255):
            t1 = t / 20
            x1 = int(50 * math.cos(t1) + 255)
            y1 = int(50 * math.sin(t1) + 255)
            pixels[x1][y1] = (255, 128, 128)

            t2 = t / 10
            x2 = int(100 * math.cos(t2) + 255)
            y2 = int(100 * math.sin(t2) + 255)
            pixels[x2][y2] = (128, 128, 255)

            pygame.draw.line(window, (255, 255, 255), (x1, y1), (x2, y2))

        pixels[10][20] = GREEN
        pixels[10][30] = RED
        pixels[10][40] = BLUE

        pygame.draw.line(window, BLUE, (100, 200), (300, 450), 5)
        pygame.draw.rect(window, RED, (400, 400, 50, 25))
        pygame.draw.circle(window, GREEN, (150, 150), 75)
        pygame.draw.polygon(window, WHITE, ((25, 75), (76, 125), (250, 375)))


def main():
    game = Tutorial()
    game.play()
    pygame.quit()


if __name__ == "__main__":
    main()
