# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: user_id
@time:2023/5/8
@Author:majiaqin 170479
@Desc:给访问博客用户配置id
'''
import uuid

USER_KEY = 'uid'
TEN_YEARS = 60*60*24*365*10

class UserIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)
        return response

    def generate_uid(self, request):
        try:
            uid = request.COOKIRS[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uuid