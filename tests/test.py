import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import util.util as util
import HtmlTestRunner
import sys
import unittest
from tests.test_todo_list import TodoListTest
from tests.test_temp_01 import Temp01Test

# 파이썬 스크립트가 직접 실행될 때 해당 블록 안의 코드를 실행
# 모듈로 사용할 때(다른 스크립트로부터 import 되었을 때)는 실행 X
if __name__ == '__main__':
    # unittest.main()
    
    args = util.get_args(sys.argv)
    suite = util.load_tests(args, TodoListTest)
    suite2 = util.load_tests(args, Temp01Test)
    suites = unittest.TestSuite([suite, suite2])
    
    # 테스트 실행
    # unittest.TextTestRunner().run(suites)
    
    # 테스트 실행 및 report 생성
    HtmlTestRunner.HTMLTestRunner(
        output = "reports", # report 넣을 폴더명
        report_name = f"report_{args.device}", # report html 파일명
        report_title = "Test Results", # report 제목
        combine_reports = True # report 합치기
    ).run(suites)
    

