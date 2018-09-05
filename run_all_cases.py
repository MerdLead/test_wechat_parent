import sys

sys.path.append('..')
from conf.case_strategy import CaseStrategy
from conf.drivers import Drivers


if __name__ == '__main__':
    cs = CaseStrategy()

    cases = cs.collect_cases()
    # in future, cases_list may be used for testing strategy in multi devices
    Drivers().run(cases)
