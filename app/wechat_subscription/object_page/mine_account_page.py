import time
from macaca import WebDriverException
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from app.wechat_subscription.object_page.home_page import HomePage


class AccountPage(BasePage):
    """我的账号 界面"""

    @teststep
    def mine_account(self):
        """点公众号菜单- 我的账号- 我的账号的text为依据"""
        self.driver \
            .element_by_name("我的账号").click()

    @teststep
    def remark(self):
        """获取 备注名 以xpath为依据"""
        ele = self.driver \
            .element_by_xpath("//android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.view.View[1]")
        return ele

    @teststep
    def checkbox_button(self):
        """点 接收作业提醒 选择框 的class name为依据"""
        ele = self.driver \
            .element_by_class_name("android.widget.CheckBox")
        return ele

    # 我的账号 界面
    @teststeps
    def wait_check_account_page(self, timeout=10000):
        """以title：“我的账号”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('我的账号', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststeps
    def account_all_ele(self):
        """以“我的账号”所有元素 的父节点 xpath为依据"""
        print('---------------------')
        ele = self.driver \
            .elements_by_xpath('//android.webkit.WebView[1]/descendant::android.view.View')
        content = []
        for i in range(len(ele)):
            value = ele[i].get_property('value')
            if value['description'] != '':
                content.append(value['description'])
        return ele, content

    @teststeps
    def account_info(self, content):
        """我的账号页面 信息"""
        if len(content) == 10:
            print('<我的账号>页面:')
            for i in range(0, len(content), 2):
                print(content[i]+':'+content[i+1])
        else:
            print('★★★ Error- <我的账号>页面元素缺失:', content)
        return content[5]

    @teststep
    def remark_name(self):
        """点击 ‘设置备注名’ 以text为依据"""
        self.driver \
            .element_by_xpath("//android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]/android.view.View[3]/android.view.View[1]")\
            .click()

    @teststep
    def remark_edittext(self):
        """点击 ‘备注名弹框 - 输入框’ 以text为依据"""
        ele = self.driver \
            .element_by_class_name("android.widget.EditText")
        return ele

    @teststeps
    def wait_check_remark_page(self, timeout=10000):
        """以 输入框“android.widget.EditText”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_class_name('android.widget.EditText', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststeps
    def wait_check_remark_tips_page(self, timeout=10000):
        """以 修改备注名成功 的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('修改备注名成功', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def tap_blank(self):
        """点击空白处-- 因为焦点在输入框中时，获取不到元素信息"""
        self.driver \
            .touch('tap', {
                'x': 540,
                'y': 300
            })
        time.sleep(2)

    @teststep
    def confirm_button(self):
        """点击 ！！！修改页面 ‘确定按钮’ 以text为依据"""
        self.driver \
            .element_by_name("确定 ").click()

    @teststep
    def cancel_button(self):
        """点击 ‘取消按钮’ 以text为依据"""
        self.driver \
            .element_by_name("取消").click()

    # 修改成功页面
    @teststep
    def success_icon(self):
        """点击 修改成功tips弹框的‘确定按钮’ 以text为依据
            -- 由于两个确定按钮的文案内容差一个空格 ！！！！"""
        self.driver \
            .element_by_name("").click()

    @teststep
    def confirm(self):
        """点击 修改成功tips弹框的‘确定按钮’ 以text为依据
            -- 由于两个确定按钮的文案内容差一个空格 ！！！！"""
        self.driver \
            .element_by_name("确定").click()

    @teststep
    def logout_button(self):
        """点击 ‘退出登录按钮’ 以text为依据"""
        self.driver \
            .element_by_class_name("android.widget.Button").click()

    @teststeps
    def wait_check_logout_page(self, timeout=10000):
        """以title：“确认退出登录吗？”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('确认退出登录吗？', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststeps
    def logout_operate(self):
        if self.wait_check_account_page():  # 我的账号 页面检查点
            print("在 '我的账号' 页面:")
        else:
            HomePage().close_button()  # 点击关闭按钮
            HomePage().account_tab()  # 点击底部菜单 - 我的账号
            self.mine_account()  # 点击二级标题 我的账号
            if self.wait_check_account_page():  # 我的账号 页面检查点
                print("进入 '我的账号' 页面:")
            else:
                print('★★★ Error - 未进入我的账号 页面')

        self.logout_button()  # 退出登录 按钮
        if self.wait_check_logout_page():  # 退出登录确认弹框 检查点
            self.confirm()  # 确定按钮

    @teststeps
    def get_info(self):
        """获取我的账号页面信息  手机号、备注等"""
        content = 0
        HomePage().account_tab()  # 账号管理 tab
        self.mine_account()  # 进入 我的账号
        if self.wait_check_account_page():  # 页面检查点
            content = self.account_all_ele()  # 所有元素  content[1][3]=手机号
            HomePage().buck_up_button()  # 返回主界面
        return content[1][3], content[1][5], content[1][1]

    @teststeps
    def stu_name_judge(self):
        """判断每个页面展示的为备注名还是昵称"""
        remark = self.get_info()
        if remark[1] != '未设置':
            return remark[1], remark[0]  # 备注名
        else:
            return remark[2], remark[0]  # 学生昵称

    @teststeps
    def compare_name(self, content, name):
        """每个页面展示的学生名称和备注 比较"""
        if len(content) > 12:
            if '...' in content:
                var = content[:8]
            else:
                var = content
        else:
            var = content

        if var != name:
            print('★★★ Error - 学习周报页面展示的学生名字:', var)
