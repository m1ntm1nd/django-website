from django.urls import __path__
from django.urls.conf import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index2', index2, name='about'),
    path('index3', index3, name='parts'),
    path('index4', index4, name='teams'),
    path('info/task/<int:task_id>/', info), #http://127.0.0.1:8000/studhack/info/task/1/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]

