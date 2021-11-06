from selenium.webdriver.common.by import By


def getweb(driver,url):
    driver.get(url)

def elementclick(driver,elementXpath):
    driver.find_element(By.XPATH,elementXpath).click()

def getattribute(driver,elementXpath,type):
    attribute =driver.find_element(By.XPATH,elementXpath).get_attribute(type)
    return attribute

def gettext(driver,elementXpath):
    verifyText = driver.find_element(By.XPATH,elementXpath).text
    return verifyText

#切换当前窗口
def switchWindow(driver,i):
    handles = driver.window_handles
    driver.switch_to.window(handles[i])

#拖动滚动条到指定元素
def slideScroll(driver,targetElem):
    element = driver.find_element(By.XPATH,targetElem)
    driver.execute_script("arguments[0].scrollIntoView();", element)
