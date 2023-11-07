import unittest
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import util
import sys
from enum import Enum

id_todo_list = util.get_id(aos="Todo list", ios="todo")
xpath_filter_text = util.get_xpath(aos="//android.widget.EditText", ios="todo")
id_todo_item = util.get_id(aos="2 / 27 / true / veritatis pariatur delectus", ios="todo")

# todo kyk iOS 테스트 성공
xpath_touch = util.get_id(aos="todo", ios="//XCUIElementTypeStaticText[@name=\"Touch\"]")
id_touchable_view = util.get_id(aos="todo", ios="touchableView")

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=config.appium_server_url, options=util.get_capabilities_options())

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_action(self) -> None:
        # driver = self.driver
        
        # util.click_element(driver=driver, id=id_todo_list)
        
        # # time.sleep(2)
        # # util.scroll(driver=driver, direction=util.ScrollDirection.DOWN)
        # # util.scroll(driver=driver, direction=util.ScrollDirection.UP)
        
        # util.click_element(driver=driver, xpath=xpath_filter_text)
        # driver.find_element(by=AppiumBy.XPATH, value=xpath_filter_text).send_keys("veritatis pariatur delectus")
        # driver.hide_keyboard()
        
        # util.click_element(driver=driver, id=id_todo_item)
        
        # time.sleep(3)
        
        # todo kyk iOS 테스트 성공
        driver = self.driver
        util.click_element(driver=driver, xpath=xpath_touch)
        util.click_element(driver=driver, id=id_touchable_view)
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()


