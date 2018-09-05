#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from app.wechat_subscription.object_page.report_page import ReportPage
from conf.decorator import testcase, setup, teardown

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class MonthReport(unittest.TestCase):
    """学习月报"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.report = ReportPage()
        cls.account = AccountPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_month_report(self):
        print("\n\n---学习月报脚本---\n\n")
        self.login.app_status()  # 判断APP当前状态
        self.home.click_sub()  # 进入公众号

        if self.home.wait_check_parent():
            name = self.account.stu_name_judge()  # 获取备注名
            print(name)
            if self.home.wait_check_parent():
                self.home.report_tab()  # 底部 学习报告tab
                self.report.study_month_report()  # 进入 学习月报

                if self.report.wait_check_month_page():  # 页面检查点
                    self.judge_report_tbs()  # 判断内核是否存在

                    content1 = self.report.all_element()  # 学习月报 页面所有元素
                    self.report.month_all_info(content1[1]) #学习月报页面元素校验
                    self.account.compare_name(content1[1][0][:-6],name[0][:8])  # 备注名比较 name[0][:8]备注名前8位

                    month = self.report.month()  # 月份
                    value = month.get_attribute('contentDescription')
                    if value!= '8月':
                        print('★★★ Error - 展示的月份不是当前月份', month.text)

                    self.report.share_button(0)  # 晒一下 按钮
                    if self.report.wait_check_share_page():  # 页面检查点
                        self.report.click_blank()  # 点击空白处 - 使浮层消失
                        share = self.report.all_element()  # 分享页 所有元素
                        self.report.month_share_all_info(share[1])  # 元素信息判断

                        # self.account.compare_name(share[1][1], name[0])  # 备注名比较
                    else:
                        print("\n无数据统计\n")
                        print('-----------------------')
                    self.home.back_to_mainPage()  # 返回主界面

    @testcase
    def judge_report_tbs(self):
        if not self.report.wait_check_report_show():
            self.login.clear_tbs_to_retry()
            if self.home.wait_check_parent():
                self.home.report_tab()  # 底部 学习报告tab
                self.report.study_month_report()  # 进入 学习月报
                if self.report.wait_check_month_page():
                    print("返回学习月报页面")
        else:
            print("页面元素正常")
