import poium
from poium.webdriver import Page
import pytest
import time
from page.PC_page import Home_page
from config import RunConfig,StaticConfig

class Test_Search:
    """搜索测试"""

    def test_1search_key_word(self,browser,base_url):
        page = Home_page(browser)
        page.get(StaticConfig.pchome_url)
        if page.monetate_icon:
            page.monetate_icon.click()
        page.search_input.send_keys("螺蛳粉")
        page.search_submit.click()
        time.sleep(3)
        assert browser.title == "螺蛳粉 | 亚米"
