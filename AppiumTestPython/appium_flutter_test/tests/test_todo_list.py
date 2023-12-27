import time
import config
from pages.page_main import MainPage
from pages.page_todo_list import TodoListPage
import util.util as util
from tests.test_base import BaseTest
import sys
import unittest

class TodoListTest(BaseTest):

    def setUp(self) -> None:
        if util.get_platform() == util.Platform.AOS:
            super().setUp(app_package="com.example.test_flutter", app_activity=".MainActivity")
        else:
            super().setUp(bundle_id="com.kykdev.testFlutter")
        
    def test_todo_list(self) -> None:
        main_page = MainPage(self.driver)
        main_page.click_todo_list()
        
        todo_list_page = TodoListPage(self.driver)
        time.sleep(2)
        todo_list_page.scroll_down()
        todo_list_page.scroll_up()
        todo_list_page.send_keys_filter_text()
        todo_list_page.check_todo_item()
        todo_list_page.click_todo_item()
        
        time.sleep(0.5)
        
