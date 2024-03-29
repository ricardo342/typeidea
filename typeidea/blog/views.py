from datetime import date
from django.core.cache import cache
from django.db.models import Q, F
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from silk.profiling.profiler import silk_profile

from .models import Post, Tag, Category
from config.models import SideBar
from comment.forms import CommentForm
from comment.models import Comment

# Create your views here.

class CommonViewMixin:
    @silk_profile(name='get_navs')
    def get_navs(self):
        pass
    
    def get_context_data(self, **kwargs):
        context = super(CommonViewMixin, self).get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context

class IndexView(ListView):
    queryset = Post.latest_post()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

class CategoryView(IndexView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category': category,
        })
        return context

    def get_queryset(self):
        '''重写queryset, 根据分类过滤'''
        queryset = super(CategoryView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category__id=category_id)

class TagView(IndexView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag': tag,
        })
        return context

    def get_queryset(self):
        '''重写queryset, 根据标签过滤'''
        queryset = super(TagView, self).get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag__id=tag_id)

class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_post()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

    # def get(self, request, *args, **kwargs):
    #     response = super(PostDetailView, self).get(request, *args, **kwargs)
    #     Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1, uv=F('uv')+1)


    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.handle_visited()
        return response

        # 调试用
        # from django.db import connection
        # print(connection.queries)
        # return response

    def handle_visited(self):
        increase_pv = False
        increase_uv = False
        uid = self.request.uid
        pv_key = 'pv:{0}:{1}'.format(uid, self.request.path)
        uv_key = 'uv:{0}:{1}:{2}'.format(uid, str(date.today()), self.request.path)
        if not cache.get(pv_key):
            increase_pv = True
            # 设置缓存一分钟有效
            cache.set(pv_key, 1, 1*60)

        if not cache.get(uv_key):
            increase_uv = True
            # 设置缓存24小时有效
            cache.set(uv_key, 1, 24*60*60)

        if increase_pv and increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1, uv=F('uv')+1)

        elif increase_pv:
            Post.objects.filter(pk=self.object.id).update(pv=F('pv')+1)

        elif increase_uv:
            Post.objects.filter(pk=self.object.id).update(pv=F('uv')+1)

    # def get_context_data(self, **kwargs):
    #     context = super(PostDetailView, self).get_context_data(**kwargs)
    #     context.update({
    #         'comment_form': CommentForm,
    #         'comment_list': Comment.get_by_target(self.request.path),
    #     })
    #     return context

def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_post()

    context = {'category': category,
               'tag': tag,
               'post_list': post_list,
               'sidebars': SideBar.get_all(), }
    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)

def post_detail(request, post_id=None):
    try:
        post_detail = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post_detail = None

    context = {'post': post_detail,
               'sidebars': SideBar.get_all(), }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)

class PostListView(ListView):
    queryset = Post.latest_post()
    # 设置分页功能中每页条目数
    paginate_by = 1
    # 如果不设置此项,在模板中需要使用object_list变量
    context_object_name = 'post_list'
    template_name = 'blog/list.html'

class SearchView(IndexView):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data()
        context.update({
            'keyword': self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        queryset = super(SearchView, self).get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))

class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super(AuthorView, self).get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)