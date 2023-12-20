import util.util as util
from pages.page_base import BasePage


class MainPage(BasePage):

    def click_todo_list(self):
        id_todo_list = util.get_value(aos="Todo list", ios="Todo list")
        util.click_by_id(self.driver, id_todo_list)


