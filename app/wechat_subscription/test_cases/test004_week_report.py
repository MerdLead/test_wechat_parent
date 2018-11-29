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
        cls.login.app_status ()  # 判断APP当前状态
        cls.home.click_sub ()  # 进入公众号

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_week_report(self):
        print("\n---学习周报脚本---\n\n")

        if self.home.wait_check_parent_title():
            name = self.account.stu_name_judge()  # 获取备注名
            if self.home.wait_check_parent_title():
                self.home.report_tab()  # 底部 学习报告tab
                self.report.study_week_report()  # 进入 学习周报

                if self.report.wait_check_week_page():  # 页面检查点

                    content1 = self.report.all_element()  # 学习周报 页面所有元素
                    count1 = self.report.homework_all_info(content1[1])  # 作业卷子统计 元素信息判断
                    self.account.compare_name(content1[1][0][:-6], name[0][:8])  # 备注名比较 name[0][:8]备注名前8位

                    self.report_homework_count() #作业卷子统计情况
                    if self.home.wait_check_parent_title():
                        self.home.report_tab()  # 底部 学习报告tab
                        self.report.study_week_report()  # 进入 学习周报
                        if self.report.wait_check_week_page():
                             self.report_wordbook_count(count1) #单词本统计情况
                             self.home.back_to_mainPage()  # 返回主界面


    @testcase
    def judge_report_tbs(self):
        if not self.report.wait_check_report_show():
            self.login.clear_tbs_to_retry()
            if self.home.wait_check_parent_title():
                self.home.report_tab()  # 底部 学习报告tab
                self.report.study_week_report()  # 进入 学习周报
                if self.report.wait_check_week_page():
                    print("返回学习周报页面")
        else:
            print("页面正常")

    @testcase
    def report_homework_count(self):
        self.report.share_button(0)  # 作业卷子统计 -- 晒一下 按钮
        if self.report.wait_check_share_page():  # 页面检查点
            self.report.click_blank()  # 点击空白处 - 使浮层消失
            share = self.report.all_element()  # 作业卷子统计 -- 分享页 所有元素
            self.report.homework_share_all_info(share[1])  # 元素信息判断
        else:
            print("作业无数据统计，分享不可用\n")
        print('----------------------')

        self.home.back_to_club_home()  # 返回


    @testcase
    def report_wordbook_count(self, count1):
        if count1 == 9:  # 上周有 作业卷子统计信息
            self.report.swipe_up(0.5, 0.8, 0.2, 1000)  # 向上滑屏

        content2 = self.report.all_element()  # 学习周报 页面所有元素
        self.report.word_all_info(content2[1])  # 单词本统计 元素信息判断
        if count1 == 9:
            if len(self.report.share_button_count()) == 2:
                self.report.share_button(1)
            elif len(self.report.share_button_count()) == 1:
                self.report.share_button(0)
        if count1 == 3:
            self.report.share_button(1)  # 单词本统计 -- 晒一下 按钮

        if self.report.wait_check_share_page():  # 页面检查点
            self.report.click_blank()  # 点击空白处 - 使浮层消失
            share = self.report.all_element()  # 作业卷子统计 -- 分享页 所有元素
            self.report.word_share_all_info(share[1])  # 元素信息判断
        else:
            print("单词本无数据统计，分享不可用\n")
        print('-----------------------')
