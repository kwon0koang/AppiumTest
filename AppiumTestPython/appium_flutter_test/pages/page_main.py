import util.util as util
from pages.page_base import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MainPage(BasePage):

    def click_todo_list(self):
        id_todo_list = util.get_value(aos="Todo list", ios="Todo list")
        util.click(self.driver, AppiumBy.ID, id_todo_list)


