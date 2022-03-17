from lib2to3.pgen2 import token
from django.urls import path, re_path
from django.conf.urls import include


from Login.views import LoginAuth,MyObtainTokenPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    re_path(r'^v1/login', LoginAuth.as_view()),
    re_path(r'^v2/Auth2/', MyObtainTokenPairView.as_view()),    
    re_path(r'^v2/refresh/', TokenRefreshView.as_view()),
]