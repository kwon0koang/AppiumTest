import time
import unittest
from pages.main_page import MainPage
from base_test import BaseTest

class Temp02Test(BaseTest):

    def test_temp_01(self) -> None:
        time.sleep(0.5)
        
    def test_error(self):
        raise ValueError("에러 테스트 :)")

    @unittest.skip("스킵 테스트 :)")
    def test_skip(self):
        pass
    
    # def test_fail(self):
    #     self.assertEqual(1, 2)
        
