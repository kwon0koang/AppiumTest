from appium import webdriver
import config
import util
from appium.webdriver.common.appiumby import AppiumBy
import time

driver = webdriver.Remote(command_executor=config.appium_server_url(), options=util.get_capabilities_options())

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Todo list")
el.click()

time.sleep(5)