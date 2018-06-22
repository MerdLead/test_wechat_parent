from macaca import WebDriverException
from conf.decorator import teststep, teststeps
from conf.base_page import BasePage


class OrderPage(BasePage):
    """购买 界面"""
    @teststep
    def mine_order(self):
        """点公众号菜单- 我的账号- 我的订单的text为依据"""
        self.driver \
            .element_by_name("我的订单").click()

    @teststeps
    def wait_check_order_page(self, timeout=10000):
        """以title：“我的订单”的text为依据"""
        try:
            self.driver \
                .wait_for_element_by_name('我的订单', timeout=timeout)
            return True
        except WebDriverException:
            return False

    @teststeps
    def order_all_ele(self):
        """以“我的订单”所有元素 的父节点 xpath为依据"""
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
    def order_info(self, content):
        """我的订单页面 信息"""
        print(content[0], '页面:')
        count = []
        for i in range(len(content)):
            if content[i] == '订单详情':
                count.append(i+1)

        item = []
        for j in range(len(count)):  # count长度代表有几个订单
            if j == 0:
                item.append(content[1:count[0]])
            else:
                item.append(content[count[j-1]:count[j]])

        for k in range(len(item)):
            if '购买成功' in item[k]:
                if len(item[k]) == 5:
                    print('购买成功订单:', item[k])
                else:
                    print('★★★ Error- <购买成功订单>元素缺失:', item[k])
            elif '退款中...' in item[k]:
                if len(item[k]) == 5:
                    print('退款中订单:', item[k])
                else:
                    print('★★★ Error- <退款中订单>元素缺失:', item[k])
            elif '已退款' in item[k]:
                if len(item[k]) == 5:
                    print('已退款订单:', item[k])
                else:
                    print('★★★ Error- <已退款订单>元素缺失:', item[k])

    @teststep
    def order_details(self, index):
        """订单详情"""
        self.driver \
            .elements_by_name('订单详情')[index].click()

    # 正在拼团的订单
    @teststeps
    def time(self):
        # todo 判断时间的格式
        print('格式正确')

    @teststep
    def cancel_order(self, index):
        """取消订单"""
        self.driver \
            .elements_by_name('取消订单')[index].click()

    @teststep
    def known_button(self):
        """弹框中 '我知道了'按钮"""
        self.driver \
            .element_by_name('我知道了').click()

    # 拼团成功
    # 拼团失败- 退款中    “退款中...”
    # 拼团失败- 退款完成  ‘已退款’
    @teststeps
    def details_page_info(self, content):
        """订单详情页面 信息"""
        if len(content) != 8:
            print('★★★ Error- <订单详情>页面元素缺失:', content)
        else:
            print('<订单详情>页面:', '\n',
                  content[0], '\n',
                  '价格：', content[1], '\n',
                  '原价：', content[2], '\n',
                  content[3]+':'+content[4], '\n',
                  '学生:', content[5], '\n',
                  '有效期：', content[6], '\n',
                  content[7])

    @teststeps
    def swip_up(self):
        x, y = self.get_window_size()
        from_x = 0.5 * x
        from_y = 0.95 * y
        to_x = 0.5 * x
        to_y = 0.25 * y

        self.driver \
            .touch('drag', {
                'fromX': from_x,
                'fromY': from_y,
                'toX': to_x,
                'toY': to_y,
                'duration': 1})
