"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .custom_site import custom_site
from typeidea.blog.views import post_list, post_detail
from typeidea.config.views import links


urlpatterns = [
    path(r'super_admin/', admin.site.urls),
    path(r'admin/', custom_site.urls),
    path('^$', post_list),
    path(r'^category/(?P<category_id>\d+)/$', post_list),
    path(r'^tag/(?P<tag_id>\d+)/$', post_list),
    path(r'^post/(?P<post_id>\d+).html$', post_detail),
    path(r'^links/$', links),
]
