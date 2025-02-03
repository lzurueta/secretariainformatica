from django.contrib.auth.models import Group, User
from django.db import models

# Create your models here.

Group.add_to_class('home', models.CharField(max_length=150, null=True, blank=True, verbose_name="Home"))
Group.add_to_class('icon', models.CharField(max_length=150, null=True, blank=True, verbose_name="Icono"))

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(null=True, blank=True, upload_to='sistema/profile_images')
    tipoUsuario = models.CharField(max_length=20, null=True, blank=True, choices=(
        ('Interno', 'Interno'),
        ('Externo', 'Externo'),
    ), verbose_name='Tipo Usuario', default='Interno')
    area = models.ForeignKey('general.area', verbose_name='Area', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class MenuGrupo(models.Model):
    grupo = models.ForeignKey(Group, verbose_name='Grupo', on_delete=models.CASCADE)
    url = models.CharField(max_length=150, null=True, blank=True, verbose_name="url")
    nombre = models.CharField(max_length=150, null=True, blank=True, verbose_name="nombre")

    def __str__(self):
        return self.grupo.name + ' ' + self.nombre


class Ayuda(models.Model):
    grupo = models.ForeignKey(Group, verbose_name='Grupo', on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=150, null=True, blank=True, verbose_name="nombre")
    descripcion = models.CharField(max_length=10000, null=True, blank=True, verbose_name="Descripción")
    url = models.CharField(max_length=150, null=True, blank=True, verbose_name="url")

    def __str__(self):
        return self.nombre