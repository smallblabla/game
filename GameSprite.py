import pygame

class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_url,speed):

        super().__init__()

        self.image = pygame.image.load(image_url)

        self.rect = self.image.get_rect()

        self.speed = speed


    def update(self):
        self.rect.y += self.speed

