import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color = ai_setting.bg_color

    #创建一艘飞船
    ship = Ship(ai_setting,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_setting,screen,ship,bullets)
        #更新飞船
        ship.update()
        #更新子弹
        gf.update_bullets(bullets)
        #重绘屏幕
        gf.update_screen(ai_setting,screen,ship,bullets)


run_game()