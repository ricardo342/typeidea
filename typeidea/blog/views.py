from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Post, Tag, Category
from config.models import SideBar
from comment.forms import CommentForm
from comment.models import Comment

# Create your views here.

class CommonViewMixin:
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

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({
            'comment_form': CommentForm,
            'comment_list': Comment.get_by_target(self.request.path),
        })
        return context

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