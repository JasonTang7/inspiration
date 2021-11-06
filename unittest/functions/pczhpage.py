from selenium.webdriver.common.by import By
from functions import pczhpageElements,common

def search(driver,key_word):
    driver.find_element(By.XPATH,pczhpageElements.search_keyword).send_keys(key_word)
    common.elementclick(driver,pczhpageElements.search_submit)

