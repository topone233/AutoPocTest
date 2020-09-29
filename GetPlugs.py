# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

# 导入poc或exp脚本
import plugins.tongda_oa as tongda_oa
import plugins.thinkphp_checkcode_time_sqli as thinkphp_checkcode_time_sqli


def GetPlugs(url):
    # print(tongda_oa)
    try:
        tongda_oa.test(url)
        # thinkphp_checkcode_time_sqli.thinkphp_checkcode_time_sqli_verify(url)
    except Exception as e:
        print("\033[31m[!]" + url + "异常！\033[0m")
        # print(e)
        pass