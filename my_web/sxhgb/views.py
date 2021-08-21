from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def indexview(requests):
    return render(requests, 'index.html')


@csrf_exempt
def sxhgbview(requests):
    if requests.GET:
        return render(requests, 'sxhgb.html', {})
    else:
        username = requests.POST.get('username')
        password = requests.POST.get('password')
        return render(requests, 'sxhgb.html', {})

