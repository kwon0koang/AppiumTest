import util
from pages.base_page import BasePage


class MainPage(BasePage):

    id_todo_list = util.get_element(aos="Todo list", ios="todo")

    def click_todo_list(self):
        util.click_element_by_id(self.driver, MainPage.id_todo_list)


