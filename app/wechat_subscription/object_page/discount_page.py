import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage
from utils.click_bounds import ClickBounds


class DiscountPage(BasePage):
    """优惠页"""

    @teststeps
    def wait_check_page(self):
        """以title：“立即购买”的text为依据"""
        try:
            ele = (By.XPATH, "//android.widget.TextView[contains(@text,'长留-在线助教优惠活动')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except :
            return False

    @teststeps
    def all_element(self):
        """以“优惠页”页面所有元素 的父节点 xpath为依据"""
        time.sleep(3)
        print('---------------------')
        ele = self.driver.find_elements_by_class_name('android.view.View')
        content = []
        for i in range(len(ele)):
            value = ele[i].get_attribute('contentDescription')
            if value != '':
                content.append(value)
        return ele, content

    @teststep
    def checkbox_1(self):
        """半年卡 选择框"""
        self.driver.find_element_by_xpath(
            "//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[13]").click()
        time.sleep(2)

    @teststep
    def checkbox_2(self):
        """年卡卡 选择框"""

        self.driver.find_element_by_xpath(
            "//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[16]/android.view.View[1]").click()
        time.sleep(2)


    @teststep
    def card_type(self):
        """所选卡片的类型"""
        ele = self.driver.\
            find_element_by_xpath('//android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]')

        value = ele.get_property('value')
        return value['description']

    @teststep
    def see_button(self):
        """点击 ‘去看看按钮’ 以text为依据"""
        self.driver \
            .find_element_by_name("去看看").click()

        time.sleep(2)

    @teststep
    def buy_now_button(self):
        """点击 ‘立即购买 按钮’ 以text为依据"""
        self.driver.find_element_by_accessibility_id("立即购买").click()

        time.sleep(2)

    # 去看看页面
    @teststep
    def group_buy_button(self):
        """点击 ‘一键开团按钮’ 以text为依据"""
        self.driver \
            .find_element_by_name("一键开团").click()
        time.sleep(2)

    @teststep
    def stu_account_pwd(self):
        """学生账号 学生密码"""
        ele = self.driver.\
            find_elements_by_class_name('android.widget.EditText')
        return ele

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
    def commit_button(self):
        """点击 ‘确定 按钮’ 以text为依据"""
        self.driver \
            .find_element_by_accessibility_id("确定 ").click()
        time.sleep(2)

    @teststeps
    def wait_check_buycard_page(self):
        """以title：“购买学习卡”的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id('购买学习卡')
            return True
        except :
            return False

    @teststeps
    def wait_check_user_image(self):
        try:
            ele = (By.CLASS_NAME, "android.widget.Image")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except :
            return False

    @teststep
    def now_payfor_button(self):
        """点击 ‘立即支付按钮’ 以text为依据"""
        self.driver \
            .find_element_by_accessibility_id("立即支付").click()
        time.sleep(2)

    @teststeps
    def wait_check_pay_page(self):
        """以title：“确认支付”的text为依据"""
        try:
            ele = (By.XPATH, "//android.widget.TextView[contains(@text,'请输入支付密码')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(ele))
            return True
        except :
            return False

    @teststep
    def close_button(self):
        """点击 微信支付页面 ‘关闭按钮’ 以id为依据"""
        self.driver \
            .find_element_by_id("com.tencent.mm:id/csk").click()
        time.sleep(2)

    @teststep
    def finish_button(self):
        """点击 微信支付页面 ‘完成按钮’ 以text为依据"""
        self.driver \
            .find_element_by_name("完成").click()

    @teststeps
    def wait_check_pay_success_page(self, timeout=10000):
        """以title：“支付成功”的text为依据"""
        try:
            self.driver \
                .wait_for_find_element_by_name('支付成功', timeout=timeout)
            return True
        except :
            return False

    @teststeps
    def wait_check_finish_page(self, timeout=10000):
        """以title：“购买情况”的text为依据"""
        try:
            self.driver \
                .wait_for_find_element_by_name('购买情况', timeout=timeout)
            return True
        except :
            return False

    @teststeps
    def discount_card_info(self, content):
        if len(content) ==10:
            half_card = content[:4]
            year_card = content[4:8]
            print("优惠卡页面：\n",
                  "半年卡：",half_card,'\n',
                  '年卡：',year_card
                  )
        else:
            print("★★★ Error->优惠页面元素个数不正确！！")

    @teststeps
    def buy_page_info(self, content):
        """点击 优惠购买 后的 购买页面 信息"""
        count = []

        if len(content) == 15:  # 半年卡&年卡
            count.append(4)
            count.append(12)
        elif len(content) == 7:  # 只有半年卡
            count.append(4)
        elif len(content) == 11:  # 只有年卡
            count.append(8)

        item = []
        for j in range(len(count)):  # 代表有几个优惠卡
            if j == 0:
                item.append(content[:count[0]])
            else:
                item.append(content[count[j - 1]:count[j]])

        for k in range(len(item)):
            if len(item[k]) == 4:
                print('<购买>页面:', '\n',
                      '类型：', item[k][0], item[k][1], '\n',
                      item[k][2], '\n',
                      item[k][3], '\n')
            elif len(item[k]) == 8:
                print('<购买>页面:', '\n',
                      '类型：', item[k][0], item[k][1], '\n',
                      item[k][2], '\n',
                      item[k][3], '\n',
                      item[k][4], item[k][5], item[k][6], item[k][7])
            else:
                print('★★★ Error- <购买>页面元素缺失:', item[k])
        return len(content)

    @teststeps
    def discount_page_info(self, content):
        """点击 去看看后 页面 信息"""
        if '同学们都在团购，可直接参团' in content:
            count = []
            for i in range(len(content)):
                if content[i] == "同学们都在团购，可直接参团":
                    count.append(i)
                    break

            # if len(count) == 2:  # 说明不止一个已开团
            #     var = (len(content) - 3 - count[1])//4   # 已开几个团
            # else:
            var = (len(content) - 3 - count[0])   # 已开几个团数var//4
            print('当前开团情况：')
            for i in range(var//4):
                print(i+1, '\n',
                      content[count[0]+1+4*i], '\n',
                      content[count[0] + 2 + 4 * i])
            print('------------------------------')
        else:
            var = 1

        if len(content) != 14 + var - 1:
            print('★★★ Error- <优惠卡具体信息>页面元素缺失:', content)
        else:
            print(content[0], '\n',
                  '拼团价：', content[1], '\n',
                  '原价:', content[2], '\n',
                  content[3] + ":" + content[4], '\n',
                  content[5] + ":   " + content[6] + "." + content[7] + "   " + content[8] + "." + content[9], '\n',
                  content[10])

    @teststeps
    def group_page_info(self, content):
        """点击 一键开团后 页面 信息"""
        if len(content) != 10:
            print('★★★ Error- <开团>页面元素缺失:', content)
        else:
            print(content[1], '\n',
                  content[2], '\n',
                  '拼团价：', content[3], '\n',
                  '原价:', content[4], '\n',
                  content[5] + ":" + content[6])

    @teststeps
    def pay_form(self):
        ele = self.driver.find_element_by_class_name("android.widget.CheckBox")
        value = ele.get_attribute("contentDescription")
        return value[2:]


    @teststeps
    def buy_now_page_info(self, content):
        """点击 立即购买后 页面 信息"""
        if len(content) != 8:
            print('★★★ Error- <开团>页面元素缺失:', content)
        else:
            print(content[1], '\n',
                  content[2], '\n',
                  '拼团价：', content[3], '\n',
                  '原价:', content[4])

    @teststeps
    def payment_info(self, content):
        """支付页面 信息"""
        pay = self.pay_form()
        if len(content) == 11:
            print('<支付>页面:', '\n',
                  content[1], '\n',
                  content[2], '\n',
                  '价格:', content[3], '\n',
                  '原价:', content[4], '\n',
                  '学生:', content[5], '\n',
                  content[6], ':',pay, '\n',
                  '协议:', content[8], '\n',
                  '实际付款金额:', content[9])
        elif len(content) == 13:
            print('<支付>页面:', '\n',
                  content[1], '\n',
                  content[2], '\n',
                  '价格:', content[3], '\n',
                  '原价:', content[4], '\n',
                  content[5]+':'+content[6], '\n',
                  '学生:', content[7], '\n',
                  content[8], ':', pay, '\n',
                  '协议:', content[10], '\n',
                  '实际付款金额:', content[11])
        else:
            print('★★★ Error- <支付>页面元素缺失:', content)

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

    @teststeps
    def finish_page_info(self, content):
        """支付完成 页面信息"""
        if len(content) not in (8, 10):
            print('★★★ Error- <支付完成>页面元素缺失:', content)
        elif len(content) == 8:
            print('<支付完成>页面:', '\n',
                  content[0], '\n',
                  '价格:', content[1], '\n',
                  '原价:', content[2], '\n',
                  content[3], ':', content[4], content[6], '\n',
                  '学生:', content[5], '\n',
                  content[7])
        elif len(content) == 10:
            print('<支付完成>页面:', '\n',
                  content[0], '\n',
                  '价格:', content[1], '\n',
                  '原价:', content[2], '\n',
                  content[3], ':', content[4], '\n',
                  content[5], ':', content[6], content[7], content[8], '\n',
                  content[9])
