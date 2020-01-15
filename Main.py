import pygame
import time
from  Tool import *
from  Hero import *
from  BackGround import *
from  SafetyBlock import *
from NoneBlock import *
from JumpBlock import *
from LoseBlock import *
from Blood import *
from Prop_1 import *
from Prop_2 import *
from Prop_3 import *


class MainGame():

    def __init__(self):
        self.Time = 0
        self.safetyblock_num =  0
        self.score = 0
        self.time1 = self.getNowTimeString()
        self.time2 = 0
        self.blood_num = 3
        pygame.init()
        print("游戏初始化成功")
        #1.创建游戏窗口
        self.screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.start_screen = pygame.Surface(self.screen.get_size())
        #2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        #3.创建精灵与精灵组
        self.__creat_sprites()
        #4.设置定时器事件 - 创建木块 , 设置
        pygame.time.set_timer(CREAT_SAFETY_EVENT,create_safety_time)
        pygame.time.set_timer(CREAT_PROP_EVENT,create_prop_time)
        pygame.time.set_timer(CREAT_OTHER_EVENT,create_other_time)

    #创建精灵
    def __creat_sprites(self):
        #创建背景精灵，创建背景精灵组
        bg_1 = BackGround(bg_img_1,1)
        bg_2 = BackGround(bg_img_2,1)
        bg_2.rect.y = -WINDOW_HEIGHT
        self.bg_ground = pygame.sprite.Group(bg_1,bg_2)
        #创建英雄精灵，创建英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        #创建安全木块精灵组
        self.safetyblock = SafetyBlock()
        self.safetyblock_group = pygame.sprite.Group()
        #创建消失木块精灵组
        self.noneblock = NoneBlock()
        self.noneblock_group = pygame.sprite.Group()
        #创建跳跃木块精灵组
        self.jumpblock = JumpBlock()
        self.junpblock_group = pygame.sprite.Group()
        # 创建掉血木块精灵组
        self.loseblock = LoseBlock()
        self.loseblock_group = pygame.sprite.Group()
        # 创建道具精灵组
        self.prop_1 = Prop_1()
        self.prop_1_group = pygame.sprite.Group()
        # 创建道具精灵组
        self.prop_2 = Prop_2()
        self.prop_2_group = pygame.sprite.Group()
        # 创建道具精灵组
        self.prop_3 = Prop_3()
        self.prop_3_group = pygame.sprite.Group()

    #事件监听
    def __event_handler(self):
        #将英雄初始x速度设为，防止按键后持续移动
        self.hero.speed = 0
        #得到按键事件列表
        keys = pygame.key.get_pressed()
        #事件循环判断
        for event in pygame.event.get():
            #如果点击退出
            if event.type == pygame.QUIT:
                MainGame.game_over()

            if event.type == CREAT_OTHER_EVENT:
                i = random.randint(1,8)
                if i == 1:
                    self.noneblock = NoneBlock()
                    self.noneblock_group.add(self.noneblock)
                if i == 2 or i == 8:
                    self.jumpblock = JumpBlock()
                    self.junpblock_group.add(self.jumpblock)
                    self.safetyblock_num += 1
                if i == 3 or i == 7:
                    self.loseblock = LoseBlock()
                    self.loseblock_group.add(self.loseblock)
                if i == 4 or i == 5 or i == 6:
                    self.safetyblock_num += 1
                    self.safetyblock = SafetyBlock()
                    self.safetyblock_group.add(self.safetyblock)

            if event.type == CREAT_PROP_EVENT:
                j = random.randint(1,7)
                if j == 1:
                    self.prop_1 = Prop_1()
                    self.prop_1_group.add(self.prop_1)
                if j == 2 or j == 4 or j == 6:
                    self.prop_2 = Prop_2()
                    self.prop_2_group.add(self.prop_2)
                if j == 3 or j == 5 or j == 7:
                    self.prop_3 = Prop_3()
                    self.prop_3_group.add(self.prop_3)

        #如果按键列表中有按左
        if keys[pygame.K_RIGHT]:
            self.hero.speed = 5
            self.hero.image = pygame.image.load(hero_right_img)
        #如果按键列表中有按右
        elif keys[pygame.K_LEFT]:
            self.hero.speed = -5
            self.hero.image = pygame.image.load(hero_left_img)


    #碰撞检测
    def __check_collide(self):
        safety_events = pygame.sprite.spritecollide(self.hero,self.safetyblock_group,False)
        #如果列表有值
        for event in safety_events:
            if self.hero.rect.y > event.rect.y - event.rect.height:
                if self.hero.rect.x > event.rect.x and self.hero.rect.x < event.rect.x + event.rect.width:
                    self.hero.rect.x = event.rect.x + event.rect.width

                if self.hero.rect.x <event.rect.x and self.hero.rect.x > event.rect.x - event.rect.width:
                    self.hero.rect.x = event.rect.x - event.rect.width
            elif self.hero.rect.y - self.hero.rect.height < event.rect.y and self.hero.rect.y - self.hero.rect.height > event.rect.y - event.rect.height:
                self.hero.rect.y = event.rect.y + self.hero.rect.height
            else:
                self.hero.rect.y -= 5
            #英雄与消失木块相碰
        #消失版
        none_events = pygame.sprite.spritecollide(self.hero,self.noneblock_group,False)
        for event in none_events:
            if self.hero.rect.y > event.rect.y - event.rect.height:
                if self.hero.rect.x > event.rect.x and self.hero.rect.x < event.rect.x + event.rect.width:
                    self.hero.rect.x = event.rect.x + event.rect.width

                if self.hero.rect.x <event.rect.x and self.hero.rect.x > event.rect.x - event.rect.width:
                    self.hero.rect.x = event.rect.x - event.rect.width
            elif self.hero.rect.y - self.hero.rect.height < event.rect.y and self.hero.rect.y - self.hero.rect.height > event.rect.y - event.rect.height:
                self.hero.rect.y = event.rect.y + self.hero.rect.height
            else:
                self.noneblock_group.remove(event)
        #跳板
        jump_events = pygame.sprite.spritecollide(self.hero,self.junpblock_group,False)
        for event in jump_events:
            if self.hero.rect.y > event.rect.y - event.rect.height:
                if self.hero.rect.x > event.rect.x and self.hero.rect.x < event.rect.x + event.rect.width:
                    self.hero.rect.x = event.rect.x + event.rect.width

                if self.hero.rect.x <event.rect.x and self.hero.rect.x > event.rect.x - event.rect.width:
                    self.hero.rect.x = event.rect.x - event.rect.width
            elif self.hero.rect.y - self.hero.rect.height < event.rect.y and self.hero.rect.y - self.hero.rect.height > event.rect.y - event.rect.height:
                self.hero.rect.y = event.rect.y + self.hero.rect.height
            else:
                self.hero.rect.y -= 80
        #掉血版
        lose_events = pygame.sprite.spritecollide(self.hero,self.loseblock_group,False)
        for event in lose_events:
            if self.hero.rect.y > event.rect.y - event.rect.height:
                if self.hero.rect.x > event.rect.x and self.hero.rect.x < event.rect.x + event.rect.width:
                    self.hero.rect.x = event.rect.x + event.rect.width

                if self.hero.rect.x < event.rect.x and self.hero.rect.x > event.rect.x - event.rect.width:
                    self.hero.rect.x = event.rect.x - event.rect.width
            elif self.hero.rect.y - self.hero.rect.height < event.rect.y and self.hero.rect.y - self.hero.rect.height > event.rect.y - event.rect.height:
                self.hero.rect.y = event.rect.y + self.hero.rect.height
            else:
                self.blood_num -= 1
                self.loseblock_group.remove(event)
        #加血
        prop_1_events = pygame.sprite.spritecollide(self.hero,self.prop_1_group,True)
        if len(prop_1_events) > 0:
            if self.blood_num < 3:
                self.blood_num += 1
        #左右瞬移
        prop_2_events = pygame.sprite.spritecollide(self.hero,self.prop_2_group,True)
        if len(prop_2_events) > 0:
            _x = random.randint(-400,400)
            self.hero.rect.x += _x
            self.score += 1
            print(self.score)
        #上下瞬移
        prop_3_events = pygame.sprite.spritecollide(self.hero, self.prop_3_group, True)
        if len(prop_3_events) > 0:
            _y = random.randint(-300,300)
            self.hero.rect.y += _y
            self.score += 1
            print(self.score)
    #更新精灵组，显示位置

    def __update_sprites(self):
        if self.blood_num == 3:
            blood = Blood(blood_3)
        if self.blood_num == 2:
            blood = Blood(blood_2)
        if self.blood_num == 1:
            blood = Blood(blood_1)
        if self.blood_num == 0:
            blood = Blood(blood_0)
        self.blood_group = pygame.sprite.Group(blood)
        #血条
        self.blood_group.update()
        self.bg_ground.draw(self.screen)
        #加载屏幕精灵组
        self.bg_ground.update()
        self.bg_ground.draw(self.screen)
        #加载英雄精灵组
        if self.safetyblock_num >= 1:
            self.hero_group.update()
            self.hero_group.draw(self.screen)
        #加载安全木块精灵组
        self.safetyblock_group.update()
        self.safetyblock_group.draw(self.screen)
        # 加载消失木块精灵组
        self.noneblock_group.update()
        self.noneblock_group.draw(self.screen)

        self.junpblock_group.update()
        self.junpblock_group.draw(self.screen)

        self.loseblock_group.update()
        self.loseblock_group.draw(self.screen)

        self.blood_group.update()
        self.blood_group.draw(self.screen)

        self.prop_1_group.update()
        self.prop_1_group.draw(self.screen)

        self.prop_2_group.update()
        self.prop_2_group.draw(self.screen)

        self.prop_3_group.update()
        self.prop_3_group.draw(self.screen)

    #结束游戏

    def start_game(self):
        print("游戏开始")
        music_start()
        #调用函数
        font = pygame.font.SysFont('microsoft Yahei', 60)
        while True:
            #1.设置帧率
            self.clock.tick(60)
            #2.事件监听
            self.__event_handler()
            #3.碰撞检测
            self.__check_collide()
            #4.更新/绘制精灵组
            self.__update_sprites()
            #5.更新显示
            self.screen.blit(self.count_time(), (0, 0))
            self.screen.blit(self.count_score(), (220, 0))
            if self.blood_num == 0 or self.hero.game_over == True:
                self.game_over(self.screen)
            pygame.display.flip()
            pygame.display.update()



    @staticmethod
    def game_over(screen):
         print("游戏结束")
         music_over()
         image = pygame.image.load("img/game_over.png")
         screen.blit(image, (140, 400))
         pygame.display.flip()
         time.sleep(3)
         pygame.quit()
         exit()

    def getNowTimeString(self):
        now = time.time()
        return now

    def count_time(self):
        font = pygame.font.SysFont('microsoft Yahei', 60)
        self.time2 = int(self.getNowTimeString()) - int(self.time1)
        surface = font.render("Time:%d"%(self.time2), False, (221,0,27))
        return surface

    def count_score(self):
        font = pygame.font.SysFont('幼圆', 40)
        surface = font.render("score:%d"%(self.score * 5 + self.time2 * 10), False, (127,186,0))
        return surface
    
