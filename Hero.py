from GameSprite import *
from Tool import *
from Main import *
from SafetyBlock import *

class Hero(GameSprite):

    def __init__(self):

        #调用父级初始化方法
        super().__init__(hero_img,0)
        #定义初始位置
        self.rect.x = hero_first_x
        self.rect.y = hero_first_y
        self.game_over = False

    def update(self):
        #英雄在y方向的速度
        speed_y = 4
        self.rect.y += speed_y
        #英雄在x方向的速度
        self.rect.x += self.speed

        #判断是否触碰上下边界
        if self.rect.y < 0 or self.rect.y > WINDOW_HEIGHT:
            self.game_over = True

        #判断是否触碰左右边界
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WINDOW_WIDTH-self.rect.width:
            self.rect.x = WINDOW_WIDTH-self.rect.width

