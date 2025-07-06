# Libros Aplicacion

## Descripcion del proyecto
Este proyecto consiste en una aplicación web construida con Django + Django REST Framework para:

- Registrar libros con sus respectivos autores.
- Realizar consultas desde Postman.
- Visualizar gráficas de análisis utilizando matplotlib.
- Obtener sugerencias de libros por género y valoración.

## Requisitos y versiones

1. Python 3.8+
2. Django 4.2.21
3. Django REST Framework 3.14+
4. PostgreSQL

## Librerías utilizadas

```
asgiref==3.7.2
Django==4.2.21
djangorestframework==3.14.0
matplotlib==3.8.4
cycler==0.12.1
fonttools==4.51.0
kiwisolver==1.4.5
numpy==1.24.4
packaging==24.0
pillow==10.3.0
pyparsing==3.1.2
python-dateutil==2.9.0.post0
six==1.16.0
psycopg2==2.9.9
psycopg2-binary==2.9.9
tzdata==2024.1
```

## Instalacion y configuracion 

### Crear un entorno virtual:
```
python -m venv venv
```

### Activar entorno virtual:
```
Windows venv\Scripts\activate
```

### Instalar dependencias:
```
pip install django
pip install djangorestframework
```

### Crear el proyecto:
```
django-admin startproject Libro 
cd Libro
python manage.py startapp libros
```

