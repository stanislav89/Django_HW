from django.shortcuts import render

from django.shortcuts import render
from datetime import datetime
import random
import string

# Create your views here.
from django.http import HttpResponse


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


def index(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'index.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
        'bool': True,
        'now': datetime.now(),
        'article_number': random.randint(1, 21),
        'display_num': True
    })


def second(request):
    return render(request, 'second_page.html')


def main_article(request):
    return render(request, 'article_page.html')


def article(request, article_number, slug_text=''):
    return render(request, 'number.html', {
        'article_number': article_number,  # рандомный article
        'article_number_del': article_number % 2,  # делённый по модулю article
        'slug_text': slug_text,
    })
