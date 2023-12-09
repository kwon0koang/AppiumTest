from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.options.android import UiAutomator2Options

# 테스트 앱 열기
capabilities = UiAutomator2Options().load_capabilities({
  "platformName": "Android",
  "appium:deviceName": "aos_galaxy_note_10_plus",
  "appium:udid": "R3CMA0F73PL",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.example.test_flutter",
  "appium:appActivity": ".MainActivity",
  "appium:autoGrantPermissions": "true",
  "appium:noReset": "true",
  "appium:newCommandTimeout": "3000"
})
driver = webdriver.Remote(command_executor="http://localhost:4723", options=capabilities)

time.sleep(3)

# "Todo list" 클릭
el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Todo list")
el.click()

time.sleep(2)

# 스크롤
driver.swipe(700, 1500, 0, 0, 1000)
driver.swipe(200, 500, 900, 1800, 1000)

time.sleep(3)








