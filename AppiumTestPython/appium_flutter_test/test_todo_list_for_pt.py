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
from pages.page_main import MainPage
from pages.page_todo_list import TodoListPage
import argparse

class TestAppium(unittest.TestCase):
    def __init__(self, methodName='runTest', platform=None, port=None):
        super().__init__(methodName)
        self.platform = platform
        self.port = port

    def setUp(self) -> None:
        # 플랫폼 셋팅
        util.platform = util.Platform.IOS if self.platform == "ios" else util.Platform.AOS
        
        # 포트 셋팅
        config.appium_server_port = config.appium_server_port if self.port is None else self.port
        
        # 드라이버 셋팅
        self.driver = webdriver.Remote(command_executor=config.appium_server_url(), options=util.get_capabilities_options())

    def tearDown(self) -> None:
        if self.driver:
            self.driver.terminate_app(util.get_app_package())
            self.driver.quit()

    def test_todo_list(self) -> None:
        
        # todo kyk
        
        time.sleep(0.5)

# 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드를 실행
# 모듈로 사용할 때(다른 스크립트로부터 import 되었을 때)는 실행 X
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test Appium", add_help=True)
    
    parser.add_argument("--platform", "-p", dest="platform", help="aos or ios (default : aos)")
    parser.add_argument("--port", "-P", dest="port", help="default : 4723")
    
    # 1번째는 스크립트의 이름. 실제 파라미터는 2번째부터
    args = parser.parse_args(sys.argv[1:])
    
    print(f"parameters >>>>>>> platform : {args.platform} / port : {args.port}")

    # 파라미터 전달하여 테스트
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppium)
    for test_case in suite:
        test_case.platform = args.platform
        test_case.port = args.port
            
    unittest.TextTestRunner().run(suite)



