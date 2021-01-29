from django.contrib import admin
from django.urls import path

from app2.views import index, main_article, second, article

urlpatterns = [
    path('', index, name='index'),
    path('article/', main_article, name='main_article'),
    path('second/', second, name='second'),
    path('article/<int:article_number>/', article, name='article'),
    path('article/<int:article_number>/<slug:slug_text>', article, name='slug_text'),
]
