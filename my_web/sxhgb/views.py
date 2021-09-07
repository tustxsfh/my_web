from django.shortcuts import render
from django.views import View
from django.core.cache import cache
from django_redis import get_redis_connection
from .tasks import sxhgb_study


# Create your views here.
from .SXHGB_V4.login import login
from .SXHGB_V4.peixun import peixun


def indexview(requests):
    return render(requests, 'index.html')


# function views
# @csrf_exempt
# def sxhgbview(requests):
#     if requests.GET:
#         return render(requests, 'sxhgb.html', {})
#     else:
#         username = requests.POST.get('username')
#         password = requests.POST.get('password')
#         return render(requests, 'sxhgb.html', {})

# class views

# global username
# username = ''
# global password
# password = ''
# global name
# name = ''


class SxhgbView(View):

    def get(self, requests):
        return render(requests, 'sxhgb.html')

    def post(self, requests):
        redis_conn = get_redis_connection('default')
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        name = requests.POST.get('yourname')
        # login(username, password, name)
        # peixun()

        # cache.set('username', username, 60*60)
        # cache.set('password', password, 60*60)
        # cache.set('name', name, 60*60)
        redis_conn.setex('username', 60*60, username)
        redis_conn.setex('password', 60*60, password)
        redis_conn.setex('name', 60*60, name)

        sxhgb_study.delay()



        return render(requests, 'sucess.html', {'name': name})


class SucessView(View):
    def get(self, requests):
        return render(requests, 'sucess.html', )

# class StudyView(View):
#     def get(self, requests):
#
#         login(username, password, name)
#         peixun()
#         return render(requests, 'sucess.html', {})
#

# def post(self, requests):
#     username = requests.POST.get('username')
#     password = requests.POST.get('password')
#     return render(requests, 'sucess.html', {})
