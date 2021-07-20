import sys

import pygame

from settings import Settings

def run_game():
    #初始化游戏，并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #设置背景颜色
    bg_color = ai_setting.bg_color

    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.quit:
                sys.exit()
        
        #每次循环时都重绘屏幕
        screen.fill(bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()