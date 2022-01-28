from tkinter.messagebox import NO
from django.http import response
from django.template import context
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
#importacion de modelos 
from primerComponente.models import primerModelo

#importacion sealizadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.

class PrimerViewList(APIView):
   
   def get(self, request, format=None):
        querySet=primerModelo.objects.all()
        serializer=PrimerTablaSerializer(querySet,many=True,context={'request':request})
        return Response(serializer.data)

   def post(self, request, format=None):
      serializer=PrimerTablaSerializer(data=request.data,context={'request':request})
      if serializer.is_valid():
         serializer.save()
         return Response(
            serializer.data,status=status.HTTP_201_CREATED
         )
      else: 
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class PrimerViewDetail(APIView):
   def get_object(self, pk):
      try:
         return primerModelo.objects.get(pk=pk)
      except primerModelo.DoesNotExist:
         return 404

   def get(self, request, pk, format=None):
      idResponse = self.get_object(pk)
     
      if idResponse != 404:
         serializer=PrimerTablaSerializer(idResponse,context={'request':request})
         return Response (serializer.data,status=status.HTTP_200_OK)
      else: 
         return Response ("Dato no encontrado", status=status.HTTP_400_BAD_REQUEST)  
         #serializer.errors


   def put(self,request, pk, format=None):
      idResponse = self.get_object(pk)

      if idResponse != 404:
         serializer=PrimerTablaSerializer(idResponse, data=request.data ,context={'request':request})
         if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
         else: 
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      else:
          return Response ("Id no encontrado",status=status.HTTP_400_BAD_REQUEST)
      