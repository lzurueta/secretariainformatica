from django.contrib import admin
from .models import Ministerio, NivelServicio, EstadoTicket, Ticket

class MinisterioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

class NivelServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tiempo_respuesta')
    search_fields = ('nombre',)
    list_filter = ('tiempo_respuesta',)

class EstadoTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_solicitante', 'usuario_ministerio', 'usuario_fuente',
                    'nivel_servicio', 'fecha_vencimiento', 'asignado_a', 'estado', 'fecha_creacion')
    search_fields = ('usuario_solicitante__username', 'tema_ayuda', 'departamento')
    list_filter = ('estado', 'nivel_servicio', 'fecha_vencimiento')
    date_hierarchy = 'fecha_creacion'
    ordering = ('-fecha_creacion',)


admin.site.register(Ministerio, MinisterioAdmin)
admin.site.register(NivelServicio, NivelServicioAdmin)
admin.site.register(EstadoTicket, EstadoTicketAdmin)
admin.site.register(Ticket, TicketAdmin)
