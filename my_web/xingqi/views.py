from django.shortcuts import render

# Create your views here.

def indexview(requests):
    return render(requests,'index.html')
