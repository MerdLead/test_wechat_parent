import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from app.wechat_subscription.object_page.home_page import HomePage
from app.wechat_subscription.object_page.login_page import LoginPage
from app.wechat_subscription.object_page.mine_account_page import AccountPage
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class ReportPage(BasePage):
    """学习报告 界面"""

    @teststeps
    def __init__(self):
        self.home = HomePage()

    @teststep
    def study_week_report(self):
        """点公众号菜单- 学习报告- 学习周报 的text为依据"""
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'学习周报')]").click()
        time.sleep(2)

    @teststep
    def study_month_report(self):
        """点公众号菜单- 学习报告- 学习月报 的text为依据"""
        self.driver \
            .find_element_by_xpath("//android.widget.TextView[contains(@text,'学习月报')]").click()
        time.sleep(3)

    @teststeps
    def wait_check_week_page(self):
        """以 title:学习周报 的text为依据"""
        try:
            locator = (By.XPATH, "//android.widget.TextView[contains(@text,'学习周报')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except :
            return False

    @teststeps
    def wait_check_month_page(self):
        """以 title:学习月报 的text为依据"""
        try: 
            locator = (By.XPATH,"//android.widget.TextView[contains(@text,'学习月报')]")
            WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except :
            return False

    @teststeps
    def wait_check_report_show(self):
        """以 title:学习月报 的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id("晒一下")
            return True
        except:

            return False

    @teststeps
    def all_element(self):
        """以“学习周报、月报”所有元素 的父节点 xpath为依据"""
        ele = self.driver.find_elements_by_class_name('android.view.View')
        content = []
        for i in range(len(ele)):
            value = ele[i].get_attribute('contentDescription')
            if value!= '':
                if value is None:
                    continue
                else:
                    content.append(value)
        return ele,content

    @teststep
    def share_button(self,index):
        """点 ‘晒一下’按钮 的text为依据"""
        self.driver.find_elements_by_accessibility_id("晒一下")[index].click()

    @teststep
    def share_button_count(self):
        """点 ‘晒一下’按钮 的text为依据"""
        ele = self.driver.find_elements_by_accessibility_id("晒一下")
        return ele


    @teststep
    def share_button_type(self, index):
        """点 ‘晒一下’按钮 的text为依据"""
        ele = self.driver \
            .find_elements_by_name("晒一下")[index]


        value = ele.get_property('value')
        if value['clickable']:
            return True

    @teststeps
    def wait_check_share_page(self):
        """以 title:在线助教分享页 的text为依据"""
        try:
            locator = (By.XPATH, "//android.widget.TextView[contains(@text,'在线助教分享页')]")
            WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located(locator))
            return True
        except :
            return False

    @teststeps
    def wait_check_select_month(self,index):
        """以 title:在线助教分享页 的text为依据"""
        try:
            self.driver.find_element_by_accessibility_id(str(index+"月"))
            return True
        except:

            return False

    # 学习周报
    @teststep
    def buy_card(self):
        """点 ‘购买学生卡’按钮 的text为依据"""
        self.driver \
            .find_element_by_name("购买学生卡").click()


    @teststep
    def click_blank(self):
        """点击空白处-- 因为焦点在输入框中时，获取不到元素信息"""
        self.driver.tap([(58,1200),])
        time.sleep(2)

    # 学习月报
    @teststep
    def year(self):
        """年份"""
        self.driver\
            .find_element_by_xpath(

                '//android.webkit.WebView[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]/android.view.View[1]')\
            .click()

    @teststep
    def month(self):
        """月份"""
        ele = self.driver \
            .find_element_by_xpath(
                '//android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[4]/android.view.View[1]/android.view.View[3]/android.view.View[1]')
        return ele



    @teststeps
    def year_select(self, index):
        """选择不同年份"""

    @teststeps
    def month_select(self, month,index):
        """选择不同月份"""
        select_month = index
        if select_month < month-3 :
            while True:
                self.swipe_up(0.5,0.85,0.95,2000)
                if self.wait_check_select_month(index):
                    self.driver.find_element_by_accessibility_id(str(index+"月")).click()
                    break
        else:
            self.driver.find_element_by_accessibility_id(str(index + "月")).click()
        time.sleep(2)
        self.driver.find_element_by_accessibility_id("确定").click()
        time.sleep(5)


    @teststeps
    def homework_all_info(self, content):
        """学习周报 页面  作业卷子统计信息"""
        count = []
        for i in range(len(content)):
            if content[i] == '作业卷子统计':
                count.append(i)
            if content[i] == '单词本统计':
                count.append(i)
                break
        if count[0] == 2:
            print('学生:%s， 时间：%s' % (content[0][:-5], content[1]))

        else:
            print('★★★ Error - 页面中元素缺失', content)

        print('-------------------------------------------')
        if count[1] - count[0] == 9:  # 作业卷子统计
            print(content[count[0]]+':', '\n',
                  content[count[0] + 2], '\n',
                  content[count[0] + 3], '\n',
                  content[count[0] + 4], '\n',
                  content[count[0] + 5], '\n',
                  content[count[1]-2]+":" + content[count[1]-3], '\n',
                  content[count[1]-1],'\n')
        elif count[1] - count[0] == 3:  # 无统计信息
            print(content[count[0]]+':', '\n',
                  content[count[0]+2],"\n",
                )

        return count[1] - count[0]

    @teststeps
    def word_all_info(self, content):
        """学习周报 页面 单词本统计信息"""
        count = []
        for i in range(len(content)):
            if content[i] == '单词本统计':
                count.append(i)
                break

        if len(content) - count[0] == 6:  # 无统计信息
            print(content[count[0]] + ':', '\n',
                  content[count[0] + 2], '\n',
                  content[count[0] + 3] + content[count[0] + 4] + content[count[0] + 5])
        elif len(content) - count[0] == 3:  # 单词本统计
            print(content[count[0]], ':', '\n',
                  content[len(content)-1],'\n')


    @teststeps
    def homework_share_all_info(self, content):
        """学习周报 分享页面 信息"""
        if len(content) != 12:
            print('★★★ Error - 页面中元素缺失', content)
        else:
            print('分享页：', '\n',
                  content[2], '\n',
                  content[3], '\n',
                  content[4], '\n',
                  content[5], '\n',
                  content[7] + ":" + content[6], '\n',
                  content[8]+content[9]+content[10], '\n',
                  content[11],'\n')


    @teststeps
    def word_share_all_info(self, content):
        """学习周报 分享页面 信息"""
        if len(content) != 6:
            print('★★★ Error - 页面中元素缺失', content)
        else:
            print('分享页：', '\n',
                  content[2] + content[3] + content[4], '\n',
                  content[5])

    @teststeps
    def month_all_info(self, content):
        """学习月报 页面 信息"""
        if len(content) != 10:
            print('★★★ Error - 页面中元素缺失', content)
        else:
            print(content[0], ' ', content[1], '\n','\n',
                  content[2], content[3], content[4], '\n',
                  content[7], '\n',
                  content[8], '\n',
                  content[9],'\n')


    @teststeps
    def month_share_all_info(self, content):
        """学习月报 分享页面 信息"""
        if len(content) != 5:
            print('★★★ Error - 页面中元素缺失', content)
        else:
            print(content[0], '分享页：', '\n',
                  content[1] + content[2] + content[3], '\n',
                  content[4])

        print('----------------------------------------------')

    @teststeps
    def swipe_up(self, a, b, c, t=500):
        """向上滑动"""
        screen = self.get_window_size()
        x1 = int(screen[0] * a)
        y1 = int(screen[1] * b)
        y2 = int(screen[1] * c)
        self.driver.swipe(x1, y1, x1, y2, t)

