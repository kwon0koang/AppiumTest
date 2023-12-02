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
        print(f"__init__")
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
        print("tearDown")
        if self.driver:
            print("tearDown / quit")
            # noReset true 하면 테스트 끝나도 앱 종료안되서 강제 종료
            self.driver.terminate_app(util.get_app_package())
            self.driver.quit()

    def test_todo_list(self) -> None:
        
        # id_todo_list = util.get_element(aos="Todo list", ios="todo")
        # util.click_element_by_id(self.driver, id_todo_list)
        
        # xpath_filter_text = util.get_element(aos="//android.widget.EditText", ios="todo")
        # util.click_element_by_xpath(self.driver, xpath_filter_text)
        # util.send_keys_element_by_xpath(self.driver, xpath_filter_text, "veritatis pariatur delectus")
        # self.driver.hide_keyboard()
        
        # id_todo_item = util.get_element(aos="2 / 27 / true / veritatis pariatur delectus", ios="todo")
        # util.click_element_by_id(self.driver, id_todo_item)
        
        # time.sleep(0.5)
        
        # POM 적용 후 ==============================================================
        main_page = MainPage(self.driver)
        main_page.click_todo_list()
        
        todo_list_page = TodoListPage(self.driver)
        time.sleep(2)
        todo_list_page.scroll_down()
        todo_list_page.scroll_up()
        todo_list_page.send_keys_filter_text()
        todo_list_page.click_todo_item()
        
        time.sleep(0.5)
        

# 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드를 실행
# 모듈로 사용할 때(다른 스크립트로부터 import 되었을 때)는 실행 X
if __name__ == '__main__':
    # unittest.main()
    
    # # 1번째는 스크립트 이름. 실제 파라미터는 2번째부터
    # arguments = sys.argv[1:]
    # print("Received parameters:", arguments)

    # # 파라미터를 TestAppium custom_parameter로 전달하여 테스트
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestAppium)
    # for test_case in suite:
    #     if isinstance(test_case, TestAppium):
    #         test_case.custom_parameter = arguments[0] if arguments else None
    #         print("test_case.custom_parameter:", test_case.custom_parameter)
            
    parser = argparse.ArgumentParser(description="Test Appium", add_help=True) # python3 test.py --help
    
    devices = " / ".join(config.capabilities.keys())
    parser.add_argument("--device", "-d", dest="device", help=f"Available devices >>>>>>> {devices}")
    
    # 1번째는 스크립트의 이름. 실제 파라미터는 2번째부터
    args = parser.parse_args(sys.argv[1:])
    
    print(f"parameters >>>>>>> device : {args.device}")

    # 파라미터 전달
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAppium)
    for test_case in suite:
        test_case.device = args.device
            
    unittest.TextTestRunner().run(suite)



