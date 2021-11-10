import time
import unittest
from time import sleep
from unittest.case import skip
from selenium import webdriver
from selenium.webdriver.common.by import By
from functions import pczhpage,common,pczhpageElements
import config
import requests
import json


class TestSearch(unittest.TestCase):
    """YAMI PC中文站 主流程自动化测试"""
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Chrome()
        cls.pc_url = "https://www.yamibuy.com"
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    #def setUp(self):
    #    try:
    #        if self.runNo == 3:
    #            print("重试次数已达到阈值：%s次，进行下个用例的测试" %self.runNo)
    #            raise RuntimeError('用例执行失败')
    #   except RuntimeError:
    #       raise AssertionError
    
    def test_1search_key_word(self):
        """通过关键字搜索"""
        self.driver.implicitly_wait(10)
        key_word = "螺蛳粉"
        common.getweb(self.driver,self.pc_url)
        #sleep(2)
        try:
            monetate_icon = self.driver.find_element(By.XPATH,pczhpageElements.monetate_icon)
        except:
            monetate_icon =""
        if monetate_icon:
            common.elementclick(self.driver,pczhpageElements.monetate_icon)
        #sleep(2)
        pczhpage.search(self.driver,key_word)
        sleep(2)
        self.assertEqual(self.driver.title,key_word+" | 亚米")
        #sleep(2)
    
    def test_2itemdetail(self):
        """跳转到商品详情页"""
        self.driver.implicitly_wait(10)
        common.elementclick(self.driver,pczhpageElements.search_result_item)
        #sleep(5)
        i = -1 #i表示切换到的窗口索引
        common.switchWindow(self.driver,i)
        type = 'data-scene'
        text = common.getattribute(self.driver,pczhpageElements.pdp_scene,type)
        self.assertEqual(text,"item_detail")
        #sleep(2)

    
    def test_3addcart(self):
        """详情页加购"""
        self.driver.implicitly_wait(10)
        common.slideScroll(self.driver,pczhpageElements.item_addbutton)
        common.elementclick(self.driver,pczhpageElements.item_addbutton)
        sleep(2)
        verifyText = common.gettext(self.driver,pczhpageElements.item_addedText)
        #try:
        self.assertEqual(verifyText,"商品已加入购物车")
        #except AssertionError:
        #    raise
        #    raise AssertionError
        #    self.runNo = self.runNo +1
        #    print("结果有误进入重跑机制：%s" %AssertionError)
        #    sleep(3)
        #    common.getweb(self.driver,"https://www.yamibuy.com/zh/p/liuzhou-guangxi-specialty-luosifen-pickle-flavor-noodles-280g-no-quail-egg-random-version/1021006541")
        #    self.test_3addcart()
        #sleep(2)
    
    
    def test_4viewcart(self):
        """查看购物车"""
        self.driver.implicitly_wait(10)
        common.elementclick(self.driver,pczhpageElements.item_viewcart)
        #sleep(2)
        type = 'data-scene'
        text = common.getattribute(self.driver,pczhpageElements.cart_scene,type)
        self.assertEqual(text,"cart_main")
        #sleep(2)
    
    def test_5submit(self):
        """未登录点击去结算"""
        self.driver.implicitly_wait(10)
        common.elementclick(self.driver,pczhpageElements.cart_submit)
        #sleep(2)
        common.sendkeys(self.driver,pczhpageElements.cus_email,config.cus_email)
        #sleep(2)
        # common.elementclick(self.driver,pczhpageElements.password_frame)
        common.sendkeys(self.driver,pczhpageElements.cus_password,config.cus_password)
        #sleep(2)

        
    @unittest.skip("暂未调通，添加cookie后，刷新页面，不是登录状态")
    def test_6login(self):
        """通过接口实现用户登陆"""
        login_url="https://customer.yamibuy.com/api/users/login"
        # header = {"Cookie":"ymb_tnimager=EKTaL8%2BMHEMNoM2ChNe4hw%3D%3D",
        # "Cache-Control":"no-cache",
        # "Postman-Token":"<calculated when request is sent>",
        # "Content-Type":"application/json",
        # "Content-Length":"<calculated when request is sent>",
        # "Host":"<calculated when request is sent>",
        # "Connection":"keep-alive"}
        body_data_json ={"params": {"email": "autotesting@yamibuy.com","pwd": "111111","imagePosition": 66,"isRest": 1}}
        response = requests.post(url=login_url,json=body_data_json,verify=False)
        json_obj = json.loads(response.content)
        token = json_obj['data']['token']
        # self.driver.get("https://trade.yamibuy.com/zh/cart")
        self.driver.delete_cookie("YMB_TK")
        self.driver.add_cookie({'name':'YMB_TK', 'value':token})
        sleep(2)
        self.driver.refresh()
        sleep(15)