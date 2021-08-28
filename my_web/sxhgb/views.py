from django.http import request
from django.shortcuts import render
from django.views import View
from .SXHGB_V4.login import *
from .SXHGB_V4.peixun import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

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
class SxhgbView(View):
    def get(self, requests):
        return render(requests, 'sxhgb.html')

    def post(self, requests):
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        name = requests.POST.get('yourname')
        login(username, password, name)
        peixun()
        return render(requests, 'sucess.html', {'name':name})



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
