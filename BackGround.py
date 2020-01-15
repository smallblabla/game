import pygame
from GameSprite import *
from Tool import *

class BackGround(GameSprite):

    def update(self):
        #调用父类方法实现
        super().update()

        #如果背景图片滚出窗口，则将其位置调整
        if self.rect.y >= WINDOW_HEIGHT:
            self.rect.y = -WINDOW_HEIGHT
            self.rect.y = -WINDOW_HEIGHT