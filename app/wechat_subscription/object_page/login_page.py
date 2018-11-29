import time
import os


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.wechat_subscription.object_page.home_page import HomePage
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from selenium.webdriver.common.by import By

from utils.toast_find import Toast


class LoginPage(BasePage):
    """登录界面"""

    @teststeps
    def __init__(self):
        self.home = HomePage()
        self.toast = Toast()
    @teststeps

    def wait_check_wx(self):
        """以微信主界面“tab:微信”的text为依据"""
        try:
            main_ele = (By.XPATH, "//android.widget.TextView[contains(@text,'微信')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(main_ele))
            return True
        except :
            return False

    @teststeps
    def wait_check_test1(self):
        """以微信主界面“tab:微信”的text为依据"""
        try:
            main_ele = (By.XPATH, "//android.widget.TextView[contains(@text,'测试1')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(main_ele))
            return True
        except:
            return False

    @teststeps
    def wait_check_tbs(self):
        """以tbs页面 标题作为检查点"""
        try:
            tbs_title = (By.XPATH, "//android.widget.TextView[contains(@text,'tbs调试页面')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(tbs_title))
            return True
        except:
            return False

    @teststeps
    def wait_check_delete_x5core(self):
        """删除内核弹框检查"""
        try:
            tbs_title = (By.XPATH, "//android.widget.TextView[contains(@text,'删除内核')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(tbs_title))
            return True
        except:
            return False

    @teststeps
    def wait_check_find_exp(self):
        """搜索页面检查"""
        try:
            tbs_title = (By.ID, "com.tencent.mm:id/ht")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(tbs_title))
            return True
        except:
            return False

    @teststep
    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        os.system ("adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI/")
        time.sleep (5)

    @teststep
    def close_app(self):
        """Close on the device the application specified in the desired capabilities.
        """
        os.system ('adb shell am force-stop com.tencent.mm')

    @teststeps
    def app_status(self):
        """判断应用当前状态"""

        if self.wait_check_wx():  # 在 微信 界面
            print('微信主界面：')
            # self.clear_tbs()
        elif self.home.wait_check_parent_title():  # 家长端 主界面

            print('家长端 主界面：')
        else:
            print('其他情况：')
            self.close_app()
            self.launch_app()
            if self.wait_check_wx():  # 在 微信 主界面
                print('微信主界面：')

    @teststep
    def chat_test1_click(self):
        """点击置顶好友test1"""
        self.driver.find_elements_by_id ("com.tencent.mm:id/np")[0].click()

    @teststep
    def tbs_link_click(self):
        """点击test1发送的tbs链接"""
        self.driver.find_element_by_id ("com.tencent.mm:id/lz").click ()

    @teststep
    def click_clear_tbs_btn(self):
        """点击清除tbs内核选项"""
        self.driver.find_element_by_xpath ("//android.widget.TextView[contains(@text,'清除TBS内核')]").click()

    @teststep
    def confirm_delete(self):
        """确认清除"""
        self.driver.find_element_by_id ("android:id/button1").click()
        time.sleep (2)

    @teststep
    def back_to_test1(self):
        """点击返回按钮（X） 返回到聊天框"""
        self.driver.find_element_by_id ("com.tencent.mm:id/j7").click()

    @teststep
    def back_to_wx_home(self):
        self.driver.find_element_by_id ("com.tencent.mm:id/iz").click()

    @teststep
    def clear_tbs(self):
        """进入清除内核页面，并返回主页面"""
        self.chat_test1_click()
        if self.wait_check_test1():
            self.tbs_link_click()      #点击链接
            if self.wait_check_tbs():
                self.click_clear_tbs_btn()  #点击清除tbs
                if self.wait_check_delete_x5core():
                    self.confirm_delete()   #确认清除
                    self.back_to_test1()   # 退出tbs页面
                    if self.wait_check_test1():
                        self.back_to_wx_home() #退出聊天页面
                        if self.wait_check_wx():
                            print("已清除TBS内核\n")

    @teststeps
    def clear_tbs_to_retry(self):
        """内核清除"""
        if "QQ浏览器X5内核提供技术支持" in self.home.driver.page_source:
            print("X5内核已恢复，需重新清除TBS")
            self.home.back_to_club_home()  # 返回
            if self.home.wait_check_parent_title():  # 在线助教家长公众号主界面检查
                self.home.back_to_find()  # 退出公众号
                self.home.back_to_wx_home()  # 退出搜搜页面
                self.clear_tbs()  # 清除内核
                self.home.click_sub()  # 重新进入公众号
        else:
            print("X5内核未恢复，但依然未发现元素")
            self.home.back_to_club_home()

    @teststeps
    def check_login_error_info(self, toast_info):
        """检查登录toast信息"""
        if toast_info == '':
            pass

        elif self.toast.find_toast_by_xpath(toast_info):
            print(toast_info)
        else:
            print("未发现错误提示信息",toast_info)



