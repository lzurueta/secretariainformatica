from django.contrib import admin

from general.models import Area


# Register your models here.

class AreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'padre')


admin.site.register(Area, AreaAdmin)
