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
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    tag = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner', 'created_time']

class PostDetailSerializer(PostSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'tag', 'owner',
                  'content_html', 'created_time']