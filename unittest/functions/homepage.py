from selenium.webdriver.common.by import By
from functions import homepageElements

def search(driver,url,key_word):
    driver.get(url)
    driver.find_element(By.XPATH,homepageElements.search_keyword).send_keys(key_word)
    driver.find_element(By.XPATH,homepageElements.search_submit).click()
