from django.urls import re_path

#importacion de views
from register.views import viewRegister

urlpatterns = [
    re_path(r'^', viewRegister.as_view()),  
]