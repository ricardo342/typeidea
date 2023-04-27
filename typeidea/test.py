# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: test
@time:2023/2/11
@Author:majiaqin 170479
@Desc:用于测试程序代码
'''
import requests
import json
import pprint
import datetime
import random
import os, re
import time
from hyper.contrib import HTTP20Adapter

def coins_list():
    url = 'https://api.coingecko.com/api/v3/coins/list'
    header = {'accept': 'application/json'}
    r = requests.get(url, headers=header)
    return r.json()

if __name__ == '__main__':
    pprint.pprint(coins_list())
    pass