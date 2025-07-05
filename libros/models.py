from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

CALIFICACIONES = [
    (1, 'Bueno'),
    (2, 'Muy bueno'),
    (3, 'Malo'),
    (4, 'Muy malo'),
]

class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=CALIFICACIONES)

    def __str__(self):
        return self.nombre