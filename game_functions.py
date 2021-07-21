import sys

import pygame
from settings import Settings
from ship import Ship

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.type == pygame.K_LEFT:
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.type == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(ai_setting,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()