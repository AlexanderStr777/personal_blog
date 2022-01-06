# posts/urls.py
from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('notes', views.post_categories, name='post_categories'),
    path(
        'notes/<int:category_id>-<slug:slug>/',
        views.post_category,
        name='post_category'
    ),
    path(
        'note/<int:post_id>-<slug:slug>/',
        views.post,
        name='post'
    )
]
