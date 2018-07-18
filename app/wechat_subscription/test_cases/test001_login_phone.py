#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os

import time

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.report_page import ReportPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from app.wechat_subscription.object_page.order_page import OrderPage
from app.wechat_subscription.test_data.mine_account import phone_data
from conf.decorator import testcase, setup, teardown, teststeps

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Account(unittest.TestCase):
    """登录测试 - 手机号"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.report = ReportPage()
        cls.account = AccountPage()
        cls.order = OrderPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_login_phone(self):
        self.login.app_status()  # 判断APP当前状态

        self.login.page_source()
        self.home.click_sub()  # 进入公众号
        if self.home.wait_check_page():  # 页面检查点
            self.home.report_tab()  # 点击底部菜单 - 学习报告
            self.report.study_month_report()  # 点击二级标题 学习月报

            if self.home.wait_check_login_page():  # 页面检查点
                self.login_operate_phone()  # 测试手机号
            else:
                self.account.logout_operate()  # 退出登录
                if self.home.wait_check_login_page():  # 页面检查点
                    self.login_operate_phone()  # 测试手机号

            self.home.buck_up_button()  # 返回主界面

    @teststeps
    def login_operate_phone(self):
        """登录 操作流程 - 测试手机号"""
        for i in range(len(phone_data)):
            if self.home.wait_check_login_page():  # 页面检查点
                # if i == 0:
                #     self.home.here_button()
                #     self.home.cancel_button()
                #     if self.home.wait_check_download_page():   # 页面检查点
                #         print('进入下载页')
                #         self.home.buck_up_button()
                #         self.home.report_tab()  # 点击底部菜单 - 学习报告
                #         self.report.study_month_report()  # 点击二级标题 学习月报
                self.login.page_source()
                phone = self.home.login_phone()
                pwd = self.home.login_password()

                phone.click()  # 激活phone输入框
                if len(phone_data[i]['username']) < 12:
                    phone.send_keys(phone_data[i]['username'])  # 输入手机号
                # else:
                #     todo点击键盘

                pwd.click()  # 激活pwd输入框
                pwd.send_keys(phone_data[i]['password'])  # 输入密码

                self.home.login_button()
                if self.home.wait_check_login_page():
                    print('登录失败', phone_data[i]['username'])
                    if phone_data[i]['assert'] not in self.home.page_source():  # toast判断
                        print('★★★ Error- 登录失败toast:',  self.account.page_source())

                    self.home.close_button()  # 点击关闭按钮
                    if i == 0:
                        self.home.report_tab()  # 点击底部菜单 - 学习报告
                        self.report.study_month_report()  # 点击二级标题 学习月报
                    elif i in (1, 3):
                        self.home.report_tab()  # 点击底部菜单 - 学习报告
                        self.report.study_week_report()  # 点击二级标题 学习周报
                    elif i in (2, 5):
                        self.home.buy_tab()  # 点击底部菜单 - 购买
                    elif i in(4, 6):
                        self.home.account_tab()  # 点击底部菜单 - 账号管理
                        self.account.mine_account()  # 点击二级标题 我的账号
                    else:
                        self.home.account_tab()  # 点击底部菜单 - 账号管理
                        self.order.mine_order()  # 点击二级标题 我的订单
                else:
                    print('登录成功')
                    self.account.logout_operate()
                print('----------------------------------')
