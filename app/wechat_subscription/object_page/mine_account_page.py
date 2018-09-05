import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.wechat_subscription.object_page.login_page import LoginPage
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from app.wechat_subscription.object_page.home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC
class AccountPage(BasePage):
    """我的账号 界面"""

    @teststeps
    def wait_check_remark_name(self):
        """弹框备注名"""
        try:
            ele = (By.XPATH, "//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[12]")
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    @teststep
    def mine_account(self):
        """点公众号菜单- 我的账号- 我的账号的text为依据"""
        time.sleep(2)
        self.driver.find_elements_by_class_name('android.widget.TextView')[1].click()

    @teststep
    def remark(self):
        """获取 备注名 以xpath为依据"""
        ele = self.driver \
            .find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[7]/android.view.View[1]")
        return ele

    @teststep
    def checkbox_button(self):
        """点 接收作业提醒 选择框 的class name为依据"""
        ele = self.driver.find_element_by_class_name("android.widget.CheckBox")
        return ele

    # 我的账号 界面
    @teststeps
    def wait_check_account(self):
        """以title：“我的账号”的text为依据"""
        try:
            mine_ele = (By.XPATH, "//android.widget.TextView[contains(@text,'我的账号')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(mine_ele))
            return True
        except:
            return False


    @teststeps
    def account_all_ele(self):
        """以“我的账号”所有元素 的父节点 xpath为依据"""
        print('---------------------')
        ele = self.driver \
            .find_elements_by_class_name('android.view.View')
        content = []
        for i in range(0,len(ele)):
            value = ele[i].get_attribute('contentDescription')
            if value != '':
                if value is None:
                    continue
                else:
                    content.append(value)
        return content

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
                  .find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[6]").click()
        time.sleep(1)

    @teststep
    def remark_edittext(self):
        """点击 ‘备注名弹框 - 输入框’ 以text为依据"""
        ele = self.driver \
            .find_element_by_class_name("android.widget.EditText")
        return ele

    @teststeps
    def wait_check_remark_cancel(self):
        """以 输入框“android.widget.EditText”的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id("取消")
            return True
        except:
            return False

    @teststeps
    def wait_check_remark_tips_page(self):
        """以 修改备注名成功 的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id('修改备注名成功')
            return True
        except:
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
    def confirm_update(self):
        """点击 ！！！修改页面 ‘确定按钮’ 以text为依据 多了一个空格"""
        self.driver.find_element_by_accessibility_id("确定 ").click()
        time.sleep(2)

    @teststep
    def cancel_button(self):
        """点击 ‘取消按钮’ 以text为依据"""
        self.driver \
            .find_element_by_accessibility_id("取消").click()

    @teststep
    def wait_update_remark_error(self):
        """点击 ‘取消按钮’ 以text为依据"""
        try:
            self.driver \
                .find_element_by_accessibility_id("备注名不能超过10个字")
            return True
        except:
            return False

    @teststep
    def success_button(self):
        """点击 修改成功tips弹框的‘确定按钮’ 以text为依据"""
        self.driver.find_element_by_accessibility_id("确定").click()

    @teststep
    def logout_button(self):
        """点击 ‘退出登录按钮’ 以text为依据"""
        try:
            ele = self.driver.find_element_by_class_name("android.widget.Button")
            ele.click()
            time.sleep(2)
        except:
            print("ERROR！未发现突出登录按钮")

    @teststeps
    def wait_check_logout_page(self):
        """以title：“确认退出登录吗？”的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id('确认退出登录吗？')
            return True
        except :
            return False

    @teststeps
    def logout_operate(self):
        ele = HomePage().get_text1()
        if ele == "我的账号":  # 我的账号 页面检查点
            print("已在 '我的账号' 页面，退出登录。")
        else:
            HomePage().back_to_club_home()  # 点击关闭按钮
            HomePage().account_tab()  # 点击底部菜单 - 我的账号
            self.mine_account()  # 点击二级标题 我的账号
            if self.wait_check_account():
                ele = HomePage().get_text1()
                if ele == "我的账号":  # 我的账号 页面检查点
                    print("进入 '我的账号' 页面:")
                else:
                    print('★★★ Error - 未进入我的账号 页面')

        self.logout_button()  # 退出登录 按钮
        if self.wait_check_logout_page():  # 退出登录确认弹框 检查点
            self.success_button()  # 确定按钮

    @teststeps
    def get_info(self):
        """获取我的账号页面信息  手机号、备注等"""
        content = []
        HomePage().account_tab()  # 账号管理 tab
        self.mine_account()  # 进入 我的账号
        time.sleep(5)
        if self.wait_check_account():  # 页面检查点
            if not HomePage().wait_check_button():
                LoginPage().clear_tbs_to_retry()
                HomePage().account_tab()  # 账号管理 tab
                self.mine_account()  # 进入 我的账号
            content = self.account_all_ele()  # 所有元素
            HomePage().back_to_club_home()  # 返回主界面
            return content[3], content[5], content[1]  # content[3]=手机号 [5]=备注名 [1]=昵称
        else:
            print("未定位到我的账号检查点")
            return content


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
        if len(content) > 8 :
            if content[-3:] == "...":
                var = content[:8]
            else:
                var = content
        else:
            var = content

        if var != name:
            print('★★★ Error - 学习周报页面展示的学生名字:', var)

        else:
            print("名称核实正确\n")

