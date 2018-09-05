#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.buy_page import BuyPage
from conf.decorator import testcase, setup, teardown, teststeps

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Buy(unittest.TestCase):
    """直接购买 - 切换card"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.buy = BuyPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_direct_buy_switch(self):

        print("\n\n---优惠卡切换脚本---\n\n")
        self.login.app_status()  # 判断APP当前状态
        self.home.click_sub()  # 进入公众号
        self.home.buy_tab()  # 底部 购买tab
        self.judge_buy_tbs()

        self.buy.upgrade_button()  # 马上升级 按钮
        if self.buy.wait_check_page():  # 页面检查点
            self.switch_card_operate()  # 切换卡片类型
            self.buy.online_service()  # 在线客服按钮
            self.buy.close_button()  # 关闭按钮oK

            self.buy.direct_buy_button()  # 直接购买
            if self.buy.wait_check_page():  # 页面检查点

                self.buy.pay_for_another()  # 家长代付
                self.buy.commit_button()  # 确认支付 按钮
                if self.buy.wait_check_pay_another_page():  # 页面检查点
                    another = self.buy.all_element()  # 家长代付 页面所有元素
                    self.buy.pay_another_info(another)  # 元素信息判断

                self.home.back_to_mainPage()  # 返回主界面
    @teststeps
    def switch_card_operate(self):
        """切换卡片类型"""
        print('--------------------------------')


        self.buy.checkbox_1()
        ele =  self.buy.get_RadioButtons()
        month_card = self.buy.card_type(0)

        if month_card != '月卡':
            print('★★★ Error- 卡片类型显示错误:',month_card)
        else:
            print('切换到：', month_card)

        self.buy.checkbox_2()
        quarter_card = self.buy.card_type(1)
        if quarter_card != '季卡':
            print('★★★ Error- 卡片类型显示错误:',quarter_card)
        else:
            print('切换到：', quarter_card)

        self.buy.checkbox_3()
        half_card = self.buy.card_type(2)
        if half_card!= '半年卡':
            print('★★★ Error- 卡片类型显示错误:', half_card)
        else:
            print('切换到：', half_card)

        ele[3].click()
        year_card = self.buy.card_type(3)
        if year_card != '年卡':
            print('★★★ Error- 卡片类型显示错误:', year_card)
        else:
            print('切换到：', year_card)
        print('--------------------------------')


    @testcase
    def judge_buy_tbs(self):
        if self.buy.wait_check_page():  # 页面检查点
            if not self.buy.wait_check_upgrade_button():
                self.login.clear_tbs_to_retry()
                if self.home.wait_check_parent():
                    self.home.click_sub()  # 进入公众号
                    self.home.buy_tab()  # 底部 购买tab
            else:
                print("页面元素定位正常")


