from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#importo modelos 


#importacion sealizadores
from register.serializers import registerSerializer

# Create your views here.
class viewRegister(APIView):


    def post(self, request,  *args, **kwargs):
        serializer = registerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
