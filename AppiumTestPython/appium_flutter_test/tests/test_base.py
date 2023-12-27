import unittest
from appium import webdriver
import config
import util.util as util

class BaseTest(unittest.TestCase):
    def __init__(self, methodName='runTest', device=None):
        print(f"__init__")
        super().__init__(methodName)
        self.device = device

    def setUp(self, app_package: str = None, app_activity: str = None, bundle_id: str = None) -> None:
        # 디바이스 셋팅
        if self.device:
            config.device = self.device
        
        # 테스트 앱 셋팅
        if app_package:
            util.get_capabilites()["appium:appPackage"] = app_package
        if app_activity:
            util.get_capabilites()["appium:appActivity"] = app_activity
        if bundle_id:
            util.get_capabilites()["appium:bundleId"] = bundle_id
            
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
            

