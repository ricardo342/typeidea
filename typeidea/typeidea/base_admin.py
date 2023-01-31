# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: base_admin
@time:2023/1/29
@Author:majiaqin 170479
@Desc:抽象django的基类供所有app调用
'''
import django
from django.contrib import admin

class BaseOwnerAdmin(admin.ModelAdmin):
    '''
    1.用来自动补充文章,分类,标签,侧边栏,友链这些Model的owner字段
    2.用来针对queryset过滤当前用户的数据
    '''
    exclude = ('owner', )

    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        try:
            return qs.filter(owner=request.user)
        except:
            return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)