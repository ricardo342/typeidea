# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: custom_site
@time:2023/1/28
@Author:majiaqin 170479
@Desc:自定义Site
'''
from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')