## Crear la base de datos en PGAdmin4
![image](https://github.com/user-attachments/assets/d7ebb0d8-d411-4085-865d-b01f7c80602d)

### Migrar la base de datos:
```
python manage.py makemigrations
python manage.py migrate
```

### Correr el servidor:
```
python manage.py runserver
```

## Modelo de datos

El siguiente código es el modelo completo y funcional, incluye todo lo necesario para registrar libros y autores correctamente.

```python
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
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=100)
    calificacion = models.IntegerField(choices=CALIFICACIONES)

    def __str__(self):
        return self.nombre

```

## Registro de datos desde Postman (POST)

Este código es el registro de rutas (endpoints) para crear, ver y administrar libros y autores.

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, AutorViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet)
router.register(r'autores', AutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
```

```http
POST http://127.0.0.1:8000/libros/
POST http://127.0.0.1:8000/autores/

```


## Listado de libros y autores

```http
GET http://127.0.0.1:8000/libros/
```

![image](https://github.com/user-attachments/assets/8cd7a25c-a301-41d1-b7e9-e67e5edc3acc)

```http
GET http://127.0.0.1:8000/autores/
```

![image](https://github.com/user-attachments/assets/30850d4c-5261-48d0-99a9-9ad8c2f641e6)


### Visualizacion en JSON de libros: 

El serializer define cómo se ve la información

```python
from rest_framework import serializers
from .models import Libro, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.nombre', read_only=True)

    class Meta:
        model = Libro
        fields = ['id', 'nombre', 'fecha_lanzamiento', 'genero', 'calificacion', 'autor', 'autor_nombre']
```

```json
  {
        "id": 13,
        "nombre": "Sanctum",
        "fecha_lanzamiento": "2014-08-26",
        "genero": "Misterio",
        "calificacion": 3,
        "autor": 12,
        "autor_nombre": "Madeleine Roux"
    }
```

### Visualizacion en JSON de autores

```json
   {
        "id": 12,
        "nombre": "Madeleine Roux",
        "nacionalidad": "Norteamericana"
    }
```

### Eliminar 

Se especifica el ID del libro que se desea eliminar 

```http
DELETE http://127.0.0.1:8000/libros/18/
```

![image](https://github.com/user-attachments/assets/c2c524e0-f4da-4b91-91e1-fda5b8cc29ab)

![image](https://github.com/user-attachments/assets/4399785f-6be1-415d-8389-869848cbcf92)

### Actualizar

Para actualizar la informacion del Libro se debe especificar el ID

```http
PUT http://127.0.0.1:8000/libros/18/
```

Se requieren los datos del libro:

![image](https://github.com/user-attachments/assets/1800006e-8881-4aab-b0be-a7e7569a1be7)

Entonces se cambia y actualiza lo deseado:

![image](https://github.com/user-attachments/assets/47b22037-4489-434c-bf7c-f9c2d290b854)

![image](https://github.com/user-attachments/assets/50be69f0-a084-4455-b2b5-ab7b1f1f03db)


##  Scripts de análisis y visualización

Dentro del proyecto se incluyen **scripts independientes** que permiten analizar los datos registrados en la base de datos. Estos scripts utilizan `matplotlib` para generar **gráficos estadísticos**, como por ejemplo:

* Cantidad de libros por autor.
* Promedio de calificación por género.
* Sugerencias basadas en calificaciones altas.

Los scripts no forman parte del flujo del servidor Django (vistas o URLs), pero se ejecutan directamente desde la terminal para generar reportes visuales.

> Para ejecutarlos:

```bash
python Libro/graficos.py
```

Antes de ejecutar, asegurar de que el entorno virtual esté activado y que la base de datos tenga registros cargados.

Biblioteca utilizadas para los Scripts

* matplotlib.pyplot: Crear y mostrar los gráficos.
* collections.Counter: Contar elementos, como número de libros por autor o género.
* libros.models: Acceso a los modelos Libro y Autor para obtener los datos.


### Cantidad de libros por autor

Este gráfico de barras muestra cuántos libros tiene registrados cada autor en la base de datos. 

![image](https://github.com/user-attachments/assets/112bf123-3067-4e2b-b1d1-8b1c009a0d8a)

---

### Cantidad de libros por género

Representa la cantidad total de libros agrupados por género literario.

![image](https://github.com/user-attachments/assets/28dd957f-4891-4e9d-abb6-388d8af06d99)

---

### Libros según calificación

Este gráfico muestra cuántos libros se encuentran dentro de cada rango de calificación (por ejemplo, del 1 al 5). 

![image](https://github.com/user-attachments/assets/b16f3b8f-9b21-496d-80c7-6c15f711d838)

---

### Promedio de calificación por autor

Este gráfico presenta la calificación promedio de los libros escritos por cada autor. Ayuda a visualizar qué autores tienen una recepción más positiva en promedio por parte de los lectores.

```python 
def graficar_promedio_calificacion_por_autor():
```

![image](https://github.com/user-attachments/assets/094ae472-46ce-4cb4-b6d4-b05126fb8ec0)

---

### Distribución de calificaciones

Histograma que muestra la frecuencia de cada calificación asignada a los libros. Permite observar si las calificaciones están distribuidas uniformemente o si hay alguna tendencia clara (por ejemplo, mayoría de calificaciones altas o bajas).

```python
def graficar_distribucion_calificaciones():
```

![image](https://github.com/user-attachments/assets/8a0fad82-214b-465f-9958-969f4fe5c5ad)

---

### Distribución de libros por nacionalidad del autor

Gráfico circular (torta) que representa el porcentaje de libros según la nacionalidad de sus autores.

```python 
def graficar_libros_por_nacionalidad():
```

![image](https://github.com/user-attachments/assets/de8de72d-92a8-47a4-8e00-3ccd2b58243f)

Claro, aquí tenés una **descripción para tu README** especificando que el proyecto está bajo la **Licencia MIT**, lista para copiar y pegar:

---

##  Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.

Esto significa que sos libre de:

* Usar el código para fines personales o comerciales.
* Modificarlo y adaptarlo a tus necesidades.
* Compartirlo o integrarlo en otros proyectos.

**Siempre y cuando** se mantenga el aviso de copyright original y la licencia MIT.

Aquí tienes las licencias para las bibliotecas que mencionaste, en formato listo para añadir a tu README:

---

##  Licencias de las bibliotecas utilizadas

| Biblioteca                                 | Licencia                           |
| ------------------------------------------ | ---------------------------------- |
| **asgiref 3.7.2**                          | BSD‑3‑Clause ([github.com][1])     |
| **Django 4.2.21**                          | BSD‑3‑Clause *(igual que asgiref)* |
| **djangorestframework 3.14.0**             | BSD‑3‑Clause                       |
| **matplotlib 3.8.4**                       | PSF License *(compatible con BSD)* |
| **cycler 0.12.1**                          | MIT *(derivado de Matplotlib)*     |
| **fonttools 4.51.0**                       | Apache‑2.0                         |
| **kiwisolver 1.4.5**                       | BSD                                |
| **numpy 1.24.4**                           | BSD                                |
| **packaging 24.0**                         | BSD                                |
| **pillow 10.3.0**                          | PIL Software License *(BSD-like)*  |
| **pyparsing 3.1.2**                        | MIT                                |
| **python-dateutil 2.9.0.post0**            | Simplified BSD                     |
| **six 1.16.0**                             | MIT                                |
| **psycopg2 2.9.9 / psycopg2‑binary 2.9.9** | LGPL (con excepciones)             |
| **tzdata 2024.1**                          | CC0 *(público dominio)*            |





