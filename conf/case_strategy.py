import os
import unittest
from conf.base_config import GetVariable as gv


class CaseStrategy:
    def _collect_cases(self, cases, top_dir=None):
            # 构造测试集  defaultTestLoader（）即TestLoader（）测试用例加载器，包括多个加载测试用例的方法，返回一个测试套件

            suites = unittest\
                .defaultTestLoader.discover(gv.CASE_PATH, pattern=gv.CASE_PATTERN, top_level_dir=top_dir)
            for suite in suites:
                for case in suite:
                    cases.addTest(case)

    def collect_cases(self, suite=False):
        """collect cases
        collect cases from the giving path by case_path via the giving pattern by case_pattern
        return: all cases that collected by the giving path and pattern, it is a unittest.TestSuite()
        """
        cases = unittest.TestSuite()

        if suite:
            test_suites = []
            for file in os.listdir(gv.CASE_PATH):
                if gv.CASE_PATH in file:
                    if os.path.isdir(file):  # os.path.isdir()函数判断某一路径是否为目录
                        test_suites.append(file)
            for test_suite in test_suites:
                self._collect_cases(cases, top_dir=test_suite)
        else:
            self._collect_cases(cases, top_dir=None)
        print(cases)
        return cases
