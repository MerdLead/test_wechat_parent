#!/usr/bin/env python
# code:UTF-8  
# @Author  : SUN FEIFEI

# 备注名规则：1-10字符，不限制字符格式；
remark_data = [
    {'remark': '810111111'},  # 9位数字
    {'remark': ''},  # 为空
    {'remark': '1'},   # 1位 数字
    {'remark': 'qw'},  # 2位 字母
    {'remark': ' '},  # 1个空格
    {'remark': '    '},  # 4个空格
    {'remark': 'zaqwsx'},  # 6位字母
    {'remark': '18011111'},  # 8位数字
    {'remark': '12你2hldw45'},   # 中文、数字、英文字符组合 - 10位
    {'remark': "'1q.w@S勿2:"},  # 中文、数字、英文、大写字母、空格、@、'.'字符组合 - 9位
    {'remark': '13你好2018dw@S勿', 'assert': '备注名不能超过10个字'},   # 中文、数字、英文字符组合 - 13位
    ]
