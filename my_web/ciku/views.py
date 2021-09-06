from django.shortcuts import render

# Create your views here.

def cikuview(requests):
    return render(requests,'ciku.html')