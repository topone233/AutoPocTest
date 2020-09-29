# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import GetIp
import FofaSpider
import FofaApi

# fofa查询语句
query = '''app="Office-Anywhere-2017-网络智能办公系统"'''
# FoFaApi开关以及配置
USE_FofaApi = False
FOFA_EMAIL = ""
FOFA_KEY = ""

if __name__ == '__main__':
    FofaSpider.banner()
    if USE_FofaApi:
        FofaApi.FoFaApi_Action(query, FOFA_EMAIL, FOFA_KEY)
    else:
        GetIp.action().IpAction()
