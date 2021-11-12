import poium
from poium.webdriver import Page
import pytest
import time
from page.PC_page import Home_page
from config import RunConfig,StaticConfig
import json
from os.path import dirname, abspath
import sys


base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)


class Test_Search:
    """搜索测试"""

    def get_data(self,file_path):
        """读取参数化文件"""
        data=[]
        with(open(file_path,"-r")) as f:
            dict_data = json.load(f.read())
            for i in dict_data:
                data.append(tuple(i.values()))
        return data


    @pytest.mark.parametrize(
        "name,key_words",
        [("1","螺蛳粉"),
        ("2","面膜"),
        ("3","方便面"),
        ],
        ids=["case1","case2","case3"]
    )
    # @pytest.mark.parametrize(
    #     "name,key_words",
    #     get_data(base_path +"/test_case/data/data_file.json")
    # )
    def test_1search_key_word(self,name, key_words,browser):
        """ 首页关键字搜索"""
        page = Home_page(browser)
        page.get(StaticConfig.pchome_url)
        if page.monetate_icon is True:
            page.monetate_icon.click()
        else:
            pass
        page.search_input = key_words
        page.search_submit.click()
        time.sleep(3)
        assert browser.title ==key_words+ " | 亚米"
