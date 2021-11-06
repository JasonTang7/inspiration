import unittest
from time import sleep
from selenium import webdriver
from functions import pczhpage,common,pczhpageElements

class TestSearch(unittest.TestCase):
    """YAMI PC中文站 主流程自动化测试"""
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        cls.pc_url = "https://www.yamibuy.com"
    
    def test_1search_key_word(self):
        """通过关键字搜索"""
        key_word = "螺蛳粉"
        common.getweb(self.driver,self.pc_url)
        sleep(2)
        pczhpage.search(self.driver,key_word)
        self.assertEqual(self.driver.title,key_word+" | 亚米")
        sleep(2)
    
    def test_2itemdetail(self):
        """跳转到商品详情页"""
        common.elementclick(self.driver,pczhpageElements.search_result_item)
        sleep(5)
        i = -1 #i表示切换到的窗口索引
        common.switchWindow(self.driver,i)
        type = 'data-scene'
        text = common.getattribute(self.driver,pczhpageElements.pdp_scene,type)
        #self.assertEqual(text,"item_detail")
        sleep(2)


    def test_3addcart(self):
        """详情页加购"""
        common.slideScroll(self.driver,pczhpageElements.item_addbutton)
        common.elementclick(self.driver,pczhpageElements.item_addbutton)
        sleep(2)
        verifyText = common.gettext(self.driver,pczhpageElements.item_addedText)
        self.assertEqual(verifyText,"商品已加入购物车")
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()