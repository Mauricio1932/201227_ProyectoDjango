
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
#importacion sealizadores
from profileUser.serializer import UserSerializer

# Create your views here.

class userInfo (APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return 404

    def get(self,request, pk,format=None):
        print(request)
        idResponse = self.get_object(pk)
        serializer = UserSerializer(idResponse,context={'request':request})

        if idResponse != 404:
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response("Dato no encontrado", status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk, format=None):
        idResponse = self.get_object(pk)

        serializer=UserSerializer(idResponse, data=request.data,context={'request':request})
        if idResponse != 404:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else: 
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Dato no encontrado", status=status.HTTP_400_BAD_REQUEST) 