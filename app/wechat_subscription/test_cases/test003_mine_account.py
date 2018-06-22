#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from app.wechat_subscription.test_data.remark import remark_data
from conf.decorator import testcase, setup, teardown, teststeps

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class MineAccount(unittest.TestCase):
    """我的账号"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login = LoginPage()
        cls.account = AccountPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_mine_account(self):
        if self.account.wait_check_account_page():  # 我的账号 页面检查点
            print('在 我的账号 页面：')
        else:
            self.login.app_status()  # 判断APP当前状态

            self.home.click_sub()  # 进入公众号
            self.home.account_tab()  # 底部 我的账号tab
            self.account.mine_account()  # 进入 我的账号

        if self.account.wait_check_account_page():   # 页面检查点
            content = self.account.account_all_ele()  # 所有元素
            self.account.account_info(content[1])  # 元素信息判断

            self.receive_remind_operate()  # 接收作业提醒
            self.modify_remark_operate()  # 修改备注

        self.home.buck_up_button()  # 返回主界面

    @teststeps
    def receive_remind_operate(self):
        """接收作业提醒"""
        print('-----------------------------------')
        button = self.account.checkbox_button()  # 接收作业提醒 选择框
        value = button.get_property('value')
        if value['checked'] == "False":
            print('★★★ Error - 接收作业提醒 选择框 未被 默认 打开')
        else:
            button.click()  # 关闭 选择框
            value1 = button.get_property('value')
            if value1['checked'] == "True":
                print('★★★ Error - 接收作业提醒 选择框 未被关闭')
            else:
                button.click()  # 打开 选择框
        print('-----------------------------------')

    @teststeps
    def modify_remark_operate(self):
        for i in range(len(remark_data)):
            self.account.remark_name()  # 点击 弹出修改备注名 弹框

            self.account.tap_blank()  # 点击空白处-- 因为焦点在输入框中时，获取不到元素信息
            remark = self.account.remark_edittext()  # 请输入备注名 输入框
            remark.click()   # 激活输入框
            # DelEditText().del_text(remark)   # 删除文本框中内容-- 无需删除，自动覆盖
            remark.send_keys(remark_data[i]['remark'])  # 输入备注名
            print('修改备注为:', remark_data[i]['remark'])
            self.account.confirm_button()  # 点击确定按钮

            if self.account.wait_check_remark_page():
                print('修改备注 失败')
                for j in range(3):
                    self.account.confirm_button()  # 多次 点击确定按钮
                if remark_data[i]['assert'] not in self.home.page_source():  # toast判断
                    print('★★★ Error- 没有tips:',  self.account.page_source())

                self.account.cancel_button()  # 点击取消按钮
            else:
                if self.account.wait_check_remark_tips_page():  # 若修改备注名成功的弹框文案存在
                    self.account.confirm()  # 点击确定按钮
                    print('修改备注名成功')

                    item = self.account.remark()  # 获取 备注名
                    name = item.get_property('value')
                    if name['description'] != remark_data[i]['remark']:
                        if remark_data[i]['remark'] in ('', ' ', '    '):
                            if name['description'] != '未设置':
                                print('★★★ Error - 备注名 未保存成功')
                        else:
                            print('★★★ Error - 备注名 未保存成功')

            if self.account.wait_check_account_page() is False:  # 页面检查点
                print('★★★ Error - 未进入我的账号 页面')
            print('---------------------------------------')
