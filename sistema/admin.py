from django.contrib import admin

from sistema.models import Profile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'area', 'foto')


admin.site.register(Profile, ProfileAdmin)
