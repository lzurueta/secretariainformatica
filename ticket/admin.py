from django.contrib import admin
from .models import Ministerio, NivelServicio, EstadoTicket, Ticket, TicketMovimiento, TickeTransferencias


class MinisterioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

class NivelServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tiempo_respuesta')
    search_fields = ('nombre',)
    list_filter = ('tiempo_respuesta',)

class EstadoTicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'color')
    search_fields = ('nombre',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_solicitante', 'usuario_solicitante_temp', 'usuario_ministerio', 'usuario_fuente',
                    'nivel_servicio', 'fecha_vencimiento', 'asignado_a', 'estado', 'fecha_creacion')
    search_fields = ('usuario_solicitante__username', 'tema_ayuda', 'departamento')
    list_filter = ('estado', 'nivel_servicio', 'fecha_vencimiento')
    ordering = ('-fecha_creacion',)

class TicketMovimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'operador', 'estado_anterior', 'estado_nuevo')
    search_fields = ('ticket', 'operador')
    list_filter = ('operador',)
    ordering = ('-fecha',)


class TickeTransferenciasAdmin(admin.ModelAdmin):
    list_display = ('id', 'ticket', 'operador_anterior', 'operador_nuevo', 'fecha')
    search_fields = ('ticket', 'operador_nuevo', 'operador_anterior',)
    list_filter = ('operador_nuevo',)
    ordering = ('-fecha',)


admin.site.register(Ministerio, MinisterioAdmin)
admin.site.register(NivelServicio, NivelServicioAdmin)
admin.site.register(EstadoTicket, EstadoTicketAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(TicketMovimiento, TicketMovimientoAdmin)
admin.site.register(TickeTransferencias, TickeTransferenciasAdmin)
