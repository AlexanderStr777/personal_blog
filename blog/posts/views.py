# posts/views.py
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post, Category


def index(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, settings.PAGINATOR_VALUE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'page_obj': page_obj})


def post_categories(request):
    category_list = Category.objects.all()
    return render(
        request,
        'posts/post_categories.html',
        {'category_list': category_list}
    )


def post_category(request, category_id, slug):
    category = get_object_or_404(Category, id=category_id)
    post_list = category.posts.all()
    paginator = Paginator(post_list, settings.PAGINATOR_VALUE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'posts/index.html', {'page_obj': page_obj})


def post(request, post_id, slug):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post.html', {'post': post})
