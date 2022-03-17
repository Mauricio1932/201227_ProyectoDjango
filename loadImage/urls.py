from django.urls import re_path
from django.conf.urls import include

from loadImage.views import viewloadImage
from loadImage.views import loadImageDetail

urlpatterns = [
    re_path(r'^imagen/$', viewloadImage.as_view()),  
    re_path(r'^imagen/(?P<pk>\d+)$',loadImageDetail.as_view()),
]
