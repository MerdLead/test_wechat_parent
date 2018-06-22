#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os
import time

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from app.wechat_subscription.object_page.order_page import OrderPage
from app.wechat_subscription.object_page.report_page import ReportPage
from app.wechat_subscription.test_data.mine_account import pwd_data
from conf.decorator import testcase, setup, teardown, teststeps

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Account(unittest.TestCase):
    """登录测试 - 密码"""

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
    def test_login_pwd(self):
        if self.home.wait_check_login_page():  # 页面检查点
            print('在 登录 界面：')
        else:
            self.login.app_status()  # 判断APP当前状态

            self.home.click_sub()  # 进入公众号
            self.home.report_tab()  # 点击底部菜单 - 学习报告
            self.report.study_month_report()  # 点击二级标题 学习月报

        if self.home.wait_check_login_page():  # 页面检查点
            self.login_operate_pwd()  # 测试密码
        else:
            self.account.logout_operate()  # 退出登录 具体操作
            if self.home.wait_check_login_page():  # 页面检查点
                self.login_operate_pwd()  # 测试密码

        self.home.buck_up_button()  # 返回主界面

    @teststeps
    def login_operate_pwd(self):
        """登录 操作流程 - 测试密码"""
        time.sleep(2)
        for i in range(len(pwd_data)):
            if self.home.wait_check_login_page():  # 页面检查点
                phone = self.home.login_phone()
                pwd = self.home.login_password()

                phone.click()
                phone.send_keys(pwd_data[i]['username'])  # 输入手机号

                pwd.click()
                pwd.send_keys(pwd_data[i]['password'])  # 输入密码

                if i == 2:
                    self.home.show_password()  # 显示密码 按钮
                    pwd1 = self.home.login_password()
                    print('显示密码:', pwd1.text)
                    if pwd1.text != '123456789':
                        print('★★★ Error- 明文显示密码失败:', pwd1.text)

                    self.home.show_password()  # 显示密码 按钮
                    pwd2 = self.home.login_password()
                    print('显示密码:', pwd2.text)
                    if pwd2.text != '•••••••••':
                        print('★★★ Error- 密文显示密码失败:', pwd2.text)

                self.home.login_button()
                if self.home.wait_check_login_page():
                    print('登录失败', pwd_data[i]['username'], pwd_data[i]['password'])
                    if pwd_data[i]['assert'] not in self.home.page_source():  # toast判断
                        print('★★★ Error- 登录失败toast:', self.account.page_source())
                    else:
                        if len(pwd_data[i]) == 4:
                            if pwd_data[i]['assertpwd'] not in self.home.page_source():
                                print('★★★ Error- 登录失败 无密码toast:', self.account.page_source())

                    self.home.close_button()  # 点击关闭按钮
                    if i == 0:
                        self.home.report_tab()  # 点击底部菜单 - 学习报告
                        self.report.study_month_report()  # 点击二级标题 学习月报
                    elif i in (1, 3):
                        self.home.report_tab()  # 点击底部菜单 - 学习报告
                        self.report.study_week_report()  # 点击二级标题 学习周报
                    elif i in (2, 5):
                        self.home.buy_tab()  # 点击底部菜单 - 购买
                    elif i in (4, 6):
                        self.home.account_tab()  # 点击底部菜单 - 账号管理
                        self.account.mine_account()  # 点击二级标题 我的账号
                    else:
                        self.home.account_tab()  # 点击底部菜单 - 账号管理
                        self.order.mine_order()  # 点击二级标题 我的订单
                else:
                    print('登录成功')
                    if i != len(pwd_data)-1:
                        self.account.logout_operate()  # 退出登录 具体操作
                print('----------------------------------')
