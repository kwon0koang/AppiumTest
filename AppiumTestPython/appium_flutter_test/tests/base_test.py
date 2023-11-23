import unittest
from appium import webdriver
import config
import util
import sys

class BaseTest(unittest.TestCase):
    def __init__(self, methodName='runTest', platform=None, port=None):
        print("__init__")
        super().__init__(methodName)
        self.platform = platform
        self.port = port

    def setUp(self) -> None:
        # 플랫폼 셋팅
        util.platform = util.Platform.IOS if self.platform == "ios" else util.Platform.AOS
        
        # 서버 URL 셋팅
        port = config.appium_server_default_port if self.port is None else self.port
        appium_server_url = f"{config.appium_server_host}:{port}{config.appium_server_base_path}"
        
        print(f"setUp / platform : {util.platform} / url : {appium_server_url}")
        
        # 드라이버 셋팅
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=util.get_capabilities_options())

    def tearDown(self) -> None:
        print("tearDown")
        if self.driver:
            print("tearDown / quit")
            # ios는 noReset true 하면 테스트 끝나도 앱 종료안되서 강제 종료
            if (util.platform == util.Platform.IOS):
                self.driver.terminate_app(config.ios_bundle_id)
            self.driver.quit()

