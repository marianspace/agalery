# Generated by Django 4.1.7 on 2023-02-17 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre', max_length=100)),
                ('apellido', models.CharField(help_text='Apellido', max_length=100)),
                ('bio', models.TextField(help_text='Descripción de la obre en 300 caracteres', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=100)),
                ('usuario', models.CharField(max_length=20)),
                ('clave', models.CharField(help_text='Contraseña alfanumerica de diez caracteres', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Titulo de la obra', max_length=200)),
                ('descripcion', models.TextField(help_text='Descripción de la obre en 300 caracteres', max_length=300)),
                ('precio', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('vendida', models.BooleanField(default=False)),
                ('artista', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='agalery.artista', verbose_name='Nombre del artista')),
            ],
        ),
        migrations.CreateModel(
            name='comprador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre', max_length=100)),
                ('apellido', models.CharField(help_text='Apellido', max_length=100)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='agalery.usuario', verbose_name='Usuario Comprador')),
            ],
        ),
        migrations.AddField(
            model_name='artista',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='agalery.usuario', verbose_name='Usuario Artista'),
        ),
    ]