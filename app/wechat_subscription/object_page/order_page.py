
import time

import numpy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class OrderPage(BasePage):
    """购买 界面"""
    @teststep
    def mine_order(self):
        """点公众号菜单- 我的账号- 我的订单的text为依据"""
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@text="我的订单"]').click()

    @teststeps
    def wait_check_order_page(self):
        """以title：“我的订单”的text为依据"""
        try:
            locator = (By.XPATH,"//android.widget.TextView[contains(@text,'我的订单')]")
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except :
            return False

    @teststeps
    def wait_check_mine_orderText(self):
        """以title：“我的订单”的text为依据"""
        try:
            WebDriverWait (self.driver, 10, 0.5).until (lambda x:x.find_element_by_accessibility_id("我的订单"))
            return True
        except :
            return False

    @teststeps
    def wait_check_detail_page(self):
        """以title：“我的订单”的text为依据"""
        try:
            locator = (By.XPATH, "//android.view.View[contains(@text,'购买情况')]")
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    @teststeps
    def order_all_ele(self):
        """以“我的订单”所有元素 的父节点 xpath为依据"""
        print('---------------------')
        ele = self.driver.find_elements_by_class_name('android.view.View')
        content = []
        for i in range(len(ele)):
            value = ele[i].text
            if value!= '':
                if value is None or value.isspace():
                    continue
                else:
                    content.append(value)
        return  content

    @teststeps
    def order_info(self, content):
        """我的订单页面 信息"""
        content.remove(content[0])
        reshape_array = numpy.array(content).reshape(int(len(content)/5),5)
        for info in reshape_array:
            print(info[0], info[1], '\n',
                  info[2], info[3], '\n',
                  info[4])
            print('-'*30+'\n')
        return reshape_array



    @teststep

    def get_details_list(self):
        """获取当前页的订单详情ele"""
        ele = self.driver.find_elements_by_xpath('//android.view.View[contains(@text,"订单详情")]')
        return ele

    #     # 正在拼团的订单
    @teststeps
    def time(self):
        # todo 判断时间的格式
        print('格式正确')

    @teststep
    def cancel_order(self, index):
        """取消订单"""
        self.driver.find_element_by_accessibility_id('取消订单')[index].click()

    @teststep
    def known_button(self):
        """弹框中 '我知道了'按钮"""
        self.driver \
            .find_element_by_accessibility_id('我知道了').click()


    def get_ele_xpath(self, num):
        xpath_str = '//*[@resource-id="com.tencent.mm:id/b36"]/android.widget.FrameLayout[1]/android.widget.FrameLayout' \
                    '[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[{}]'.format(num)
        return xpath_str


    @teststep
    def order_page_ele_print(self, ele_list):
        for i in range(len(ele_list)):
            time_ele  = self.driver.find_element_by_xpath(self.get_ele_xpath(2 + 5* i))
            time_str = time_ele.get_attribute('contentDescription')

            pay_status_ele = self.driver.find_element_by_xpath(self.get_ele_xpath(3 + 5*i))
            pay_status = pay_status_ele.get_attribute('contentDescription')

            card_type_ele = self.driver.find_element_by_xpath(self.get_ele_xpath(4 + 5*i))
            card_type = card_type_ele.get_attribute('contentDescription')

            price_ele = self.driver.find_element_by_xpath(self.get_ele_xpath(5 + 5*i))
            price = price_ele.get_attribute('contentDescription')

            print('时间：',time_str,'\n状态：',pay_status)
            print('卡型：',card_type, '\n价格：',price)
            print('-'*20+'\n')


    # 购买成功
    # 拼团失败- 退款中...
    # 拼单失败,已退款
    @teststeps
    def details_page_info(self, content, pay_status):
        """订单详情页面 信息"""
        if pay_status == '拼单失败,退款中...':
            if len(content) == 13:
                print('<订单详情>页面:', '\n',
                  content[0], '\n',
                  '价格：', content[1], '\n',
                  '原价：', content[2], '\n',
                  "订单提示：", content[3]+ ":" + content[4], '\n',
                  content[5] +":"+ content[6],'\n',
                  '学生：', content[7] + content[8], '\n',
                  "购买情况：", content[9], '\n',
                  'Tips：', content[12], '\n',)
            elif len(content) == 8:
                print('<订单详情>页面:', '\n',
                      content[0], '\n',
                      '价格：', content[1], '\n',
                      '原价：', content[2], '\n',
                       content[3] + ":"+ content[4],'\n',
                      '学生：', content[5], '\n',
                      "购买情况：",content[6],'\n',
                      'Tips：', content[7], '\n',
                      )
            else:
                print('★★★ Error- <订单详情>元素缺失:', content)

        elif pay_status == '拼单失败,已退款':
            if len(content) == 8:
                print('<订单详情>页面:', '\n',
                      content[0], '\n',
                      '价格：', content[1], '\n',
                      '原价：', content[2], '\n',
                      content[3] + ":" + content[4], '\n',
                      content[5]+ ":" + content[6], '\n',
                      'Tips：', content[7], '\n',
                      )
            else:
                print('★★★ Error- <订单详情>元素缺失:', content)

        elif pay_status == '购买成功':
            if len(content) == 13:
                print('<订单详情>页面:', '\n',
                  content[0], '\n',
                  '价格：', content[1], '\n',
                  '原价：', content[2], '\n',
                  "订单提示：", content[3]+ ":" + content[4], '\n',
                  content[5] +":"+ content[6],'\n',
                  '学生：', content[7] + content[8], '\n',
                  "购买情况：", content[9], '\n',
                  'Tips：', content[12], '\n',)
            else:
                print('★★★ Error- <订单详情>元素缺失:', content)


    def screen_swipe_up(self, a, b, c, steps=0.5):
        """向上滑动"""
        screen = self.get_window_size()
        x1 = int(screen[0] * a)
        y1 = int(screen[1] * b)
        y2 = int(screen[1] * c)
        self.driver.swipe(x1, y1, x1, y2, steps)

