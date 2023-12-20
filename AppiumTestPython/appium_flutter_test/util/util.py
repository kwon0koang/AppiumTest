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
import unittest
import argparse

# 특정 단어 포함하는 xpath 가져오기
# //*[contains(@content-desc,"text you want to find")]
# You can change @label for @name or @value

# init test ======================================================================================================================================================================================================

# 스크립트 파라미터 파싱
def get_args(argv) -> argparse.Namespace:
    # help
    parser = argparse.ArgumentParser(description="Test Appium", add_help=True) # python3 test.py -h
    
    # 파싱
    devices = " / ".join(config.capabilities.keys())
    parser.add_argument("--device", "-d", dest="device", help=f"Available devices >>>>>>> {devices}")
    
    # 1번째는 스크립트 이름. 실제 파라미터는 2번째부터
    args = parser.parse_args(argv[1:])
    return args

# 테스트 슈트 로드
def load_tests(args: argparse.Namespace, test_class) -> unittest.TestSuite:
    
    # 파라미터 전달
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    for test_case in suite:
        test_case.device = args.device
        
    return suite    

# info ======================================================================================================================================================================================================

def get_capabilites():
    return config.capabilities[config.device]

def get_port() -> int: 
    return 4723
    # return config.ports[config.device]

class Platform(Enum):
    AOS = 1001
    IOS = 1002
def get_platform() -> Platform:
    if get_capabilites()['platformName'].lower() == 'ios':
        return Platform.IOS
    else:
        return Platform.AOS

def get_capabilities_options():
    if get_platform() == Platform.AOS:
        return UiAutomator2Options().load_capabilities(get_capabilites())
    else:
        return XCUITestOptions().load_capabilities(get_capabilites())
    
def get_app_package():
    if (get_platform() == Platform.AOS):
        return get_capabilites()['appium:appPackage']
    else:
        return get_capabilites()['appium:bundleId']
    
# action ======================================================================================================================================================================================================

def get_value(aos: str, ios: str):
    return aos if get_platform() == Platform.AOS else ios

# 클릭할 수 있을 때까지 기다림
def wait(driver: webdriver.WebDriver, by: str, value: str):
    wait = WebDriverWait(driver, 30)
    wait.until(EC.element_to_be_clickable((by, value)))
def wait_by_id(driver: webdriver.WebDriver, id: str):
    wait(driver, AppiumBy.ACCESSIBILITY_ID, id)
def wait_by_xpath(driver: webdriver.WebDriver, xpath: str):
    wait(driver, AppiumBy.XPATH, id)

# 클릭할 수 있을 때 element 반환
def find(driver: webdriver.WebDriver, by: str, value: str) -> WebElement:
    wait(driver, by, value)
    return driver.find_element(by=by, value=value)
def find_by_id(driver: webdriver.WebDriver, id: str) -> WebElement:
    return find(driver, AppiumBy.ACCESSIBILITY_ID, id)
def find_by_xpath(driver: webdriver.WebDriver, xpath: str) -> WebElement:
    return find(driver, AppiumBy.XPATH, xpath)

# 클릭할 수 있을 때 element 클릭
def click(driver: webdriver.WebDriver, by: str, value: str):
    find(driver, by, value).click()
def click_by_id(driver: webdriver.WebDriver, id: str):
    find(driver, AppiumBy.ACCESSIBILITY_ID, id).click()
def click_by_xpath(driver: webdriver.WebDriver, xpath: str):
    find(driver, AppiumBy.XPATH, xpath).click()
    
# 클릭할 수 있을 때 element 키 입력
def send_keys(driver: webdriver.WebDriver, by: str, el_value: str, value: str):
    find(driver, by, el_value).send_keys(value)
def send_keys_by_id(driver: webdriver.WebDriver, id: str, value: str):
    find(driver, AppiumBy.ACCESSIBILITY_ID, id).send_keys(value)
def send_keys_by_xpath(driver: webdriver.WebDriver, xpath: str, value: str):
    find(driver, AppiumBy.XPATH, xpath).send_keys(value)

# 스크롤
class ScrollDirection(Enum):
    DOWN = 8888
    UP = 9999
def scroll(driver: webdriver.WebDriver, direction: ScrollDirection) -> None:
    screen_size = driver.get_window_size()
    width = screen_size['width']
    height = screen_size['height']

    # action = TouchAction(driver)
    
    if direction == ScrollDirection.DOWN:
        start_x = width*0.2
        start_y = height*0.8
        end_x = width
        end_y = 0
        # action.press(x=start_x, y=start_y).wait(500).move_to(x=end_x, y=end_y).release().perform()
        driver.swipe(start_x, start_y, end_x, end_y, 500)
    elif direction == ScrollDirection.UP:
        start_x = width*0.2
        start_y = height*0.2
        end_x = width
        end_y = height
        # action.press(x=start_x, y=start_y).wait(500).move_to(x=end_x, y=end_y).release().perform()
        driver.swipe(start_x, start_y, end_x, end_y, 500)
    else:
        print("nothing")

# 스크롤
def scroll_down_to(driver: webdriver.WebDriver, element_id: str):
    while True:
        try:
            driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value=element_id)
            break  # 루프 종료
        except Exception:
            # 스크롤
            scroll(driver=driver, direction=ScrollDirection.DOWN)


    
