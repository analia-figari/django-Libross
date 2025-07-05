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

<pre> ## 📦 Modelo de datos ```python class Libro(models.Model): nombre = models.CharField(max_length=200) autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros") fecha_lanzamiento = models.DateField() genero = models.CharField(max_length=100) calificacion = models.IntegerField(choices=CALIFICACIONES) def __str__(self): return self.nombre ``` </pre>


