from django.db import models
from django.utils import timezone

class Institucion(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    ESTADOS = (
        ('Res', 'Reservado'),
        ('Com', 'Completada'),
        ('Anu', 'Anulada'),
        ('NoA', 'No asisten'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=9)
    fecha_inscripcion = models.DateField()
    hora_inscripcion = models.TimeField()
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    estado = models.CharField(max_length=3, choices=ESTADOS)
    observacion = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['nombre', '-fecha_inscripcion'], name='nombre_fecha_idx'),
        ]

    def save(self, *args, **kwargs):
        self.fecha_inscripcion = timezone.now().date()
        self.hora_inscripcion = timezone.now().time()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} - {self.institucion}'



