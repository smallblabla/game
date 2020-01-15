#工具类
import pygame
import time

WINDOW_WIDTH = 640 #窗口宽度
WINDOW_HEIGHT = 900 #窗口高低

bg_img_1 = "img/bg_1.jpg" #背景图片
bg_img_2 = "img/bg_2.jpg"
hero_img = "img/hero.png" #英雄人物图片
hero_right_img = "img/hero_right.png"
hero_left_img = "img/hero_left.png"
safaty_block_img = "img/safety.png"  #安全木块图片
none_block_img = "img/none.png"
jump_clock_img = "img/jump.png"

lose_blood_block_img = "img/lose.png"
blood_0 = "img/blood_0.jpg"
blood_1 = "img/blood_1.jpg"
blood_2 = "img/blood_2.jpg"
blood_3 = "img/blood_3.jpg"

prop_1 = "img/prop_1.png"
prop_2 = "img/prop_2.png"
prop_3 = "img/prop_3.png"



hero_first_x = 400 #英雄初始x位置
hero_first_y = 100 #英雄初始y位置


create_safety_time = 3000#创建安全木块间隔事件
create_prop_time = 1000#创建消失木块间隔事件
create_other_time = 3500#创建消失木块间隔事件
#创建定时器常量
CREAT_SAFETY_EVENT = pygame.USEREVENT
CREAT_OTHER_EVENT = pygame.USEREVENT+1
CREAT_PROP_EVENT = pygame.USEREVENT+2
# CREAT_JUMP_EVENT = pygame.USEREVENT


def music_start():
    pygame.mixer.init()
    # 加载音乐文件
    track = pygame.mixer.music.load("music/bg_game.mp3")
    # 开始播放音乐流
    pygame.mixer.music.play(5)

def music_over():
    pygame.mixer.music.load("music/game_over.wav")
    # 开始播放音乐流
    pygame.mixer.music.play()

