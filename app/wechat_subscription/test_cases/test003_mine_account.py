#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
import unittest
import os


from selenium.webdriver.common.by import By


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
        cls.login.app_status ()  # 判断APP当前状态
        cls.home.click_sub ()  # 进入公众号


    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_mine_account(self):
        print("\n---我的账号脚本---\n\n")
        if self.home.wait_check_parent_title():
            self.home.account_tab()
            self.account.mine_account()

            if self.account.wait_check_account_page():  # 我的账号 页面检查点
                print('在 我的账号 页面：')
                # self.jude_tbs_is_exit()       #判断tbs是否存在
                self.get_change_accountEle()  #接收页面元素
            elif self.home.wait_check_login_page():
                print("在 登录 页面")
                # self.jude_tbs_is_exit()        #判断tbs是否存在
                if self.home.wait_check_login_page():
                    self.login_mine_account( ) #登录账号
                if self.account.wait_check_account_page():
                    self.get_change_accountEle() #获取页面元素信息
                else:
                    print("ERROR！登录未成功")

    @testcase
    def jude_tbs_is_exit(self):
        """"判断tbs是否存在"""
        if not self.home.wait_check_button():
            self.login.clear_tbs_to_retry()
            self.home.account_tab()
            self.account.mine_account()
        else:
            print("已在登录或账号页面")

    @testcase
    def get_change_accountEle(self):
        """获取页面元素及更改备注"""
        content = self.account.account_all_ele()  # 所有元素
        self.account.account_info(content)  # 元素信息判断
        self.receive_remind_operate()  # 接收作业提醒
        self.modify_remark_operate()  # 修改备注
        self.home.back_to_mainPage()  # 返回主界面


    @testcase
    def login_mine_account(self):
        """登录账号"""
        phone = self.home.ele_input_text()[0]
        pwd = self.home.ele_input_text()[1]
        phone.click()  # 激活phone输入框
        phone.send_keys('18011111115')  # 输入手机号
        pwd.click()  # 激活pwd输入框
        pwd.send_keys('1115')  # 输入密码
        self.home.login_button()


    @teststeps
    def receive_remind_operate(self):
        """接收作业提醒"""
        value = self.account.checkbox_button().get_attribute('checked')   # 接收作业提醒 选择框check属性
        if value == "false":
            print('接收作业提醒 选择框 未被 默认 打开')
            self.account.checkbox_button().click()
        else:
            self.account.checkbox_button().click()  # 关闭 选择框
            value1 =  self.account.checkbox_button().get_attribute('checked')
            if value1 == "true":
                print('接收作业提醒 选择框 未被关闭')
            else:
                self.account.checkbox_button().click()  # 打开 选择框


    @teststeps
    def modify_remark_operate(self):
        """备注校验"""
        for i in range(len(remark_data)):
            self.account.remark_name()  # 点击 弹出修改备注名 弹框

            if self.account.wait_check_remark_name():
                remark = self.account.remark_edittext()  # 请输入备注名 输入框
                remark.click()   # 激活输入框
                remark.clear()   #备注名清除
                remark.send_keys(remark_data[i]['remark'])  # 输入备注名

                self.account.confirm_button()  # 点击确定按钮
                print('修改备注为:', remark_data[i]['remark'])

            if self.account.wait_check_remark_cancel(): #判断取消按钮是否还存在
                print('修改备注 失败')
                for j in range(3):
                    self.account.confirm_button()  # 多次 点击确定按钮

                if self.account.update_remark_toast(): #获取备注名toast
                    print("错误原因：备注名不能超过10个字")

                self.account.cancel_button()  # 点击取消按钮
            else:
                if self.account.wait_check_remark_tips_page():  # 若修改备注名成功的弹框文案存在
                    print('修改备注成功')
                    self.account.confirm_button()  # 点击确定按钮
                    if self.account.wait_check_remark_page():
                        item = self.account.remark()  # 获取 备注名
                        name = item.text
                        if name!= remark_data[i]['remark']:
                            if name == '未设置' :
                                if remark_data[i]['remark'].strip()!= ""  :
                                    print('★★★ Error - 备注名 未保存成功')
                                else:
                                    print("备注名 保存成功")
                            else:
                                print('★★★ Error - 备注名 未保存成功')
                        else:
                            print("备注名保存成功")

            if self.account.wait_check_account_page() is False:  # 页面检查点
                print('★★★ Error - 未进入我的账号 页面')
            print('---------------------------------------')

