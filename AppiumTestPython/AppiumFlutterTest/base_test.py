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
from pages.main_page import MainPage
from pages.todo_list_page import TodoListPage

class BaseTest(unittest.TestCase):
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

# 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드를 실행
# 모듈로 사용할 때(다른 스크립트로부터 import 되었을 때)는 실행 X
if __name__ == '__main__':
    # unittest.main()
    
    # 1번째는 스크립트의 이름. 실제 파라미터는 2번째부터
    arguments = sys.argv[1:]

    # 전달된 파라미터 출력
    print("Received parameters:", arguments)

    # 파라미터를 custom_parameter로 전달하여 테스트
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTest)
    for test_case in suite:
        if isinstance(test_case, BaseTest):
            test_case.custom_parameter = arguments[0] if arguments else None
            print("test_case.custom_parameter:", test_case.custom_parameter)

    unittest.TextTestRunner().run(suite)


