import config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum
from appium.webdriver.common.touch_action import TouchAction
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

# aos 인지 여부
def is_aos():
    return "ANDROID" == str.upper(config.capabilities['platformName'])

def get_capabilities_options():
    if is_aos():
        return UiAutomator2Options().load_capabilities(config.capabilities)
    else:
        return XCUITestOptions().load_capabilities(config.capabilities)
def get_id(aos: str, ios: str):
    return aos if is_aos() else ios
def get_xpath(aos: str, ios: str):
    return aos if is_aos() else ios

# element 클릭할 수 있을 때까지 기다렸다가 클릭
# def click_element(driver: webdriver, id: str):
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, id))).click()
def click_element(driver: webdriver, id: str=None, xpath: str=None):
    wait = WebDriverWait(driver, 10)
    if id:
        print(f"Click element by ID: {id}")
        wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, id))).click()
    elif xpath:
        print(f"Click element by XPath: {xpath}")
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath))).click()
    else:
        print("nothing")
    
# 스크롤
class ScrollDirection(Enum):
    DOWN = 8888
    UP = 9999
def scroll(driver: webdriver, direction: ScrollDirection) -> None:
    screen_size = driver.get_window_size()
    width = screen_size['width']
    height = screen_size['height']

    # 중앙 좌표 계산
    center_x = width // 2
    center_y = height // 2
    
    action = TouchAction(driver)
    
    if direction == ScrollDirection.DOWN:
        action.press(x=center_x, y=(height+center_y)//2).move_to(x=center_x, y=50).release().perform()
    elif direction == ScrollDirection.UP:
        action.press(x=center_x, y=(center_y)//2).move_to(x=center_x, y=height).release().perform()
    else:
        print("nothing")


