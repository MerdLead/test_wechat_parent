#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.buy_page import BuyPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from conf.decorator import testcase, setup, teardown

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class DirectBuy(unittest.TestCase):
    """直接购买"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.buy = BuyPage()
        cls.account = AccountPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_direct_buy(self):
        self.login.app_status()  # 判断APP当前状态

        self.home.click_sub()  # 进入公众号
        name = self.account.stu_name_judge()  # 获取备注名
        self.home.buy_tab()  # 底部 购买tab

        if self.buy.wait_check_page():  # 页面检查点
            self.buy.swipe_up()
            magic = self.buy.all_element()  # 法宝 页面所有元素
            self.buy.magic_page_info(magic[1])  # 元素信息判断

            self.account.compare_name(magic[1][0], name[0])  # 备注名比较

            if magic[1][1] != name[1]:  # 手机号比较
                print('★★★ Error - 法宝页面展示的学生手机号:', magic[1][1])

            self.buy.upgrade_button()  # 马上升级 按钮
            if self.buy.wait_check_page():  # 页面检查点
                content = self.buy.all_element()  # 购买 页面所有元素
                self.buy.buy_page_info(content[1])  # 元素信息判断

                self.account.compare_name(content[1][0], name[0])  # 备注名比较

                if content[1][1] != name[1]:  # 手机号比较
                    print('★★★ Error - 法宝页面展示的学生手机号:', content[1][1])

                self.buy.direct_buy_button()  # 直接购买
                if self.buy.wait_check_page():  # 页面检查点
                    payment = self.buy.all_element()  # 购买 页面所有元素
                    self.buy.direct_payment_info(payment[1])  # 元素信息判断

                    self.account.compare_name(payment[1][0], name[0])  # 备注名比较

                    if payment[1][1] != name[1]:  # 手机号比较
                        print('★★★ Error - 法宝页面展示的学生手机号:', payment[1][1])

                    self.buy.online_service()  # 在线客服按钮
                    self.buy.close_button()  # 关闭按钮oK

                    self.buy.commit_button()  # 确认支付 按钮
                    if self.buy.wait_check_pay_page():  # 页面检查点
                        # self.buy.pay_operate()  # 支付操作
                        self.buy.close_pay_button()  # 关闭 微信支付页面

                    self.home.buck_up_button()  # 返回主界面
