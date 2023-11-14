import time
from pages.main_page import MainPage
from pages.todo_list_page import TodoListPage
import util
from base_test import BaseTest

class TodoListTest(BaseTest):

    def test_todo_list(self) -> None:
        
        id_todo_list = util.get_element(aos="Todo list", ios="todo")
        util.click_element_by_id(self.driver, id_todo_list)
        
        xpath_filter_text = util.get_element(aos="//android.widget.EditText", ios="todo")
        util.click_element_by_xpath(self.driver, xpath_filter_text)
        util.send_keys_element_by_xpath(self.driver, xpath_filter_text, "veritatis pariatur delectus")
        self.driver.hide_keyboard()
        
        id_todo_item = util.get_element(aos="2 / 27 / true / veritatis pariatur delectus", ios="todo")
        util.click_element_by_id(self.driver, id_todo_item)
        
        time.sleep(1)
        
        # POM 적용 후 ==============================================================
        # main_page = MainPage(self.driver)
        # main_page.click_todo_list()
        
        # todo_list_page = TodoListPage(self.driver)
        # todo_list_page.send_keys_filter_text()
        # todo_list_page.click_todo_item()
        
        # time.sleep(1)

        # todo kyk iOS 테스트 성공 ===================================================
        # xpath_touch = util.get_element(aos="todo", ios="//XCUIElementTypeStaticText[@name=\"Touch\"]")
        # util.click_element_by_xpath(driver, xpath_touch)
        # id_touchable_view = util.get_element(aos="todo", ios="touchableView")
        # util.click_element_by_id(driver, id_touchable_view)
        # time.sleep(1)
        