def show_stear():
    ck = pygame.display.set_mode((640,900))   #  游戏窗口
    pygame.display.set_caption("是男人就下一百层")    #  给窗口取个名 我小时候喜欢双截龙和拳皇
    clock = pygame.time.Clock()                         #  游戏刷新速度（我个人这么理解）
    start_ck = pygame.Surface(ck.get_size())    #   充当开始界面的画布
    start_ck2 = pygame.Surface(ck.get_size())  #  充当第一关的画布界面暂时占位（可以理解为游戏开始了）
    start_ck = start_ck.convert()#修改图像（Surface 对象）的像素格式
    start_ck2 = start_ck2.convert()#修改图像（Surface 对象）的像素格式
    #start_ck.fill((255,255,255))  # 白色画布1（开始界面用的）使用纯色填充 对象
    #start_ck2.fill((0,255,0))
    background = pygame.image.load('bg.jpg')  # 图片路径/位置
    start_ck.blit(background, (0, 0))  # 对齐的坐标

    # 加载各个素材图片 并且赋予变量名
    i1 = pygame.image.load("s1.png") #开始游戏
    i1.convert()
    i11 = pygame.image.load("s2.png")
    i11.convert()

    i2 = pygame.image.load("n1.png") #结束游戏
    i2.convert()
    i21 = pygame.image.load("n2.png")
    i21.convert()

    i3 = pygame.image.load('m1.png') #选项
    i3.convert()
    i31 = pygame.image.load('m2.png')
    i31.convert()

    bg = pygame.image.load('bg_1.jpg')#背景图
    bg.convert()

    bg3 = pygame.image.load('bg3.jpg')#背景图
    bg3.convert()
    start_ck.blit(bg3, (0, 0))






    #  以下为选择开始界面鼠标检测结构。
    n1 = True
    while n1:
        clock.tick(30) # 每秒循环30次
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= 227 and x1 <= 555 and y1 >= 501 and y1 <=567:
            start_ck.blit(i11, (200, 480))#开始游戏
            if buttons[0]:
                n1 = False

        elif x1 >= 227 and x1 <= 555 and y1 >= 621 and y1 <=687:
            start_ck.blit(i21, (200, 600))#结束游戏
            if buttons[0]:
                pygame.quit()
                exit()

        # elif x1 >= 227 and x1 <= 555 and y1 >= 501 and y1 <=567:
        #     start_ck.blit(i31, (200, 480))#游戏说明
        #     if buttons[0]:
        #         start_ck.blit(bg3, (0, 240))#游戏说明图片
            
            
        else:
            start_ck.blit(i1, (200, 480))
            start_ck.blit(i2, (200, 600))
            # start_ck.blit(i3, (200, 480))


        ck.blit(start_ck,(0,0))
        pygame.display.update()


        # 下面是监听退出动作

        # 监听事件
        for event in pygame.event.get():    #用户点×

            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")

               # quit 卸载所有的模块
                pygame.quit()

                # exit() 直接终止当前正在执行的程序
                exit()


    ck.blit(start_ck2,(0,0))
    pygame.display.update()

    #  以下可以写第一关的代码了
    n2 = True
    while n2:
        clock.tick(30)
        ck.blit(start_ck2, (0, 0))
        start_ck2.blit(bg,(0,0))
        pygame.display.update()
        MainGame().start_game()
        for event in pygame.event.get():

            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")

                # quit 卸载所有的模块
                pygame.quit()

                # exit() 直接终止当前正在执行的程序
                exit()
                
if __name__ == '__main__':
    #MainGame().start_game()
    show_stear()


