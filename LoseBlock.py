import pygame
import random
from GameSprite import *
from Tool import *

class LoseBlock(GameSprite):

    def __init__(self):

        #调用父类方法，创建安全木块，指定图片
        super().__init__(lose_blood_block_img,1)
        self.rect.y = WINDOW_HEIGHT
        #指定木块随机位置
        self.rect.x = random.randint(0,WINDOW_WIDTH-self.rect.width)

    def update(self):
        #设置自动移动
        self.rect.y -= self.speed
        #判断是否废除屏幕，飞出则删除
        if self.rect.y == 0:
            print("飞出")
            self.kill()

    def __del__(self):
        print("飞出销毁")