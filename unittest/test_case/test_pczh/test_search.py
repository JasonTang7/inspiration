import unittest
from time import sleep
from selenium import webdriver
from functions import homepage

class TestSearch(unittest.TestCase):
    """YAMI PC中文站 搜索 自动化测试"""
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        cls.pc_url = "https://www.yamibuy.com"
    
    def test_search_key_word(self):
        """通过关键字搜索"""
        key_word = "螺蛳粉"
        homepage.search(self.driver,self.pc_url,key_word)
        self.assertEqual(self.driver.title,key_word+" | 亚米")
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()