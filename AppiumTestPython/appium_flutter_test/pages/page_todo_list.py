import util.util as util
from pages.page_base import BasePage
from appium.webdriver import webdriver

class TodoListPage(BasePage):

    def send_keys_filter_text(self):
        xpath_filter_text = util.get_element(aos="//android.widget.EditText", ios="//XCUIElementTypeTextField[@name=\"Filter text\"]")
        util.click_element_by_xpath(self.driver, xpath_filter_text)
        util.send_keys_element_by_xpath(self.driver, xpath_filter_text, "veritatis pariatur delectus")
        self.driver.hide_keyboard()
        # driver.press_keycode(4) // back key

    def click_todo_item(self):
        id_todo_item = util.get_element(aos="2 / 27 / true / veritatis pariatur delectus", ios="2 / 27 / true / veritatis pariatur delectus")
        util.click_element_by_id(self.driver, id_todo_item)

    def scroll_up(self):
        util.scroll(self.driver, util.ScrollDirection.UP)

    def scroll_down(self):
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        
        


