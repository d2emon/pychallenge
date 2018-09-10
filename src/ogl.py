import random
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from game.game import Game3D

CAPTION = "OpenGL"
WIDTH = 800
HEIGHT = 600


class Ground:
    vertices = (
        (-10, -.1, 20),
        (10, -.1, 20),
        (-10, -.1, -300),
        (10, -.1, -300),
    )
    color = (0, .5, .5)

    def draw(self):
        # glBegin(GL_LINES)
        glBegin(GL_QUADS)

        for vertex in self.vertices:
            glColor3fv(self.color)
            glVertex3fv(vertex)
        glEnd()


class Cube:
    base_vertices = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1),
    )
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7),
    )

    surfaces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6),
    )
    colors = (
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 0),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 0),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1),
        (0, 0, 0),
        (1, 1, 0),
        (1, 0, 1),
        (0, 1, 1),
        (1, 1, 1),
    )

    def __init__(self, z=0, max_distance=50):
        dx = random.randrange(-10, 10)
        dy = random.randrange(-10, 10)
        dz = z - random.randrange(20, max_distance)

        self.vertices = []
        for x, y, z in self.base_vertices:
            self.vertices.append((
                x + dx,
                y + dy,
                z + dz,
            ))

    def draw(self):
        # glBegin(GL_LINES)
        glBegin(GL_QUADS)

        for surface in self.surfaces:
            c = 0
            for vertex in surface:
                c += 1
                glColor3fv(self.colors[c])
                # glColor3fv(random.choice(self.colors))
                glVertex3fv(self.vertices[vertex])

        glEnd()


class Tutorial(Game3D):
    def __init__(self):
        super().__init__(CAPTION, (WIDTH, HEIGHT))

        self.cubes = []

        # Resource.load_images({
        #     'icon': "res/racecar.png",
        #     'car': "res/racecar.png",
        # })
        # pygame.display.set_icon(Resource.image('icon'))

        # self.intro_screen = Intro(self)
        # self.main_screen = MainScreen(self)
        # self.pause_screen = Pause(self)
        # self.game_over_screen = Crash(self)

        gluPerspective(45, (WIDTH/HEIGHT), .1, 50.0)

        self.ground = Ground()
        self.last = 0
        self.restart()
        glRotatef(0, 0, 0, 0)

    def restart(self, z=0):
        self.last -= 50
        self.cubes = [Cube(z) for _ in range(16)]
        glTranslatef(.0, .0, -15.0)

    def draw(self):
        super().draw()

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        if (self.last < camera_x < self.last - 2) and (self.last < camera_y < self.last - 2) and (self.last < camera_z < self.last - 2):
            print("CRASH", (camera_x, camera_y, camera_y))
        if camera_z < self.last:
            print("Avoided", camera_z)
            # glTranslatef(-camera_x, -camera_y, -camera_z)
            self.restart(camera_z)

        glTranslatef(.0, .0, .05)

        # glRotatef(1, 3, 1, 1)

        self.ground.draw()
        for cube in self.cubes:
            cube.draw()

    def events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(.0, .0, .5)
            if event.button == 5:
                glTranslatef(.0, .0, -.5)

    def key_event(self, keys):
        if keys[pygame.K_RIGHT]:
            # glRotatef(1, 0, 1, 0)
            glTranslatef(.25, .0, .0)
        if keys[pygame.K_LEFT]:
            # glRotatef(1, 0, -1, 0)
            glTranslatef(-.25, .0, .0)
        if keys[pygame.K_UP]:
            # glRotatef(1, 1, 0, 0)
            glTranslatef(.0, -.25, .0)
        if keys[pygame.K_DOWN]:
            # glRotatef(1, -1, 0, 0)
            glTranslatef(.0, .25, .0)


def main():
    game = Tutorial()
    game.play()
    pygame.quit()


if __name__ == "__main__":
    main()
