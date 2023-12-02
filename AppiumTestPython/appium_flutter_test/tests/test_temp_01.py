import time
import unittest
from pages.page_main import MainPage
from tests.test_base import BaseTest

class Temp01Test(BaseTest):

    def test_temp_01(self) -> None:
        time.sleep(0.5)
        
    def test_error(self):
        raise ValueError("에러 테스트 :)")

    @unittest.skip("스킵 테스트 :)")
    def test_skip(self):
        pass
    
    # def test_fail(self):
    #     self.assertEqual(1, 2)