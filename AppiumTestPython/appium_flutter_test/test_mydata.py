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
import util.util as util
import sys
from enum import Enum
from pages.page_main import MainPage
from pages.page_todo_list import TodoListPage
import argparse

class MyDataTest(unittest.TestCase):
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

    def sign(self) -> None:
        xpath_signkorea_ca5 = util.get_element(aos="//*[contains(@content-desc,\"MyData_User2\")]", ios="")
        util.click_element_by_xpath(self.driver, xpath_signkorea_ca5)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[1]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[11]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[2]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[12]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[3]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[13]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[4]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        xpath_button = util.get_element(aos=f"(//android.widget.ImageView[@content-desc=\"버튼\"])[14]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button)
        id_special_char_change = util.get_element(aos="특수문자변경", ios="")
        util.click_element_by_id(self.driver, id_special_char_change)
        xpath_button_1 = util.get_element(aos="(//android.widget.ImageView[@content-desc=\"버튼\"])[1]", ios="")
        util.click_element_by_xpath(self.driver, xpath_button_1)
        util.click_element_by_xpath(self.driver, xpath_button_1)
        xpath_done_button = util.get_element(aos="//android.widget.ImageButton[@content-desc=\"입력완료\"]", ios="")
        util.click_element_by_xpath(self.driver, xpath_done_button)

    def test_mydata(self) -> None:
        
        id_asset = util.get_element(aos="전체 자산", ios="")
        util.click_element_by_id(self.driver, id_asset)
        id_management = util.get_element(aos="연결관리", ios="")
        util.click_element_by_id(self.driver, id_management)

        xpath_hanwha_investment = util.get_element(aos='//*[contains(@content-desc,"한화투자증권")]', ios="")
        util.click_element_by_xpath(self.driver, xpath_hanwha_investment)
        xpath_change_conn_info = util.get_element(aos='//*[contains(@content-desc,"연결정보 변경하기")]', ios="")
        util.click_element_by_xpath(self.driver, xpath_change_conn_info)
        
        # ==========================================================
        
        id_cert = util.get_element(aos="공동인증서", ios="")
        util.click_element_by_id(self.driver, id_cert)
        id_agree_all = util.get_element(aos="(필수) 모두 동의합니다", ios="")
        util.click_element_by_id(self.driver, id_agree_all)
        id_agree = util.get_element(aos="모두 동의하기", ios="")
        util.click_element_by_id(self.driver, id_agree)
        
        time.sleep(1)
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        
        util.click_element_by_id(self.driver, id_agree)
        
        xpath_connect_one = util.get_element(aos="//*[contains(@content-desc,\"건 연결하기\")]", ios="")
        util.click_element_by_xpath(self.driver, xpath_connect_one)
        
        time.sleep(1)
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        
        id_agree_connect = util.get_element(aos="모두 동의하기", ios="")
        util.click_element_by_id(self.driver, id_agree_connect)
        id_like = util.get_element(aos="좋아요", ios="")
        util.click_element_by_id(self.driver, id_like)
        
        self.sign()
        
        xpath_hanwha = util.get_element(aos="//*[contains(@content-desc,\"한화투자증권\")]", ios="")
        util.click_element_by_xpath(self.driver, xpath_hanwha)
        
        time.sleep(1)

# 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드를 실행
# 모듈로 사용할 때(다른 스크립트로부터 import 되었을 때)는 실행 X
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Test Appium", add_help=True) # python3 test.py --help
    
    devices = " / ".join(config.capabilities.keys())
    parser.add_argument("--device", "-d", dest="device", help=f"Available devices >>>>>>> {devices}")
    
    # 1번째는 스크립트 이름. 실제 파라미터는 2번째부터
    args = parser.parse_args(sys.argv[1:])
    
    print(f"parameters >>>>>>> device : {args.device}")

    # 파라미터 전달
    suite = unittest.TestLoader().loadTestsFromTestCase(MyDataTest)
    for test_case in suite:
        test_case.device = args.device
            
    unittest.TextTestRunner().run(suite)

