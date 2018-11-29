#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.buy_page import BuyPage
from app.wechat_subscription.object_page.discount_page import DiscountPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from app.wechat_subscription.test_data.student_pay_info import stu_data
from conf.decorator import testcase, setup, teardown, teststeps


class Buy(unittest.TestCase):
    """优惠购买 - 立即支付"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.buy = BuyPage()
        cls.discount = DiscountPage()
        cls.account = AccountPage()
        cls.login.app_status ()  # 判断APP当前状态
        cls.home.click_sub ()  # 进入公众号

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_discount_buy_now(self):
        print("\n---立即购买脚本---\n\n")
        if self.home.wait_check_parent_title():
            self.home.buy_tab()  # 底部 购买tab
            if self.buy.wait_check_page():  # 页面检查点
                self.buy.upgrade_button()  # 马上升级 按钮
                if self.buy.wait_check_page():  # 页面检查点

                    if self.buy.discount_buy_button_type() == 'true':  # 可点击状态
                        self.buy.discount_buy_button()  # 优惠购买

                        if self.discount.wait_check_dicount_page():
                            buy = self.discount.all_element(self.discount.get_view_ele())  # 购买 页面所有元素
                            self.discount.discount_card_info(buy[1])  # 元素信息判断
                            self.discount.buy_now_button()  # 立即购买 按钮
                            self.login_to_buy_card()

                            if self.discount.wait_check_dicount_page():
                                if self.discount.wait_check_group_tip():
                                    self.group_buy_operate()   # 拼团购买

                            self.home.back_to_mainPage()

    @teststeps
    def group_buy_operate(self):
        print('-'*15+'拼团购买'+'-'*15)
        self.discount.see_button()
        if self.discount.wait_check_year_card_page():
            all_ele = self.discount.all_element(self.discount.get_view_ele())
            self.discount.group_ele_operate(all_ele[1])
            self.discount.group_key_button()
            self.login_to_buy_card()

    @teststeps
    def login_to_buy_card(self):
        if self.discount.wait_check_buycard_page():  # 页面检查点
            dis_buy = self.discount.all_element(self.discount.get_view_ele())  # 立即购买 页面所有元素
            self.discount.buy_now_page_info(dis_buy[1])  # 元素信息判断

            self.stu_login(stu_data[0]['account'], stu_data[0]['pwd'])  # 购买页面 登录学生账号信息
            if self.discount.wait_check_user_image():  # 页面检查点
                item = self.discount.all_element(self.discount.get_view_ele())  # 登录后 页面所有元素
                self.discount.payment_info(item[1])
                self.webchat_pay_operate()  # 微信支付过程


    @teststeps
    def stu_login(self, username, pwd):
        """购买页面 登录学生账号信息"""
        inputs = self.discount.stu_phone_pwd()
        inputs[0].click()
        inputs[0].send_keys(username)

        inputs[1].click()
        inputs[1].send_keys(pwd)

        self.discount.commit_button()  # 确定按钮

    @teststeps
    def webchat_pay_operate(self):
        """微信支付"""
        self.discount.pay_now_button()  # 立即支付按钮
        if self.buy.wait_check_confirm_pay_page():
            item = self.discount.all_element(self.discount.get_text_view_ele())
            self.buy.pay_text_operate(item[1])
            self.home.back_to_club_home()
            if self.discount.wait_check_user_image():
                self.discount.back_to_discount_page()

        elif self.discount.wait_check_pay_page():  # 页面检查点
            self.discount.close_button()  # 关闭 微信支付页面


