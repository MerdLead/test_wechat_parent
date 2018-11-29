#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os
import time


from selenium.webdriver.common.by import By


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
        cls.login.app_status ()  # 判断APP当前状态
        cls.home.click_sub ()  # 进入公众号
    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_login_pwd(self):

        print("\n---验证密码脚本---\n\n")
        if self.home.wait_check_parent_title():  # 公众号页面标题检查点
            self.home.account_tab()
            self.account.mine_account()

            if self.home.wait_check_login_page(): #登录页面检查点
                print("用户未登录，进行登录校验操作\n")
                self.login_operate_pwd()     # 测试密码
            elif self.account.wait_check_account_page():
                print("已登录，退出重新登录")
                self.account.logout_operate()  # 退出登录
                if self.home.wait_check_login_page():
                    self.login_operate_pwd()  # 测试密码
            else:
                print("ERROR！页面标题不正确！")
        self.home.back_to_mainPage()  # 返回主界面

    @teststeps
    def login_operate_pwd(self):
        """登录 操作流程 - 测试密码"""
        for i in range(0,len(pwd_data)):

            if self.home.wait_check_login_page():
                phone = self.home.ele_input_text()[0]
                pwd = self.home.ele_input_text()[1]

                phone.click()
                phone.send_keys(pwd_data[i]['username'])  # 输入手机号

                pwd.click()
                pwd.send_keys(pwd_data[i]['password'])  # 输入密码
                if i in (1,4):
                    self.show_display_pwd(i)

                self.home.login_button()
                self.login.check_login_error_info(pwd_data[i]['assert'])   #检查toast信息

                if self.home.wait_check_login_page():
                    print("用户名：",pwd_data[i]['username'], "\n密码：",pwd_data[i]['password'])
                    self.home.back_to_club_home()  # 点击关闭按钮

                    if self.home.wait_check_parent_title():
                        if i == 0:
                            self.home.report_tab()  # 点击底部菜单 - 学习报告
                            self.report.study_month_report()  # 点击二级标题 学习月报
                        elif i in (1, 3):
                            self.home.report_tab()  # 点击底部菜单 - 学习报告
                            self.report.study_week_report()  # 点击二级标题 学习周报
                        elif i == 4:
                            self.home.buy_tab()  # 点击底部菜单 - 购买
                        elif i == 5:
                            self.home.account_tab()  # 点击底部菜单 - 账号管理
                            self.order.mine_order()  # 点击二级标题 我的订单
                        else:
                            self.home.account_tab()  # 点击底部菜单 - 账号管理
                            self.account.mine_account()  # 点击二级标题 我的账号
                else:
                    print('登录成功',"\n用户名：",pwd_data[i]['username'], "\n密码：",pwd_data[i]['password'])
                    if i != len(pwd_data) - 1:
                        self.account.logout_operate()  # 退出登录 具体操作
            print('----------------------------------')

    @teststeps
    def show_display_pwd(self, i):
        """显示与隐藏密码"""
        self.home.show_password()  # 显示密码 按钮
        pwd1 = self.home.ele_input_text()[1]
        value = pwd1.text
        if pwd_data[i]['password'].strip() == "":
            pwd_data[i]['password']="请输入密码"

        if value != pwd_data[i]['password']:
            print('★★★ Error- 密码显示失败')
        else:
            print("密码显示成功")
        if pwd_data[i]['password'] == "请输入密码":
            pwd_data[i]['password'] = ""
