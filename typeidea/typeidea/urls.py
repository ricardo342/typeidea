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
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, AuthorView
)
from config.views import links, LinkListView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(r'category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path(r'tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    # path('post/<post_id>.html', post_detail, name='post-detail'),
    path(r'post/<int:pk>.html', PostDetailView.as_view(), name='post-detail'),
    path(r'links/', links, name='links'),
    path(r'super_admin/', admin.site.urls, name='super-admin'),
    path(r'admin/', custom_site.urls, name='admin'),
    path(r'search/', SearchView.as_view(), name='search'),
    path(r'author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path(r'links/', LinkListView.as_view(), name='links'),
]
