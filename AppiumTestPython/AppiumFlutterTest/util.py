import config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# aos 인지 여부
def is_aos():
    return "Android" == config.capabilities['platformName']

# element 클릭할 수 있을 때까지 기다렸다가 클릭
def click_element(driver: webdriver, id: str):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, id))).click()
    



