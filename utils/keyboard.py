#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from conf.base_page import BasePage
from utils.click_bounds import ClickBounds


def keyboard(key):
    """小键盘 q w e等字母"""
    screen = BasePage().get_window_size()
    keyboard_list = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                     'a', 's', 'd', 'f', 'g', 'h', 'd', 'k', 'l',
                     'capslock', 'z', 'x', 'c', 'v', 'b', 'n', 'm', "backspace",
                     ',', '.', '-', 'blank', "'", 'enter']

    if key.lower() in keyboard_list:
        i = keyboard_list.index(key.lower())
        if i < 10:
            ClickBounds().click_bounds(0.08888 * screen[0] * (i+0.5) + 0.011 * screen[0]*(i+1), 1365)
        elif i in range(10, 19):
            ClickBounds().click_bounds((0.08888+0.011) * screen[0] * (i - 9), 1515)  # i +1-10
        elif i in range(19, 28):
            ClickBounds().click_bounds((0.08888+0.011) * screen[0] * (i - 18), 1680)  # i+1-19
        else:  # 28--32
            if i > 30:
                ClickBounds().click_bounds(0.08888 * screen[0] * (i-25+0.5) + 0.011 * screen[0]*(i - 23), 1840)  #
            else:
                ClickBounds().click_bounds(0.08888 * screen[0] * (i - 28 + 0.5) + 0.011 * screen[0] * (i - 26), 1840)

    """小键盘
    第一行： # 0.08888 * screen[0] * (i+0.5) 一个按钮大小为0.08888 * screen[0]及点击按钮中心点+0.5
            # 0.011 * screen[0]*(i+1)  按钮间隔
    第二行：# 0.08888 * screen[0] * (i-10+0.5+0.5) 一个按钮大小为0.08888 * screen[0]及点击按钮中心点+0.5及第一个按钮之前的缩进+0.5
            # 0.011 * screen[0]*(i-10+1)  按钮间隔
    第三行：  # 0.08888 * screen[0] * (i-19+0.5+0.5) 一个按钮大小为0.08888 * screen[0]及点击按钮中心点+0.5及第一个按钮之前的缩进+0.5
            # 0.011 * screen[0]*(i-19+1)  按钮间隔
    第四行：
            ！> 30: # 0.08888 * screen[0] * (i-24+0.5) 一个按钮大小为0.08888 * screen[0]及点击按钮中心点+0.5
                    # 0.011 * screen[0]*(i + 2 -26+1)  按钮间隔
            ! < 31:  # 0.08888 * screen[0] * (i-27+0.5) 一个按钮大小为0.08888 * screen[0]及点击按钮中心点+0.5
                # 0.011 * screen[0]*(i-27+1)  按钮间隔
    """
