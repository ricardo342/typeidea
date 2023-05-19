# -*- coding:utf-8 -*-
#!/usr/bin/python3
'''
@File: forms
@time:2023/4/24
@Author:majiaqin 170479
@Desc:
'''
from django import forms
from ckeditor.widgets import CKEditorWidget
from mistune import markdown

from .models import Comment

class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='昵称',
        max_length=50,
        widget=forms.widgets.Input(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    email = forms.CharField(
        label='Email',
        max_length=50,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    website = forms.CharField(
        label='网站',
        max_length=100,
        widget=forms.widgets.URLInput(
            attrs={'class': 'form-control', 'style': 'width: 60%;'}
        )
    )

    content = forms.CharField(
        widget=CKEditorWidget(),
        label='正文',
        required=True
    )

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 10:
            raise forms.ValidationError('内容长度小于10个字符, 请重新输入!')
        content = markdown(content)
        return content

    class Meta:
        model = Comment
        fields = ['nickname', 'email', 'website', 'content']