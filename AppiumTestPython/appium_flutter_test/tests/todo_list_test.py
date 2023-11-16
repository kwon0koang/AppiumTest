import time
from pages.main_page import MainPage
from pages.todo_list_page import TodoListPage
import util
from base_test import BaseTest
import sys
import unittest

class TodoListTest(BaseTest):

    def test_todo_list(self) -> None:
        main_page = MainPage(self.driver)
        main_page.click_todo_list()
        
        todo_list_page = TodoListPage(self.driver)
        time.sleep(2)
        todo_list_page.scroll_down()
        todo_list_page.scroll_up()
        todo_list_page.send_keys_filter_text()
        todo_list_page.click_todo_item()
        
        time.sleep(0.5)
        
