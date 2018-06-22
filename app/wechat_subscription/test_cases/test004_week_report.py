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


class WeekReport(unittest.TestCase):
    """学习周报"""

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
    def test_week_report(self):
        self.login.app_status()  # 判断APP当前状态

        self.home.click_sub()  # 进入公众号
        name = self.account.stu_name_judge()  # 获取备注名

        self.home.report_tab()  # 底部 学习报告tab
        self.report.study_week_report()  # 进入 学习周报

        if self.report.wait_check_week_page():  # 页面检查点
            content1 = self.report.all_element()  # 学习周报 页面所有元素
            count1 = self.report.homework_all_info(content1[1])  # 作业卷子统计 元素信息判断

            self.account.compare_name(content1[1][0], name[0][:8])  # 备注名比较

            if count1 == 9:   # 上周有 作业卷子统计信息
                self.report.share_button(0)  # 作业卷子统计 -- 晒一下 按钮
                if self.report.wait_check_share_page():  # 页面检查点
                    self.report.click_blank()  # 点击空白处 - 使浮层消失
                    share = self.report.all_element()  # 作业卷子统计 -- 分享页 所有元素
                    self.report.homework_share_all_info(share[1])  # 元素信息判断
                    self.home.buck_up_button()  # 返回
            else:
                self.home.buck_up_button()  # 返回

            self.home.report_tab()  # 底部 学习报告tab
            self.report.study_week_report()  # 进入 学习周报

            if self.report.wait_check_week_page():  # 页面检查点
                if count1 == 9:  # 上周有 作业卷子统计信息
                    self.report.swipe_up()  # 向上滑屏
                content2 = self.report.all_element()  # 学习周报 页面所有元素
                count2 = self.report.word_all_info(content2[1])  # 单词本统计 元素信息判断

                if count2 == 3:  # 提分版
                    if count1 == 9:  # 上周有 作业卷子统计信息
                        self.report.share_button(0)  # 单词本统计 -- 晒一下 按钮
                    else:
                        self.report.share_button(1)  # 单词本统计 -- 晒一下 按钮
                    if self.report.wait_check_share_page():  # 页面检查点
                        self.report.click_blank()  # 点击空白处 - 使浮层消失
                        share = self.report.all_element()  # 作业卷子统计 -- 分享页 所有元素
                        self.report.word_share_all_info(share[1])  # 元素信息判断
                else:  # 基础版
                    self.home.buck_up_button()  # 返回主界面
