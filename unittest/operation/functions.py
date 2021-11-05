from selenium.webdriver.common.by import By

def search(driver,url,key_word):
    driver.get(url)
    driver.find_element(By.XPATH,"//*[@class='search-box']//input[@name='keywords']").send_keys(key_word)
    driver.find_element(By.XPATH,"//*[@class='search-box']//button[@type='submit']").click()
