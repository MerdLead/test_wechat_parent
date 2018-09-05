#!/usr/bin/env python
# encoding:UTF-8  
# @Author  : SUN FEIFEI
from conf.base_page import BasePage
from utils.keyboard import keyboard


class DelEditText(BasePage):
    def del_text(self, edit_text):
        context = edit_text.text  # 获取文本框里的内容
        print('context:', context, len(context))
        if context != "" and context != '请输入备注名':
            self.edit_text_clear(len(context))  # 删除文本框中是内容

    def edit_text_clear(self, var):
        """"
            清除EditText文本框里的内容
            @param:text 要清除的内容
        """
        for i in range(var):
            keyboard('backspace')
