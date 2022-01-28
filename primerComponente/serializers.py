from rest_framework import serializers

# importarcion de modelos 
from primerComponente.models import primerModelo


class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = primerModelo
        #fields = ('id','campo_uno', 'edad')
        fields = ('__all__')
