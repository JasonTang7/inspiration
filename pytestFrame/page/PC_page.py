from os import link
from poium import Page, Element

class Home_page(Page):
    #PC首页
    monetate_icon=Element(xpath="//*[@id='monetate_allinone_lightbox']//i[@class='iconfont icon-close']",timeout=5,describe="页面弹窗")
    search_input=Element(timeout=5,describe="搜索input",xpath="//*[@class='search-box']//input[@name='keywords']")
    search_submit=Element(xpath="//*[@class='search-box']//button[@type='submit']",timeout=5,describe="搜索按钮") 
