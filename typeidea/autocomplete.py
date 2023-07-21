# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: autocomplete
@time:2023/5/19
@Author:majiaqin 170479
@Desc:懒加载自动补全View层
'''

from dal import autocomplete

from blog.models import Category, Tag

class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Category.objects.none()

        qs = Category.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Tag.objects.none()

        qs = Tag.objects.filter(owner=self.request.user)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs