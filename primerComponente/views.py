
from multiprocessing import context
from tkinter.messagebox import NO
from django.http import response
#from django.template import context
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

#importacion de modelos 
from primerComponente.models import primerModelo

#importacion sealizadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.

#varibales globales
responseOk = '{"messages":"success"}'
responseOk = json.loads(responseOk)

responseBad = '{"messages":"error"}'
responseBad = json.loads(responseBad)

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
         serializer=PrimerTablaSerializer(idResponse, data=request.data,context={'request':request})
         if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
         else: 
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      else:
          return Response ("Id no encontrado",status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request, pk, format=None):
      idResponse = self.get_object(pk)
      respuesta =self.response_custom(idResponse,data=request.data,context={'request':request})
      if idResponse != 404:
         idResponse.delete()
         return Response (responseOk,status= status.HTTP_204_NO_CONTENT)
      else:
         return Response (responseBad,status=status.HTTP_400_BAD_REQUEST)

      #    serializer=PrimerTablaSerializer(idResponse, data=request.data ,context={'request':request})
      #    if serializer.is_valid():
      #       idResponse.delete()
      #       return Response (serializer.data, status=status.HTTP_200_OK)
      #    else: 
      #       return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      # else:
      #     return Response ("Id no encontrado",status=status.HTTP_400_BAD_REQUEST)


   def response_custom(self,request,status):
      if status != 404:
         ...
      else:
         ...
      