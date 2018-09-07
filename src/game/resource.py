import pygame


class Resource:
    images = dict()

    @classmethod
    def load(cls, images):
        for image, filename in images.items():
            cls.images[image] = pygame.image.load(filename)

    @classmethod
    def image(cls, image):
        return cls.images.get(image)
