# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: comment_block
@time:2023/4/28
@Author:majiaqin 170479
@Desc:
'''
from django import template

from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()

@register.inclusion_tag('comment/block.html')
def comment_block(target):
    return {
        'target': target,
        'comment_form': CommentForm(),
        'comment_list': Comment.get_by_target(target),
    }