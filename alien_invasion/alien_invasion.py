import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一个play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一个存储游戏统计信息的实例，并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    #设置背景颜色
    bg_color = ai_settings.bg_color

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个用于存储子弹的编组
    bullets = Group()
    #创建一个用于存储外星人的编组
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个外星飞船
    alien = Alien(ai_settings,screen)

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            #更新飞船
            ship.update()
            #更新子弹
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            #更新外星飞船位置
            gf.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
        #重绘屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,bullets,aliens,play_button)


run_game()