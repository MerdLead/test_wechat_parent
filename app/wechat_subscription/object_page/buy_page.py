import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from utils.click_bounds import ClickBounds


class BuyPage(BasePage):
    """购买tab页"""

    @teststeps

    def wait_check_page(self):
        """以title：“购买”的text为依据"""
        try:
            locator = (By.XPATH,"//android.widget.TextView[contains(@text,'购买')]")
            WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except :
            return False

    @teststeps
    def wait_check_update_buy(self):
        """以title：“直接购买”的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id("直接购买")
            return True
        except:
            return False

    @teststeps
    def wait_check_upgrade_button(self):
        """以title：“购买”的text为依据"""
        try:
            locator = (By.CLASS_NAME, "android.widget.Button")
            WebDriverWait(self.driver, 30, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except:

            return False

    @teststeps
    def all_element(self):
        """以“购买”页面所有元素 的父节点 xpath为依据"""
        time.sleep(3)
        print('---------------------')


        ele = self.driver.find_elements_by_class_name('android.view.View')
        content = []
        for i in range(len(ele)):
            value = ele[i].get_attribute('contentDescription')
            if value!= '':
                content.append(value)
        return content

    @teststeps
    def get_RadioButtons(self):
        ele = self.driver.find_elements_by_class_name("android.widget.RadioButton")
        return ele



    @teststep
    def checkbox_1(self):
        """月卡 选择框"""

        self.driver.find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[7]").click()
        time.sleep(2)
        # ClickBounds().click_bounds(65, 10)
    @teststep
    def checkbox_2(self):
        """季卡 选择框"""
        self.driver.find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[10]").click()
        time.sleep(2)
        # ClickBounds().click_bounds(70, 1000)
    @teststep
    def checkbox_3(self):
        """半年卡 选择框"""
        self.driver.find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[13]").click()
        time.sleep(2)
        # ClickBounds().click_bounds(70, 1200)
    @teststep
    def checkbox_4(self):
        """年卡 选择框"""
        self.driver.find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[16]/android.view.View[1]").click()
        time.sleep(2)
        # ClickBounds().click_bounds(70, 1400)


    @teststep
    def online_service(self):
        """在线客服 按钮 以text为依据"""
        self.driver \
            .find_element_by_accessibility_id("在线客服").click()

    @teststep
    def card_type(self,index):
        """所选卡片的类型"""
        ele = self.get_RadioButtons()
        value = ele[index].get_attribute('contentDescription')
        kind = value.split(" ")[1]
        return kind

    @teststep
    def upgrade_button(self):
        """马上升级 按钮 以text为依据"""
        self.driver \
            .find_element_by_class_name("android.widget.Button").click()

        time.sleep(2)

    # 试用期，显示：您还未升级“在线助教”【提分版】，快去升级吧！
    # 有效期内，显示：“在线助教”【提分版】有效期截止到X年X月X日；
    # 交费后有效期已过，显示：“在线助教”【提分版】已过期

    @teststep
    def direct_buy_button(self):
        """点击 ‘直接购买’按钮 以text为依据"""

        self.driver.find_element_by_accessibility_id("直接购买").click()

        time.sleep(2)

    @teststep
    def discount_buy_button(self):
        """点击 ‘优惠购买按钮’ 以text为依据"""

        self.driver.find_element_by_accessibility_id("优惠购买").click()
        time.sleep(2)

    @teststep
    def discount_buy_button_type(self):
        """‘优惠购买按钮 是否可点击’ 以text为依据"""

        ele = self.driver.find_element_by_accessibility_id("优惠购买")
        value = ele.get_attribute('clickable')
        return value

    # 在线客服 关闭按钮
    @teststep
    def close_button(self):
        """点击 ‘OK’按钮 以text为依据"""

        time.sleep(5)
        self.driver.find_element_by_accessibility_id("OK").click()
        time.sleep(2)
    # 支付页面
    @teststeps
    def pay_for_webchat(self):
        """微信支付"""
        self.driver \
            .find_element_by_xpath(
                "//android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]/android.view.View[1]")\
            .click()

    @teststeps
    def pay_for_another(self):
        """家长代付"""
        self.driver \
            .find_element_by_xpath(
                "//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[10]/android.view.View[1]")\
            .click()

    @teststeps
    def commit_button(self):
        """确认支付 按钮"""


        self.driver .find_element_by_xpath("//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[12]").click()

    @teststeps
    def agreement(self):
        """链接 购买协议"""
        self.driver \
            .find_element_by_accessibility_id("购买协议").click()

    @teststeps
    def wait_check_pay_page(self):
        """以title：“确认交易”的text为依据"""
        try:
            locator = (By.ID, "com.tencent.mm:id/ea7")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except :
            return False

    @teststeps
    def wait_check_pay_another_page(self):
        """以title：“家长代付”的text为依据"""
        try:
            time.sleep(3)
            self.driver.find_element_by_accessibility_id('微信代付')
            return True
        except :

            return False

    @teststep
    def close_pay_button(self):
        """点击 微信支付页面 ‘关闭按钮’ 以text为依据"""

        self.driver .find_element_by_id("com.tencent.mm:id/csk").click()
        time.sleep(2)

    @teststeps
    def wait_check_pay_success_page(self, timeout=10000):
        """以title：“支付成功”的text为依据"""
        try:
            self.driver \
                .wait_for_find_element_by_name('支付成功', timeout=timeout)
            return True
        except :
            return False

    @teststep
    def finish_button(self):
        """点击 微信支付页面 ‘完成按钮’ 以text为依据"""
        self.driver \
            .find_element_by_name("完成").click()

    @teststeps
    def pay_operate(self):
        """支付 过程"""
        ClickBounds().click_bounds(180, 1650)
        ClickBounds().click_bounds(180, 1650)
        ClickBounds().click_bounds(900, 1300)
        ClickBounds().click_bounds(550, 1470)
        ClickBounds().click_bounds(550, 1670)
        ClickBounds().click_bounds(900, 1480)

        if self.wait_check_pay_success_page():
            self.finish_button()  # 点击完成按钮
            print('支付完成')

    @teststeps
    def buy_page_info(self, content):
        """购买页面 信息"""
        if len(content) != 9:
            print('★★★ Error- <购买>页面元素缺失:', content)
        else:
            print('<购买>页面:', '\n',
                  '学生：', content[0], '\n',
                  '手机号：', content[1], '\n',
                  'tips:', content[3:5], '\n',

                  '选择的是：', content[6],'\n')

    @teststeps
    def magic_page_info(self, content):
        """法宝页面 信息"""

        if len(content) != 5:
            print('★★★ Error- <法宝>页面元素缺失:', content)
        else:
            print('<法宝>页面:', '\n',
                  '学生：', content[0], '\n',
                  '手机号：', content[1], '\n',

                  'tips:', content[3:], '\n')
    @teststeps
    def direct_payment_info(self, content):
        """支付页面 信息"""
        if len(content) != 17:
            print('★★★ Error- <支付>页面元素缺失:', content)
        else:
            print('<支付>页面:', '\n',
                  '学生:', content[0], '\n',
                  '手机号：', content[1], '\n',

                  '价格:', content[3]+content[4], '\n',
                  '购买内容:', content[5], '\n',
                  '协议:', content[9],'\n',
                  '说明:', content[14],"\n",content[15],'\n',
                  '-----------------------------------------')

    @teststeps
    def discount_payment_info(self, content):
        """支付页面 信息"""

        if len(content) != 17:
            print('★★★ Error- <支付>页面元素缺失:', content)
        else:
            print('<支付>页面:', '\n',
                  '学生:', content[0], '\n',
                  '手机号：', content[1], '\n',
                  '价格:', content[3:5], '\n',
                  '购买内容:', content[5], '\n',

                  '协议:', content[8], '\n',
                  '说明:', content[14:16])

    @teststeps
    def pay_another_info(self, content):
        """家长代付 页面 信息"""
        if len(content) != 9:
            print('★★★ Error- <代付>页面元素缺失:', content)
        else:
            print(content[1], '页面:', '\n',
                  content[2], '\n',
                  '价格：', content[3], '\n',
                  '付款方式:', content[4], '\n',
                  '说明:', content[5], '\n',

                  content[8],'\n')

