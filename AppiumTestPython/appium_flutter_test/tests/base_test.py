import unittest
from appium import webdriver
import config
import util
import sys

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
            print("tearDown / quit")
            # ios는 테스트 끝나도 앱 종료안되서 강제 종료
            if (util.platform == util.Platform.IOS):
                self.driver.terminate_app(config.ios_bundle_id)
            self.driver.quit()

