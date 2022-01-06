# posts/admin.py
from django.conf import settings
from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'pub_date', 'category',)
    list_filter = ('pub_date',)
    empty_value_display = settings.EMPTY_VALUE


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
