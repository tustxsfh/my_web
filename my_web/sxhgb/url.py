from django.urls import path
from .views import *





urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', indexview, name='index'),
    # path('sxhgb/', sxhgbview, name='sxhgb'),
    path('sxhgb/', SxhgbView.as_view(), name='sxhgb'),
    path('sucess/', SucessView.as_view(), name='study'),

]