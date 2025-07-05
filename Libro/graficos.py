import os
import django
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Libro.settings')
django.setup()

import matplotlib.pyplot as plt
from libros.models import Libro, Autor
from collections import Counter


########Contar libros por autor
autores = Autor.objects.all()
nombres = []
cantidades = []

for autor in autores:
    total = Libro.objects.filter(autor=autor).count()
    nombres.append(autor.nombre)
    cantidades.append(total)


plt.figure(figsize=(10, 6))
plt.bar(nombres, cantidades, color='skyblue')
plt.xlabel('Autor')
plt.ylabel('Cantidad de Libros')
plt.title('Cantidad de libros por autor')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()


plt.show()

#############Libros por género
generos = Libro.objects.values_list('genero', flat=True).distinct()
genero_labels = []
genero_cantidades = []

for genero in generos:
    total = Libro.objects.filter(genero=genero).count()
    genero_labels.append(genero)
    genero_cantidades.append(total)

plt.figure(figsize=(8, 6))
plt.bar(genero_labels, genero_cantidades, color='salmon')
plt.xlabel('Género')
plt.ylabel('Cantidad de Libros')
plt.title('Cantidad de libros por género')
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

##############Libros por calificación
calificaciones = Libro.objects.values_list('calificacion', flat=True).distinct()
calif_labels = sorted(list(set(calificaciones)))
calif_cantidades = []

for c in calif_labels:
    total = Libro.objects.filter(calificacion=c).count()
    calif_cantidades.append(total)

plt.figure(figsize=(7, 5))
plt.bar([str(c) for c in calif_labels], calif_cantidades, color='limegreen')
plt.xlabel('Calificación')
plt.ylabel('Cantidad de Libros')
plt.title('Libros según calificación')
plt.tight_layout()
plt.show()

#####promedio de calificaciones por autor
def graficar_promedio_calificacion_por_autor():
    autores = Autor.objects.all()
    nombres_autores = []
    promedios = []

    for autor in autores:
        libros = Libro.objects.filter(autor=autor)
        if libros.exists():
            promedio = sum(libro.calificacion for libro in libros) / libros.count()
            nombres_autores.append(autor.nombre)
            promedios.append(promedio)

    plt.figure(figsize=(10, 6))
    plt.bar(nombres_autores, promedios, color="green")
    plt.xticks(rotation=45)
    plt.title("Promedio de calificación por autor")
    plt.ylabel("Calificación promedio")
    plt.tight_layout()
    plt.show()


#####

def graficar_distribucion_calificaciones():
    calificaciones = [libro.calificacion for libro in Libro.objects.all()]

    plt.figure()
    plt.hist(calificaciones, bins=range(1, 7), edgecolor='black', color='salmon')
    plt.title('Distribución de Calificaciones')
    plt.xlabel('Calificación')
    plt.ylabel('Cantidad de Libros')
    plt.xticks(range(1, 6))
    plt.tight_layout()
    plt.show()


#######
def graficar_libros_por_nacionalidad():
    nacionalidades = [libro.autor.nacionalidad for libro in Libro.objects.all()]
    conteo = Counter(nacionalidades)

    plt.figure()
    plt.pie(conteo.values(), labels=conteo.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Distribución de Libros por Nacionalidad del Autor')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
  
    graficar_promedio_calificacion_por_autor()
    graficar_distribucion_calificaciones()
    graficar_libros_por_nacionalidad()
