import util
from pages.base_page import BasePage
from appium import webdriver
from appium.webdriver import webdriver


class TodoListPage(BasePage):
        
    xpath_filter_text = util.get_element(aos="//android.widget.EditText", ios="todo")
    id_todo_item = util.get_element(aos="2 / 27 / true / veritatis pariatur delectus", ios="todo")

    def send_keys_filter_text(self):
        util.click_element_by_xpath(self.driver, TodoListPage.xpath_filter_text)
        util.send_keys_element_by_xpath(self.driver, TodoListPage.xpath_filter_text, "veritatis pariatur delectus")
        self.driver.hide_keyboard()
        # driver.press_keycode(4) // back key

    def click_todo_item(self):
        util.click_element_by_id(self.driver, TodoListPage.id_todo_item)

    def scroll_down(self):
        util.scroll(self.driver, util.ScrollDirection.DOWN)
        
        


