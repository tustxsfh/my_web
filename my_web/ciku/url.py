from django.urls import path
from .views import *





urlpatterns = [
    path('ciku/', cikuview, name='ciku'),

]