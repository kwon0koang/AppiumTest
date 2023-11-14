import util
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_todo_list(self):
        id_todo_list = util.get_element(aos="Todo list", ios="Todo list")
        util.click_element_by_id(self.driver, id_todo_list)


