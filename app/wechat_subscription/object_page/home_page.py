import time
from macaca import WebDriverException
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from utils.click_bounds import ClickBounds


class HomePage(BasePage):
    """主界面"""

    @teststeps
    def wait_check_page(self, timeout=10000):
        """以title：“万星在线资源服务”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('万星在线资源服务', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def search_button(self):
        """微信首页搜索按钮"""
        self.driver.element_by_name("搜索").click()

    @teststep
    def subscription(self):
        """“输入内容搜索”的text为依据"""
        time.sleep(2)
        self.driver.element_by_id('com.tencent.mm:id/hx').send_keys("万星在线资源服务")

    @teststep
    def click_sub(self):
        """点开公众号 的text为依据"""
        self.driver.element_by_name('万星在线资源服务').click()

    @teststep
    def report_tab(self):
        """点公众号菜单- 学习报告 的id为依据"""
        self.driver.element_by_name('学习报告').click()

    @teststep
    def buy_tab(self):
        """点公众号菜单- 购买”的text为依据"""
        self.driver \
            .element_by_name("购买").click()
        time.sleep(2)

    @teststep
    def account_tab(self):
        """点公众号菜单- 我的账号的text为依据"""
        self.driver \
            .element_by_name("账号管理").click()

    @teststep
    def cancel_button(self):
        """以“返回按钮”的id为依据"""
        self.driver \
            .element_by_name("取消").click()

    @teststep
    def buck_up_button(self):
        """以“返回按钮”的id为依据"""
        self.driver \
            .element_by_name("返回").click()

    # 未登录状态时
    @teststeps
    def wait_check_login_page(self, timeout=10000):
        """以title：“登录”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('登录', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def login_phone(self):
        """手机号 输入框的text为依据"""
        ele = self.driver \
            .elements_by_class_name("android.widget.EditText")[0]
        return ele

    @teststep
    def login_password(self):
        """密码 输入框的text为依据"""
        ele = self.driver \
            .elements_by_class_name("android.widget.EditText")[1]
        return ele

    @teststep
    def login_button(self):
        """登录 button的text为依据"""
        self.driver \
            .element_by_class_name("android.widget.Button").click()
        time.sleep(1)

    @teststep
    def show_password(self):
        """显示密码 的text为依据"""
        self.driver \
            .element_by_xpath(
                "//android.webkit.WebView[1]/android.view.View[2]/android.view.View[2]/android.view.View[3]")\
            .click()

    @teststep
    def here_button(self):
        """wording中链接: 这里 的text为依据"""
        ClickBounds().click_bounds(560, 1145)

    @teststeps
    def wait_check_download_page(self, timeout=10000):
        """以title：“在线助教学生”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('在线助教学生', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def close_button(self):
        self.driver\
            .element_by_name('返回').click()

    def page_source(self):
        """以“获取page_source”的TEXT为依据"""
        item = self.driver.source
        return item

    @teststeps
    def login_operate(self, username, password):
        if self.wait_check_login_page():  # 页面检查点
            phone = self.login_phone()
            pwd = self.login_password()

            phone.click()  # 激活phone输入框
            phone.send_keys(username)  # 输入手机号

            pwd.click()  # 激活pwd输入框
            pwd.send_keys(password)  # 输入密码

            self.login_button()
            if self.wait_check_login_page():
                print('登录失败', username)
