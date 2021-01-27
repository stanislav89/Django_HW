"""blog28 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include, re_path
from new28app.views import index, main_article, archive_article, users, article, number_archive, \
    user_number, phone_number, symbols

urlpatterns = [
    path('', include('new28app.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='main_article'),
    path('article/archive/', archive_article, name='archive_article'),
    path('article/89/', user_number, name='user_number'),
    path('users/', users, name='article'),
    path('article/<int:article_id>/archive', number_archive, name='number_archive'),
    path('article/<int:article_id>/<slug:name>', article, name='article_number_text'),
    re_path(r'[0][5][0][0-9]{7}/$', phone_number, name='phone_number'),
    re_path(r'[0][6][6][0-9]{7}/$', phone_number, name='phone_number'),
    re_path(r'[0][9][5][0-9]{7}/$', phone_number, name='phone_number'),
    re_path(r'[0][9][9][0-9]{7}/$', phone_number, name='phone_number'),
    re_path(r'[1-9a-fA-F]{4}[-][0-9a-zA-Z]{6}/$', symbols, name='symbols')
]
