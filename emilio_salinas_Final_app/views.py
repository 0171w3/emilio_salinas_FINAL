from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from .forms import InscritoForm, InstitucionForm
from django.views.generic import TemplateView

# Vistas basadas en funciones
def index(request):
    # Lectura de datos
    inscritos = Inscrito.objects.all()
    instituciones = Institucion.objects.all()

    # Manejo de formularios y operaciones CRUD
    if request.method == 'POST':
        if 'inscrito' in request.POST:
            form_inscrito = InscritoForm(request.POST)
            if form_inscrito.is_valid():
                form_inscrito.save()
                return redirect('index')  # Puedes redirigir a donde desees después de la creación
        elif 'institucion' in request.POST:
            form_institucion = InstitucionForm(request.POST)
            if form_institucion.is_valid():
                form_institucion.save()
                return redirect('index')  # Puedes redirigir a donde desees después de la creación
        elif 'update' in request.POST:
            # Lógica para la actualización (puedes usar formularios o directamente actualizar el objeto)
            pass
        elif 'delete' in request.POST:
            # Lógica para la eliminación (puedes usar formularios o directamente eliminar el objeto)
            pass

    # Formularios para la creación
    form_inscrito = InscritoForm()
    form_institucion = InstitucionForm()

    return render(request, 'index.html', {
        'inscritos': inscritos,
        'instituciones': instituciones,
        'form_inscrito': form_inscrito,
        'form_institucion': form_institucion,
    })

def editar_inscrito(request, id):
    # Editar un inscrito existente
    inscrito = get_object_or_404(Inscrito, id=id)

    if request.method == 'POST':
        form = InscritoForm(request.POST, instance=inscrito)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InscritoForm(instance=inscrito)

    return render(request, 'editar_inscrito.html', {'form': form, 'inscrito': inscrito})

# Vistas basadas en clases para la API
class InscritoList(APIView):
    def get(self, request):
        # Obtener lista de inscritos para la API
        inscritos = Inscrito.objects.all()
        serializer = InscritoSerializer(inscritos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        # Crear un nuevo inscrito mediante la API
        data = request.data
        serializer = InscritoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscritoDetail(APIView):
    def get(self, request, id):
        # Obtener detalles de un inscrito mediante la API
        try:
            inscrito = Inscrito.objects.get(id=id)
        except Inscrito.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InscritoSerializer(inscrito)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InstitucionList(APIView):
    def get(self, request):
        # Obtener lista de instituciones para la API
        instituciones = Institucion.objects.all()
        serializer = InstitucionSerializer(instituciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Crear una nueva institución mediante la API
        data = request.data
        serializer = InstitucionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InstitucionDetail(APIView):
    def get(self, request, id):
        # Obtener detalles de una institución mediante la API
        try:
            institucion = Institucion.objects.get(id=id)
        except Institucion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = InstitucionSerializer(institucion)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        # Actualizar una institución mediante la API
        try:
            institucion = Institucion.objects.get(id=id)
        except Institucion.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        serializer = InstitucionSerializer(institucion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


