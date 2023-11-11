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

id_todo_list = util.get_element(aos="Todo list", ios="todo")
xpath_filter_text = util.get_element(aos="//android.widget.EditText", ios="todo")
id_todo_item = util.get_element(aos="2 / 27 / true / veritatis pariatur delectus", ios="todo")

# todo kyk iOS 테스트 성공
xpath_touch = util.get_element(aos="todo", ios="//XCUIElementTypeStaticText[@name=\"Touch\"]")
id_touchable_view = util.get_element(aos="todo", ios="touchableView")

class TestAppium(unittest.TestCase):
    def __init__(self, methodName='runTest', custom_parameter=None):
        print("__init__")
        super().__init__(methodName)
        self.custom_parameter = custom_parameter

    def setUp(self) -> None:
        print(f"setUp / self.custom_parameter : {self.custom_parameter}")
        
        # 플랫폼 셋팅
        util.platform = util.Platform.IOS if self.custom_parameter == "ios" else util.Platform.AOS
        print(f"setUp / util.platform : {util.platform}")
        
        # 드라이버 셋팅
        self.driver = webdriver.Remote(command_executor=config.appium_server_url, options=util.get_capabilities_options())

    def tearDown(self) -> None:
        print("tearDown")
        if self.driver:
            self.driver.quit()

    def test_action(self) -> None:
        driver = self.driver
        
        util.click_element(driver=driver, id=id_todo_list)
        
        # time.sleep(2)
        # util.scroll(driver=driver, direction=util.ScrollDirection.DOWN)
        # util.scroll(driver=driver, direction=util.ScrollDirection.UP)
        
        util.click_element(driver=driver, xpath=xpath_filter_text)
        driver.find_element(by=AppiumBy.XPATH, value=xpath_filter_text).send_keys("veritatis pariatur delectus")
        driver.hide_keyboard()
        
        util.click_element(driver=driver, id=id_todo_item)
        
        time.sleep(3)
        
        # todo kyk iOS 테스트 성공
        # driver = self.driver
        # util.click_element(driver=driver, xpath=xpath_touch)
        # util.click_element(driver=driver, id=id_touchable_view)
        # time.sleep(3)

if __name__ == '__main__':
    # unittest.main()
    
    # 1번째는 스크립트의 이름. 실제 파라미터는 2번째부터
    arguments = sys.argv[1:]

    # 전달된 파라미터 출력
    print("Received parameters:", arguments)

    # 파라미터를 TestAppium custom_parameter로 전달하여 테스트
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppium)
    for test_case in suite:
        if isinstance(test_case, TestAppium):
            test_case.custom_parameter = arguments[0] if arguments else None
            print("test_case.custom_parameter:", test_case.custom_parameter)

    unittest.TextTestRunner().run(suite)


