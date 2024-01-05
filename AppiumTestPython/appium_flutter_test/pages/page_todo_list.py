import util.util as util
from pages.page_base import BasePage
from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import unittest

class TodoListPage(BasePage):

    testCase = unittest.TestCase()

    def send_keys_filter_text(self):
        xpath_filter_text = util.get_value(aos="//android.widget.EditText", ios='//XCUIElementTypeTextField[@name="Filter text"]')
        util.click(self.driver, AppiumBy.XPATH, xpath_filter_text)
        util.send_keys(self.driver, AppiumBy.XPATH, xpath_filter_text, "veritatis pariatur delectus")
        self.driver.hide_keyboard()
        # driver.press_keycode(4) // back key
        
    def check_todo_item(self):
        id_todo_item = util.get_value(aos="2 / 27 / true / veritatis pariatur delectus", ios="2 / 27 / true / veritatis pariatur delectus")
        el = util.wait(self.driver, AppiumBy.ID, id_todo_item)
        content_desc = el.get_attribute("content-desc")
        self.testCase.assertEqual(content_desc, '2 / 27 / true / veritatis pariatur delectus', '검증 실패 :(')

    def click_todo_item(self):
        id_todo_item = util.get_value(aos="2 / 27 / true / veritatis pariatur delectus", ios="2 / 27 / true / veritatis pariatur delectus")
        util.click(self.driver, AppiumBy.ID, id_todo_item)

    def scroll_up(self):
        util.scroll(self.driver, util.ScrollDirection.UP)

    def scroll_down(self):
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        
        


