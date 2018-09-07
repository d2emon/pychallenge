import pygame


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_CAPTION = "Game"

STATE_QUIT = 0
STATE_RUN = 1
STATE_GAME_OVER = 2

FPS = 30


class Game:
    def __init__(self, caption=SCREEN_CAPTION, size=(SCREEN_WIDTH, SCREEN_HEIGHT), fps=FPS):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.bg_color = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.fps = fps

        self.sys_font = pygame.font.SysFont(None, 25)
        self.large_text = pygame.font.Font('freesansbold.ttf', 50)

        self.state = STATE_RUN

    def run(self):
        self.state = STATE_RUN
        while self.state == STATE_RUN:
            self.clock.tick(self.fps)

            # Read events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

                self.events(event)

            # Controlling keys
            keys = pygame.key.get_pressed()
            self.key_event(keys)

            if keys[pygame.K_ESCAPE]:
                self.quit()

            self.draw()

            pygame.display.update()
            # pygame.display.flip()

    def events(self, event):
        pass

    def key_event(self, keys):
        pass

    def draw(self):
        self.window.fill(self.bg_color)

    def quit(self):
        self.state = STATE_QUIT

    def game_over(self):
        self.state = STATE_GAME_OVER
        pygame.display.update()

    def message(self, font, text, pos=(0, 0), color=(0, 0, 0)):
        surface = font.render(text, True, color)
        rect = surface.get_rect()
        rect.center = pos
        self.window.blit(surface, rect)


def main():
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()