import unittest
import re
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config
import util
import sys

el_todo_list = "Todo list" if util.is_aos() else "todo"
el_todo_item = "2 / 27 / true / veritatis pariatur delectus" if util.is_aos() else "todo"
        
class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        capabilities_options = UiAutomator2Options().load_capabilities(config.capabilities)
        self.driver = webdriver.Remote(command_executor=config.appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_tab_action(self) -> None:
        driver = self.driver
        
        wait = WebDriverWait(driver, 20)
        
        wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, el_todo_list))).click()
        wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, el_todo_item))).click()
        
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()


