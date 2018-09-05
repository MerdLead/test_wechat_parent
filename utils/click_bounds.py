#!/usr/bin/env python
# encoding:UTF-8
from conf.base_page import BasePage


class ClickBounds(BasePage):
    """ # 小键盘回车键坐标值()
        # 小键盘删除键坐标值(990，1680)  """
    def click_bounds(self, location_x, location_y, screen_x=1080, screen_y=1920):
        # 获取当前手机屏幕大小X,Y
        screen = self.get_window_size()

        # 设定系数
        a = location_x / screen_x
        b = location_y / screen_y

        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self.driver \
            .touch('tap', {
                'x': a * screen[0],
                'y': b * screen[1]
            })
