from dataclasses import field
from rest_framework import serializers

# importarcion de modelos 
from loadImage.models import modeloLoadImage


class serializerLoadImage(serializers.ModelSerializer):
    class Meta:
        model = modeloLoadImage
        #fields = ('id','campo_uno', 'edad')
        #fields = ('__all__')
        fields = ('url_img','name_img','formato')

    
        