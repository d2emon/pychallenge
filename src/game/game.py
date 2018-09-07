import pygame


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_CAPTION = "Game"

STATE_QUIT = 0
STATE_INTRO = 1
STATE_RUN = 2
STATE_PAUSED = 3
STATE_GAME_OVER = 4

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

        self.buttons = []

    def after(self):
        pass

    def show(self):
        self.clock.tick(self.fps)

        # Read events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.state = STATE_QUIT
            self.events(event)

        # Controlling keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.state = STATE_QUIT

        self.key_event(keys)
        self.mouse_event(pygame.mouse.get_pos(), pygame.mouse.get_pressed())

        self.draw(self.game.window)

        pygame.display.update()
        # pygame.display.flip()

        self.after()

    def draw(self, window):
        if self.bg_color:
            window.fill(self.bg_color)

    def events(self, event):
        pass

    def key_event(self, keys):
        pass

    def mouse_event(self, pos, pressed):
        for button in self.buttons:
            button.mouse_event(pos, pressed)

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

        self.intro_screen = Screen(self)
        self.main_screen = Screen(self)
        self.pause_screen = Screen(self)
        self.game_over_screen = Screen(self)

    def play(self):
        while self.state != STATE_QUIT:
            while self.state == STATE_INTRO:
                self.intro_screen.show()
            while self.state == STATE_RUN:
                self.main_screen.show()
            while self.state == STATE_PAUSED:
                self.pause_screen.show()
            while self.state == STATE_GAME_OVER:
                self.game_over_screen.show()


def main():
    game = Game()
    game.play()
    pygame.quit()


if __name__ == "__main__":
    main()