#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI

import random

import unittest
import os

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.order_page import OrderPage
from conf.decorator import testcase, setup, teardown, teststeps

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Order(unittest.TestCase):
    """我的订单"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.order = OrderPage()
        cls.login.app_status ()  # 判断APP当前状态
        cls.home.click_sub ()  # 进入公众号

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_order(self):
        print("\n---我的订单脚本---\n\n")
        if self.home.wait_check_parent_title ():
            self.home.account_tab()  # 底部 我的账号tab
            self.order.mine_order()  # 进入 我的订单

            if self.order.wait_check_order_page():  # 页面检查点
                content = self.order.order_all_ele()
                ele_array = self.order.order_info(content)  # 元素信息判断

                ele = self.order.get_details_list()
                index = 1
                ele[index].click()  # 订单详情

                if self.order.wait_check_detail_page():
                    details = self.order.order_all_ele()  # 我的订单 所有元素
                    self.order.details_page_info(details, ele_array[index][1])  # 元素信息判断

                self.home.back_to_mainPage()  # 返回主界面

