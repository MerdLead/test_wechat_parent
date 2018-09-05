import time
import os


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.wechat_subscription.object_page.home_page import HomePage
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """登录界面"""

    @teststeps
    def __init__(self):
        self.home = HomePage()

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
        """以微信主界面“tab:微信”的text为依据"""
        try:
            tbs_title = (By.XPATH, "//android.widget.TextView[contains(@text,'tbs调试页面')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(tbs_title))
            return True
        except:
            return False

    @teststeps
    def wait_check_delete_x5core(self):
        """以微信主界面“tab:微信”的text为依据"""
        try:
            tbs_title = (By.XPATH, "//android.widget.TextView[contains(@text,'删除内核')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(tbs_title))
            return True
        except:
            return False

    @teststeps
    def wait_check_find_exp(self):
        """以微信主界面“tab:微信”的text为依据"""
        try:
            tbs_title = (By.ID, "com.tencent.mm:id/ht")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(tbs_title))
            return True
        except:
            return False

    @teststep
    def back_up_button(self):
        self.driver\
            .element_by_id('com.tencent.mm:id/i1').click()

    @teststeps
    def app_status(self):
        """判断应用当前状态"""

        if self.wait_check_wx():  # 在 微信 界面
            print('微信主界面：')
            self.clear_tbs()
        elif self.home.wait_check_parent():  # 家长端 主界面

            print('家长端 主界面：')
        else:
            print('其他情况：')
            self.close_app()
            self.launch_app()


            if self.wait_check_wx():  # 在 微信 主界面
                print('微信主界面：')

    @teststep
    def clear_tbs(self):
        self.driver.find_elements_by_id("com.tencent.mm:id/np")[0].click()
        if self.wait_check_test1():
            self.driver.find_element_by_id("com.tencent.mm:id/lz").click()
            if self.wait_check_tbs():
                self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'清除TBS内核')]").click()
                if self.wait_check_delete_x5core():
                    self.driver.find_element_by_id("android:id/button1").click()
                    print("清除TBS内核...")
                    time.sleep(2)
                    self.driver.find_element_by_id("com.tencent.mm:id/j7").click()
                    if self.wait_check_test1():
                        self.driver.find_element_by_id("com.tencent.mm:id/iz").click()
                        if self.wait_check_wx():
                            print("已清除TBS内核\n")


    @teststep
    def launch_app(self):
        """Start on the device the application specified in the desired capabilities.
        """
        os.system("adb shell am start -n com.tencent.mm/com.tencent.mm.ui.LauncherUI/")
        time.sleep(5)

    @teststep
    def close_app(self):
        """Close on the device the application specified in the desired capabilities.
        """
        os.system('adb shell am force-stop com.tencent.mm')



    @teststeps
    def clear_tbs_to_retry(self):
        if "QQ浏览器X5内核提供技术支持" in self.home.driver.page_source:
            print("X5内核已恢复，需重新清除TBS")
            self.home.back_to_club_home()  # 返回
            if self.home.wait_check_parent():  # 在线助教家长公众号主界面检查
                self.home.back_to_find()  # 退出公众号
                self.home.back_to_wx_home()  # 退出搜搜页面
                self.clear_tbs()  # 清除内核
                self.home.click_sub()  # 重新进入公众号
        else:
            print("X5内核未恢复，但依然未发现元素")
            self.home.back_to_club_home()

    @teststeps
    def wait_check_phone_regist(self):
        try:
            self.driver.find_element_by_accessibility_id("该手机号尚未注册，请先至学生端注册")
            return True
        except:
            return False

    @teststeps
    def wait_check_phone_pwd_error(self):
        try:
            self.driver.find_element_by_accessibility_id("账号或密码错误")
            return True
        except:
            return False

    @teststeps
    def wait_check_toast_phone(self):
        try:
            self.driver.find_element_by_accessibility_id("请输入正确手机号")
            return True
        except:
            return False

    @teststeps
    def wait_check_toast_pwd(self):
        try:
            self.driver.find_element_by_accessibility_id("密码错误")
            return True
        except:
            return False

    @teststeps
    def check_login_error_info(self):
        time.sleep(1.5)
        if self.wait_check_phone_regist():
            print("该手机号尚未注册，请先至学生端注册")
        elif self.wait_check_phone_pwd_error():
            print("账号或密码错误")
        elif self.wait_check_toast_phone() and self.wait_check_toast_pwd():
            print("请输入正确手机号   密码错误")
        elif self.wait_check_toast_phone():
            print("请输入正确手机号")
        elif self.wait_check_toast_pwd():
            print("密码错误")
        else:
            print("<><><><>")


