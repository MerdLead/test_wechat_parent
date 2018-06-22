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


class DiscountBuy(unittest.TestCase):
    """优惠购买"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.buy = BuyPage()
        cls.discount = DiscountPage()
        cls.account = AccountPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_discount_buy(self):
        self.login.app_status()  # 判断APP当前状态

        self.home.click_sub()  # 进入公众号
        content = self.account.get_info()  # 获取手机号

        self.home.buy_tab()  # 底部 购买tab

        if self.buy.wait_check_page():  # 页面检查点
            self.buy.upgrade_button()  # 马上升级 按钮
            if self.buy.wait_check_page():  # 页面检查点

                if self.buy.discount_buy_button_type():  # 可点击状态
                    self.buy.discount_buy_button()  # 优惠购买
                    if self.discount.wait_check_page():  # 页面检查点
                        buy = self.discount.all_element()  # 购买 页面所有元素
                        count = self.discount.buy_page_info(buy[1])  # 元素信息判断

                        if count == 15:
                            self.switch_card_operate()  # 切换卡片类型

                        if count in (11, 15):
                            self.discount.see_button()  # 去看看 按钮
                            dis_buy = self.discount.all_element()  # 去看看 页面所有元素

                            self.discount.discount_page_info(dis_buy[1])  # 元素信息判断
                            self.discount.group_buy_button()  # 一键开团 按钮
                            group = self.discount.all_element()  # 一键开团 页面所有元素
                            self.discount.group_page_info(group[1])  # 元素信息判断

                            self.stu_login(content[0], stu_data[0]['pwd'])  # 购买页面 登录学生账号信息

                            item = self.discount.all_element()  # 登录后 页面所有元素
                            self.discount.payment_info(item[1])

                            self.webchat_pay_operate()  # 微信支付过程

                        self.home.buck_up_button()  # 返回主界面

    @teststeps
    def switch_card_operate(self):
        """切换卡片类型"""
        self.discount.checkbox_1()  # 半年卡
        if self.discount.card_type() != '半年卡':
            print('--------------------------------')
            print('★★★ Error- 卡片类型显示错误:', self.buy.card_type())

        self.discount.checkbox_2()  # 年卡
        if self.discount.card_type() != '年卡':
            print('★★★ Error- 卡片类型显示错误:', self.buy.card_type())
            print('--------------------------------')

    @teststeps
    def stu_login(self, username, pwd):
        """购买页面 登录学生账号信息"""
        account = self.discount.stu_account_pwd()  # 学生账号  学生密码
        account[0].click()
        account[0].send_keys(username)

        self.discount.tap_blank()  # 点击空白处-- 因为焦点在输入框中时，获取不到元素信息
        account[1].click()
        account[1].send_keys(pwd)
        self.discount.commit_button()  # 确定按钮

    @teststeps
    def webchat_pay_operate(self):
        """微信支付"""
        self.discount.now_payfor_button()  # 立即支付按钮
        if self.discount.wait_check_pay_page():  # 页面检查点
            self.discount.close_button()  # 关闭 微信支付页面

            # self.discount.now_payfor_button()  # 立即支付按钮
            # if self.discount.wait_check_pay_page():  # 页面检查点
            #     self.discount.pay_operate()  # 支付操作
            #
            #     if self.discount.wait_check_finish_page():  # 页面检查点
            #         content = self.discount.all_element()  # 支付完成 页面所有元素
            #         self.discount.finish_page_info(content[1])  # 元素信息判断
