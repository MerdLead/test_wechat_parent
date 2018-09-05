#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conf.decorator import teststep
from conf.base_page import BasePage


class Toast(BasePage):
    @teststep
    def find_toast(self, text, timeout=1000):
        """is toast exist, return True or False"""
        # noinspection PyBroadException
        try:
            toast = ("xpath", ".//*[contains(@text,'%s')]" % text)
            t = self.driver \
                .wait_for_element_by_xpath(toast, timeout=timeout)
            return True
        except Exception:
            return False
