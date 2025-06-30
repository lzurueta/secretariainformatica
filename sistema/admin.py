from django.contrib import admin

from sistema.models import Profile, MenuGrupo


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'area', 'foto')


admin.site.register(Profile, ProfileAdmin)


class MenuGrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'grupo', 'nombre', 'url', 'icon')


admin.site.register(MenuGrupo, MenuGrupoAdmin)

from django.contrib import admin
from .models import Area, Usuario, Idea, Proyecto, Etapa, HoraCargada, Insumo

admin.site.register(Area)
admin.site.register(Usuario)
admin.site.register(Idea)
admin.site.register(Proyecto)
admin.site.register(Etapa)
admin.site.register(HoraCargada)
admin.site.register(Insumo)
