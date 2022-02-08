from distutils import extension
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
#import models
from loadImage.models import modeloLoadImage

#import serializers
from loadImage.serializers import serializerLoadImage

#varibles globales
responseOk = '{"messages":"success"}'
responseOk = json.loads(responseOk)

responseBad = '{"messages":"error"}'
responseBad = json.loads(responseBad)

# Create your views here.
class viewloadImage(APIView):
    def get(self, request, format=None):
        querySet=modeloLoadImage.objects.all()
        serializer=serializerLoadImage(querySet,many=True,context={'request':request})
        return ResponseCustom.response_custom(serializer.data,responseOk,status=status.HTTP_200_OK)
        

    def post(self, request, format=None):

        archivo = request.data['url_img']
        parseo = str(archivo)
        split = parseo.split('.')

        request.data['name_img'] = split[0]
        request.data['formato'] = split[1]

        serializer = serializerLoadImage(data=request.data, context ={'request':request })

        if serializer.is_valid():
            serializer.save()
            return ResponseCustom.response_custom(serializer.data,responseOk,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class loadImageDetail(APIView):

    def get_object(self,pk):
        try:
            return modeloLoadImage.objects.get(pk=pk)
        except modeloLoadImage.DoesNotExist:
            return 404

    def get(self,request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = serializerLoadImage(idResponse,context={'request':request})

        if idResponse != 404:
            return ResponseCustom.response_custom(serializer.data,responseOk,status=status.HTTP_200_OK)
        else:
            return ResponseCustom.response_custom("Dato no encontrado",responseBad, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        #serializer= serializerLoadImage(idResponse, data=request.data ,context={'request':request})
        
        if idResponse != 404:
            idResponse.url_img.delete()
            idResponse.delete()
            return Response (responseOk,status= status.HTTP_204_NO_CONTENT)
        else:
             return ResponseCustom.response_custom("Dato no encontrado",responseBad, status=status.HTTP_400_BAD_REQUEST)  

    def put(self,request, pk, format=None):
        idResponse = self.get_object(pk)

        if idResponse != 404:
            archivo = request.data['url_img']
            parseo = str(archivo)
            split = parseo.split('.')
            request.data['name_img'] = split[0]
            request.data['formato'] = split[1]
            serializer = serializerLoadImage(idResponse,data=request.data, context ={'request':request })
            if serializer.is_valid():
                serializer.save()
                return ResponseCustom.response_custom(serializer.data,responseOk,status=status.HTTP_200_OK)
            else: 
                return ResponseCustom.response_custom (serializer.errors,responseBad,status=status.HTTP_400_BAD_REQUEST)
        else:
            return ResponseCustom.response_custom("Dato no encontrado",responseBad, status=status.HTTP_400_BAD_REQUEST) 


  

class ResponseCustom():

    def response_custom(response, message, status):
        response = ({
            "message": message,
            "pay_load": response,
            "status": status
        })
        return Response(response)
        