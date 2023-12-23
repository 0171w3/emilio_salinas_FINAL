from rest_framework.serializers import ModelSerializer
from .models import Inscrito, Institucion

class InscritoSerializer(ModelSerializer):
    class Meta:
        model = Inscrito
        fields = ('id', 'nombre', 'telefono', 'fecha_inscripcion', 'institucion', 'hora_inscripcion', 'estado', 'observacion')

class InstitucionSerializer(ModelSerializer):
    class Meta:
        model = Institucion
        fields = ('id', 'nombre')
