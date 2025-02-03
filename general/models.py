from django.db import models

# Create your models here.

class Area(models.Model):
    padre = models.ForeignKey('self', null=True, blank=True, verbose_name='Padre', on_delete=models.CASCADE,
                              related_name='children')
    nombre = models.CharField(max_length=100, verbose_name='Nombre')

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.nombre
