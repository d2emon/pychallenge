import pygame


SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024
SCREEN_CAPTION = "Challenge 1"

STATE_QUIT = 0
STATE_RUN = 1

FPS = 30


class Game:
    def __init__(self, caption=SCREEN_CAPTION, size=(SCREEN_WIDTH, SCREEN_HEIGHT), fps=FPS):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)

        self.clock = pygame.time.Clock()
        self.state = STATE_RUN
        self.fps = fps

    def run(self):
        while self.state == STATE_RUN:
            self.clock.tick(self.fps)

            # Read events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            # Controlling keys
            keys = pygame.key.get_pressed()
            self.key_event(keys)

            if keys[pygame.K_ESCAPE]:
                self.quit()

            self.draw()

            pygame.display.update()

    def key_event(self, keys):
        pass

    def draw(self):
        # Background
        self.window.fill((0, 0, 0))

    def quit(self):
        self.state = STATE_QUIT


def main():
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()