import pygame


class Resource:
    images = dict()
    sounds = dict()
    musics = dict()

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

    @classmethod
    def sound(cls, sound):
        return cls.sounds.get(sound)

    @classmethod
    def load_musics(cls, sounds):
        for sound, filename in sounds.items():
            cls.musics[sound] = pygame.mixer.music(filename)

    @classmethod
    def music(cls, music):
        return cls.musics.get(music)
