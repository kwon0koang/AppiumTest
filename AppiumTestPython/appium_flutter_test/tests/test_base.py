import unittest
from appium import webdriver
import config
import util

class BaseTest(unittest.TestCase):
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
            

