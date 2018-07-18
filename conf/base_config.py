#!/usr/bin/env python
# code:UTF-8
# @Author  : SUN FEIFEI


class GetVariable(object):
    """参数化文档"""

    REPORT_ROOT = 'storges/test_report'  # 测试报告存放路径

    # 以下为 微信 devices.py 配置信息
    APP = '../weixin_1300.apk'
    PACKAGE = 'com.tencent.mm'
    ACTIVITY = ".ui.LauncherUI"
    PLATFORM = '5.1'

    # case统计 配置信息
    SUIT_PATH = 'app'
    CASE_PATH = 'app/wechat_subscription/test_cases'
    CASE_PATTERN = 'test001*.py'
