# Generated by Django 4.2.21 on 2025-06-07 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_lanzamiento', models.DateField()),
                ('genero', models.CharField(max_length=100)),
                ('calificacion', models.IntegerField(choices=[(1, 'Bueno'), (2, 'Muy bueno'), (3, 'Malo'), (4, 'Muy malo')])),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libros.autor')),
            ],
        ),
    ]
