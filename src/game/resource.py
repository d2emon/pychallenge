import pygame


class Resource:
    images = dict()
    sounds = dict()

    @classmethod
    def load_images(cls, images):
        for image, filename in images.items():
            cls.images[image] = pygame.image.load(filename)

    @classmethod
    def image(cls, image):
        return cls.images.get(image)

    @classmethod
    def load_sounds(cls, sounds):
        for sound, filename in sounds.items():
            cls.sounds[sound] = pygame.mixer.Sound(filename)
            # cls.sounds[sound] = pygame.mixer.music(filename)
