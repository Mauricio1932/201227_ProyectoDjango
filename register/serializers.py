from wsgiref import validate
from rest_framework import serializers

# importarcion de modelos 
from django.contrib.auth.models import User

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password','username','email')    
        
        
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
