# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# #importacion de paquetes
# from django.contrib.auth.models import User
# from .serializers import RegisterSerializer
# from rest_framework import generics
#importacion sealizadores

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.
class viewRegister(generics.CreateAPIView):
        queryset = User.objects.all()
        permission_classes = (AllowAny,)
        serializer_class = RegisterSerializer


    
