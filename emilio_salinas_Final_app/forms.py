from django.forms import ModelForm
from .models import Inscrito, Institucion

class InscritoForm(ModelForm):
    class Meta:
        model = Inscrito
        fields = ('nombre', 'telefono', 'institucion', 'estado', 'observacion')

class InstitucionForm(ModelForm):
    class Meta:
        model = Institucion
        fields = ('nombre',)
