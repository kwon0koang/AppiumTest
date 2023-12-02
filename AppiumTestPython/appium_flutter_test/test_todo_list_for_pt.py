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
    def __init__(self, methodName='runTest', device=None):
        super().__init__(methodName)
        self.device = device

    def setUp(self) -> None:
        # 디바이스 셋팅
        if self.device:
            config.device = self.device
        
        # 드라이버 셋팅
        appium_server_url = f"{config.appium_server_host}:{util.get_port()}"
        capabilities_options = util.get_capabilities_options()
        print(f"setUp / device : {config.device} / appium_server_url : {appium_server_url}")
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            # noReset true 하면 테스트 끝나도 앱 종료안되서 강제 종료
            self.driver.terminate_app(util.get_app_package())
            self.driver.quit()

    def test_todo_list(self) -> None:
        
        # todo kyk
        
        time.sleep(0.5)

# 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드를 실행
# 모듈로 사용할 때(다른 스크립트로부터 import 되었을 때)는 실행 X
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test Appium", add_help=True)
    
    devices = " / ".join(config.capabilities.keys())
    parser.add_argument("--device", "-d", dest="device", help=f"Available devices >>>>>>> {devices}")
    
    # 1번째는 스크립트 이름. 실제 파라미터는 2번째부터
    args = parser.parse_args(sys.argv[1:])
    
    print(f"parameters >>>>>>> device : {args.device}")

    # 파라미터 전달
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppium)
    for test_case in suite:
        test_case.device = args.device
            
    unittest.TextTestRunner().run(suite)



