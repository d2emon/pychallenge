import pygame


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_CAPTION = "Game"

STATE_QUIT = 0
STATE_INTRO = 1
STATE_RUN = 2
STATE_GAME_OVER = 3

FPS = 30


class Button:
    def __init__(self):
        self.color = (0, 0, 0)
        self.hover_color = (0, 0, 0)
        self.rect = (0, 0, 100, 100)

        self.hover = False

        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.caption = ""
        self.text_color = (0, 0, 0)

    def draw(self, surface):
        pos = (
            self.rect[0] + (self.rect[2] / 2),
            self.rect[1] + (self.rect[3] / 2),
        )

        text_surface = self.font.render(self.caption, True, self.text_color)
        rect = text_surface.get_rect()
        rect.center = pos

        color = self.color
        if self.hover:
            color = self.hover_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(text_surface, rect)

    def collide(self, pos):
        if self.rect[0] < pos[0] < self.rect[0] + self.rect[2]:
            if self.rect[1] < pos[1] < self.rect[1] + self.rect[3]:
                return True
        return False

    def action(self):
        pass

    def mouse_event(self, pos, pressed):
        self.hover = self.collide(pos)
        if self.hover and pressed[0]:
            if self.action:
                self.action()


class Screen:
    def __init__(self, game, fps=FPS):
        self.game = game

        self.clock = pygame.time.Clock()
        self.fps = fps
        self.bg_color = (0, 0, 0)

        self.sys_font = pygame.font.SysFont(None, 25)
        self.large_text = pygame.font.Font('freesansbold.ttf', 50)

    def show(self):
        self.clock.tick(self.fps)

        # Read events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            self.events(event)

        # Controlling keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.quit()

        self.key_event(keys)
        self.mouse_event(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

        self.draw(self.game.window)

        pygame.display.update()
        # pygame.display.flip()

    def draw(self, window):
        window.fill(self.bg_color)

    def events(self, event):
        pass

    def key_event(self, keys):
        pass

    def mouse_event(self, pos, pressed):
        pass

    def start(self):
        self.game.state = STATE_RUN

    def quit(self):
        self.game.quit()

    def message(self, font, text, pos=(0, 0), color=(0, 0, 0)):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.center = pos
        self.game.window.blit(surface, rect)


class Game:
    def __init__(self, caption=SCREEN_CAPTION, size=(SCREEN_WIDTH, SCREEN_HEIGHT)):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.state = STATE_INTRO

        self.intro = Screen(self)
        self.main = Screen(self)

    def play(self):
        while self.state != STATE_QUIT:
            while self.state == STATE_INTRO:
                self.intro.show()
            while self.state == STATE_RUN:
                self.main.show()
            if self.state == STATE_GAME_OVER:
                self.state = STATE_RUN

    def quit(self):
        self.state = STATE_QUIT

    def game_over(self):
        self.state = STATE_GAME_OVER
        pygame.display.update()


def main():
    game = Game()
    game.play()
    pygame.quit()


if __name__ == "__main__":
    main()