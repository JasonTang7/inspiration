from selenium.webdriver.common.by import By
from functions import pczhpageElements,common

def search(driver,key_word):
    common.sendkeys(driver,pczhpageElements.search_keyword,key_word)
    common.elementclick(driver,pczhpageElements.search_submit)

