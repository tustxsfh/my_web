# -*- coding: utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time,os


from find_course import *
from find_peixun import *
from kecheng import *
from login import *
from peixun import *
from peixun_random import *


# 完成登录功能
user_list = [           # 用户列表
    {
        'ume': 'u0139528',
        'pwd': 'u0139528',
        'name': '刘泳江'
    },
    {
        'ume': 'U0139568',
        'pwd': 'cnwj423b',
        'name': '侯亮'
    },
    {
        'ume': 'u0283323',
        'pwd': 'u0283323',
        'name': '薛文杰'
    },
    {
        'ume': '18835082733',
        'pwd': 'zl142201',
        'name': '张瑶'
    },
    {
        'ume': 'u0300728',
        'pwd': 'u0300728',
        'name': '赵璨'
    },
]


for user in user_list:

    ume = user['ume']
    pwd = user['pwd']
    name = user['name']
    login(ume, pwd, name)


    # 获取专题培训url
    find_peixun_url()

    # 获取课程url
    # find_course()

    # 完成课程学习功能
    # print(name+"课程学习开始")
    # keicheng()
    # print(name+"课程学习结束")

    # 完成专题培训学习功能
    print(name+"专题培训开始")

    peixun()               # 顺序学习
    # peixun_random()           # 随机学习
    print(name+"专题培训结束")
    time.sleep(10)
    print('*******************************************************************************')






browser.quit()
exit()
