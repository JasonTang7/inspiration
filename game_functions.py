from button import Button
import sys
from time import sleep

import pygame
from pygame.constants import SCRAP_TEXT
from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            write_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏动态设置
        ai_settings.initialize_dynamic_settings()
        #隐藏光标
        pygame.mouse.set_visible(False)
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        #重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        reset_game_content(ai_settings,screen,ship,aliens,bullets)

def check_keydown_events(event,ai_settings,screen,stats,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,stats,ship,bullets)
    elif event.key == pygame.K_q:
        write_high_score(stats)
        sys.exit()
        

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_setting,screen,stats,sb,ship,bullets,aliens,play_button):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #显示得分
    sb.show_score()
    #如果游戏处于非活动状态，则绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    #让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    #更新子弹的位置
    bullets.update()
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0 :
            bullets.remove(bullet)
    #print(len(bullets))
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应子弹和外星飞船的碰撞"""
    #检查是否有子弹击中了外星飞船，如果有就删除相应的子弹和外星飞船;第一个true管删除子弹，第二个true管删除外星飞船
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        #删除现在的子弹，加快游戏节奏，并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        #提高等级
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)

def check_high_score(stats,sb):
    """检查最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def fire_bullet(ai_settings,screen,stats,ship,bullets):
    """如果还没有到达子弹数量限制，就发射一颗子弹"""
    #创建新子弹，并将其加入到编组bullets中
    if stats.game_active and len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings,screen,ship,aliens):
    """创建外星人舰队"""
    #创建一个外星飞船,并计算每行可容纳多少外星飞船
    #外星飞船间距为外星飞船宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建外星人群
    for row_number in range(number_rows):
        #创建第一行外星人
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可以容纳多少个外星飞船"""
    #决定了一行可以有多少个飞船
    avaliable_space_X = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(avaliable_space_X / (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星飞船并将其放入当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 10 + (alien.rect.height + ai_settings.alien_row_pitch)*row_number
    aliens.add(alien)

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可以容纳多少行外星飞船"""
    avaliable_space_y = (ai_settings.screen_height - (3*alien_height) - ship_height)
    number_rows = int(avaliable_space_y / (2*alien_height))
    return number_rows

def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """检查是否有外星飞船处于屏幕边缘，并更新外星舰队中所有外星飞船的位置"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #检测外星飞船和玩家飞船的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)
        

def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """响应外星人碰撞了飞船"""
    if stats.ships_left > 1:
        #将ships_left减1
        stats.ships_left -= 1
        #更新记分牌
        sb.prep_ships()
        #清空外星人列表和子弹列表
        reset_game_content(ai_settings,screen,ship,aliens,bullets)
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_edges(ai_settings,aliens):
    """有外星飞船到达便于时调用下移并转向的函数"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """将外星舰队下移，并改变他们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """检查是否有外星人到达低端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船被撞一样处理
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break

def reset_game_content(ai_settings,screen,ship,aliens,bullets):
        #清空外星人和子弹的列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人，并将飞船放到屏幕低端中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def write_high_score(stats):
        with open('files/high_score.txt','w') as file_object:
            file_object.write(str(stats.high_score))