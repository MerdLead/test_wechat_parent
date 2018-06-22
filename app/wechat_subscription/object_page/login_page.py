import time
import os
from macaca import WebDriverException

from app.wechat_subscription.object_page.home_page import HomePage
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class LoginPage(BasePage):
    """登录界面"""

    @teststeps
    def __init__(self):
        self.home = HomePage()

    @teststeps
    def wait_check_page(self, timeout=10000):
        """以微信主界面“tab:微信”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('微信', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststep
    def back_up_button(self):
        self.driver\
            .element_by_id('com.tencent.mm:id/i1').click()

    @teststeps
    def app_status(self):
        """判断应用当前状态"""
        if self.wait_check_page():  # 在 微信 界面
            print('微信主界面：')
        elif self.home.wait_check_page():  # 家长端 主界面
            print('家长端 主界面：')
        else:
            print('其他情况：')
            self.close_app()
            self.launch_app()
            if self.wait_check_page():  # 在 微信 主界面
                print('微信主界面：')

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
