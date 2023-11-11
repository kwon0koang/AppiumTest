import config
from appium.webdriver import webdriver
from appium.webdriver.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from enum import Enum
from appium.webdriver.common.touch_action import TouchAction
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

class Platform(Enum):
    AOS = 1001
    IOS = 1002
platform = Platform.AOS

def get_capabilities_options():
    if platform == Platform.AOS:
        return UiAutomator2Options().load_capabilities(config.aos_capabilities)
    else:
        return XCUITestOptions().load_capabilities(config.ios_capabilities)
def get_element(aos: str, ios: str):
    return aos if platform == Platform.AOS else ios

# 클릭할 수 있을 때까지 기다림
def wait_element_by_id(driver: webdriver.WebDriver, id: str):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, id)))
def wait_element_by_xpath(driver: webdriver.WebDriver, xpath: str):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, xpath)))

# 클릭할 수 있을 때 element 반환
def find_element_by_id(driver: webdriver.WebDriver, id: str) -> WebElement:
    wait_element_by_id(driver, id)
    return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=id)
def find_element_by_xpath(driver: webdriver.WebDriver, xpath: str) -> WebElement:
    wait_element_by_xpath(driver, xpath)
    return driver.find_element(by=AppiumBy.XPATH, value=xpath)

# 클릭할 수 있을 때 element 클릭
def click_element_by_id(driver: webdriver.WebDriver, id: str):
    find_element_by_id(driver, id).click()
def click_element_by_xpath(driver: webdriver.WebDriver, xpath: str):
    find_element_by_xpath(driver, xpath).click()
    
# 클릭할 수 있을 때 element 클릭
def send_keys_element_by_id(driver: webdriver.WebDriver, id: str, value: str):
    find_element_by_id(driver, id).send_keys(value)
def send_keys_element_by_xpath(driver: webdriver.WebDriver, xpath: str, value: str):
    find_element_by_xpath(driver, xpath).send_keys(value)

# 스크롤
class ScrollDirection(Enum):
    DOWN = 8888
    UP = 9999
def scroll(driver: webdriver.WebDriver, direction: ScrollDirection) -> None:
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

# todo kyk 스크롤
def scroll_down_to():
    ''
