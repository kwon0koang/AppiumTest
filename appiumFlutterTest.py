import unittest
import re
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

capabilities = {
  "platformName": "Android",
  "appium:deviceName": "R3CMA0F73PL",
  "appium:appPackage": "com.example.test_flutter",
  "appium:appActivity": ".MainActivity",
  "appium:automationName": "uiautomator2"
  "appium:autoGrantPermissions": "true"
}

appium_server_url = 'http://localhost:4723/wd/hub'

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_tab_action(self) -> None:
        driver = self.driver
        
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.Button[@content-desc="Todo list"]'))).click()
        wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, '2 / 27 / true / veritatis pariatur delectus'))).click()
        
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()


