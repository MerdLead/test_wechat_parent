#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI


class GetVariable(object):
    """参数化文档"""

    REPORT_ROOT = 'storges/test_report'  # 测试报告存放路径
    # 以下为 devices.py 配置信息
    APP = '../weixin_1340.apk'
    PLATFORM_VER = '7.1.2'

    # case统计 配置信息
    CASE_PATH = 'app/wechat_subscription/test_cases'
    CASE_PATTERN = 'test004*.py'

    # 以下为 appium_server.py 配置信息
    CMD = "appium -a 127.0.0.1 -p %s -bp 4728 --no-reset"
    SERVER_URL = 'http://127.0.0.1:%s/wd/hub/status'
    SERVER_LOG = 'appium_server_port_%s.log'
    KILL = 'taskkill /PID %d /F'

    # 做题情况统计 Excel表格存放路径
    EXCEL_PATH = 'storges/test_report/games_result_info.xlsx'

