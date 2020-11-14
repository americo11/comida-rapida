# Generated by Django 3.1.3 on 2020-11-14 14:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='fecha de nacimeinto ')),
                ('fecha_muerte', models.DateField(blank=True, null=True, verbose_name='fecha de fallecimientyo ')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='ingrese el nombre??¡???', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='ingrese el idioma', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('resumen', models.TextField(help_text='ingresa brebe descripcion', max_length=200)),
                ('isbn', models.CharField(help_text='15 cacracteres ', max_length=13, verbose_name='ISBN')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.autor')),
                ('genero', models.ManyToManyField(help_text='seeleccione el genero ', to='catalogo.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='unico', primary_key=True, serialize=False)),
                ('impreso', models.CharField(max_length=200)),
                ('devolucion', models.DateField(blank=True, null=True)),
                ('estatus', models.CharField(blank=True, choices=[('m', 'Mantenimiento'), ('p', 'prestamo'), ('d', 'disponible'), ('r', 'reservado')], default='m', help_text='disponibilidad ', max_length=10)),
                ('Libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.libro')),
                ('idioma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.idioma')),
            ],
        ),
    ]
