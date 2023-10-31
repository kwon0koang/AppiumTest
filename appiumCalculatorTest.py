import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.touch_action import TouchAction
import re

capabilities = {
  "platformName": "Android",
  "appium:deviceName": "R3CMA0F73PL",
  "appium:appPackage": "com.sec.android.app.popupcalculator",
  "appium:appActivity": ".Calculator",
  "appium:automationName": "uiautomator2"
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
        calculator = self.driver

        # tap
        action = TouchAction(calculator)
        action.tap(x=173, y=1400).perform()
        action.tap(x=173, y=1400).perform()
        action.tap(x=173, y=1400).perform()
        
        # drag
        action.press(x=700, y=700).move_to(x=700, y=1400).release().perform()

        # touch number 0~9 (0은 keycode 7임)
        for i in range(7, 17):
          calculator.press_keycode(i)

        # 객체 인식
        calculator.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='초기화').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="1"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="1"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="1"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="1"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="더하기"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="2"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="2"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="2"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="2"]').click()
        calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="계산"]').click()
        sumValue = calculator.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@resource-id="com.sec.android.app.popupcalculator:id/calc_edt_formula"]').text

        def extractNumbers(input_string):
          numbers = re.findall(r'\d+', input_string)  # 숫자만 추출
          return ''.join(numbers) # 문자열로 결합
        
        result = extractNumbers(sumValue)
        if (result == "3333") :
            print("sum test pass")
            

if __name__ == '__main__':
    unittest.main()


