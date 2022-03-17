from django.urls import path, re_path

from profileUser.views import userInfo 
#

urlpatterns = [
    re_path(r'^userInfo/(?P<pk>\d+)$', userInfo.as_view()),
]