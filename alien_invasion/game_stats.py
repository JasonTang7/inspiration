from game_functions import fire_bullet


class GameStats():
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #在游戏启动时处于非活跃状态
        self.game_active = False
        #在任何情况下都不应重置最高得分
        with open('alien_invasion/files/high_score.txt') as file_object:
            self.high_score = int(file_object.read())
    
    def reset_stats(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
