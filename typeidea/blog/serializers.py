# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: serializers
@time:2023/6/1
@Author:majiaqin 170479
@Desc:用于序列化数据
'''
from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'category', 'desc', 'content_html', 'created_time']