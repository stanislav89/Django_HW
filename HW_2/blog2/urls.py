"""blog2 URL Configuration

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
from django.urls import path, include
from app2.views import index, main_article, article, second

urlpatterns = [
    path('', include('app2.urls')),
    path('', index, name='index'),
    path('article/', main_article, name='main_article'),
    path('second/', second, name='second'),
    path('article/<int:article_number>/', article, name='article'),
    path('article/<int:article_number>/<slug:slug_text>', article, name='slug_text'),
]
