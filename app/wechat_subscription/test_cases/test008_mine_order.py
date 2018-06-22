#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
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

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_order(self):
        self.login.app_status()  # 判断APP当前状态

        self.home.click_sub()  # 进入公众号
        self.home.account_tab()  # 底部 我的账号tab
        self.order.mine_order()  # 进入 我的订单

        if self.order.wait_check_order_page():  # 页面检查点
            content = self.get_all_order()
            self.order.order_info(content)  # 元素信息判断

            self.order.order_details(0)  # 订单详情
            details = self.order.order_all_ele()  # 我的订单 所有元素
            self.order.details_page_info(details[1])  # 元素信息判断

            self.home.buck_up_button()  # 返回主界面

    @teststeps
    def get_all_order(self):
        """获取页面内所有订单的信息"""
        content1 = self.order.order_all_ele()  # 我的订单 所有元素
        self.order.swip_up()
        content2 = self.order.order_all_ele()  # 我的订单 所有元素

        count = []
        var = content1[1][len(content1[1]) - 4]
        if var in content2[1]:
            for i in range(len(content2[1])):
                if content2[1][i] == var:
                    count.append(i)
                    break

            if count[0] != len(content2[1]) - 4:
                content = content1[1] + content2[1][count[0] + 4:]
            else:
                content = content1[1]
        else:
            content = content1[1]
        return content
