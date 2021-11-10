import time
import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from functions import pczhpage,common,pczhpageElements
import config
import requests
import json

@unittest.skip("调试用，正式测试不执行此测试类")
class TestLogIn(unittest.TestCase):
    """测试登录接口"""
    # @classmethod
    # def setUpClass(cls) :
    #     cls.driver = webdriver.Chrome()
    #     cls.pc_url = "https://www.yamibuy.com"
    #     cls.driver.get("https://www.yamibuy.com")
    
    # # @classmethod
    # # def tearDownClass(cls):
    # #     cls.driver.quit()

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
        self.driver.delete_cookie("YMB_TK")
        self.driver.add_cookie({'name':'YMB_TK', 'value':token})
        sleep(2)
        self.driver.refresh()
        sleep(5)