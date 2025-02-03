from django.contrib import admin

from sistema.models import Profile, MenuGrupo


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'area', 'foto')


admin.site.register(Profile, ProfileAdmin)


class MenuGrupoAdmin(admin.ModelAdmin):
    list_display = ('id', 'grupo', 'nombre', 'url', 'icon')


admin.site.register(MenuGrupo, MenuGrupoAdmin)
