# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: adminforms
@time:2023/1/28
@Author:majiaqin 170479
@Desc:自定义Form
'''
from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)