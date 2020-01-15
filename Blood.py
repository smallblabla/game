import pygame
from Tool import *

class Blood(pygame.sprite.Sprite):

    def __init__(self,image_url,speed=0):

        super().__init__()

        self.image = pygame.image.load(image_url)

        self.rect = self.image.get_rect()

        self.speed = speed

        self.rect.x = WINDOW_WIDTH - self.rect.width
        self.rect.y = 0


    def update(self):
        self.rect.y += self.speed