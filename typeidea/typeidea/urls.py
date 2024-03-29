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
from django.contrib.sitemaps import views as sitemap_views
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

from .custom_site import custom_site
from blog.views import (
    IndexView, CategoryView, TagView,
    PostDetailView, SearchView, AuthorView
)
from config.views import links, LinkListView
from comment.views import CommentView

from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
# from blog.apis import post_list, PostList
from blog.apis import PostViewSet

from autocomplete import CategoryAutocomplete, TagAutocomplete

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api-post')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(r'category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path(r'tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    # path('post/<post_id>.html', post_detail, name='post-detail'),
    path(r'post/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path(r'links/', links, name='links'),
    path(r'super_admin/', admin.site.urls, name='super-admin'),
    path(r'admin/', custom_site.urls, name='admin'),
    path(r'search/', SearchView.as_view(), name='search'),
    path(r'author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path(r'links/', LinkListView.as_view(), name='links'),
    path(r'comment/', CommentView.as_view(), name='comment'),
    path(r'rss|feed/', LatestPostFeed(), name='rss'),
    # path(r'sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    path(r'sitemap.xml', cache_page(60*20, key_prefix='sitemap_cache_')
        (sitemap_views.sitemap), {'sitemaps': {'posts': PostSitemap}}),
    path(r'category-autocomplete/', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    path(r'tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
    # path(r'api/post/', post_list, name='post-list'),
    # path(r'api/post/', PostList.as_view(), name='post-list'),
    path(r'api/', include(router.urls, namespace='api')),
    path(r'api/docs/', include_docs_urls(title='typeidea apis')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path(r'__debug__/', include(debug_toolbar.urls)),
        path(r'silk/', include('silk.urls', namespace='silk')),
    ] + urlpatterns
