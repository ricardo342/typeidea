# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: apis
@time:2023/6/1
@Author:majiaqin 170479
@Desc:新建rest-framework的View层逻辑
'''
# from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from .models import Post
# from .serializers import PostSerializer
#
# @api_view()
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts, many=True)
#     return Response(post_serializers.data)
#
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .serializers import PostSerializer, PostDetailSerializer

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    # 写入时校验权限
    permission_classes = [IsAdminUser]
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super(PostViewSet, self).retrieve(request, *args, **kwargs)