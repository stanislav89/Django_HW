from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("It's Index page!!")


def main_article(request):
    return HttpResponse('This is Main article')


def archive_article(request):
    return HttpResponse('This is Archive article')


def users(request):
    return HttpResponse('This is Users article')


def user_number(request):
    return HttpResponse('This is great 89 number!')


def number_archive(request, article_id):
    return HttpResponse("This is article with Number {} {}".format(article_id, "and archive"))


def article(request, article_id, name=''):
    return HttpResponse("This is an article with number {} {}".format(article_id, "and text: {}".format(
        name) if name else "=)"))


# принимает правильные номера украинского оператора (Vodafone)
def phone_number(request):
    return HttpResponse("This is Ukrainian phone number!")


def symbols(request):
    return HttpResponse("This is correct url!")
