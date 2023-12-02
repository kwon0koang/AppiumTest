from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options

# 테스트 앱 열기
capabilities = UiAutomator2Options().load_capabilities({
  "platformName": "android",
  "appium:deviceName": "aos_galaxy_s_20_5g",
  "appium:udid": "R3CN30JZ89F",
  "appium:automationName": "uiautomator2",
  "appium:appPackage": "com.example.test_flutter",
  "appium:appActivity": ".MainActivity",
  "appium:autoGrantPermissions": "true",
  "appium:noReset": "true"
})
driver = webdriver.Remote(command_executor="http://localhost:4723", options=capabilities)

time.sleep(3)

# "Todo list" 클릭
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Todo list")
el.click()

time.sleep(3)








