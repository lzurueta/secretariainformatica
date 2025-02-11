from django.db import models
from django.contrib.auth.models import User

from general.models import Area


# Create your models here.
class Ministerio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class NivelServicio(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField()
    tiempo_respuesta = models.DurationField()

    def __str__(self):
        return self.nombre


class EstadoTicket(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Ticket(models.Model):
    usuario_solicitante = models.ForeignKey(User, blank=True,  null=True, on_delete=models.CASCADE)
    usuario_solicitante_temp = models.CharField(max_length=255, blank=True, null=True)
    usuario_mail = models.CharField(max_length=255, blank=True, null=True)
    usuario_telefono = models.CharField(max_length=255, blank=True, null=True)
    usuario_ministerio = models.ForeignKey(Ministerio, on_delete=models.CASCADE, null=True, blank=True)
    usuario_fuente = models.CharField(max_length=100,
                                      choices=[('email', 'Email'),
                                               ('telefono', 'Teléfono'),
                                               ('sistema', 'Sistema Interno')], default='sistema')
    tema_ayuda = models.CharField(max_length=255, blank=True, null=True)
    tema_ayuda_detalle = models.CharField(max_length=2000, blank=True, null=True)
    nivel_servicio = models.ForeignKey(NivelServicio, blank=True, null=True, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField(blank=True, null=True)
    asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='tickets_asignados')
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, blank=True, null=True, related_name='tickets_area')
    estado = models.ForeignKey(EstadoTicket, on_delete=models.CASCADE, default=1)
    respuesta = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    causaRaiz = models.CharField(max_length=2000, blank=True, null=True)
    accionAplicada = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return f"Ticket {self.id} - {self.usuario_solicitante}"

class TicketMovimiento(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="movimientos")
    operador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()
    estado_anterior = models.ForeignKey(EstadoTicket, on_delete=models.CASCADE, default=6, related_name='ticket_estado_anterior')
    estado_nuevo = models.ForeignKey(EstadoTicket, on_delete=models.CASCADE, default=6, related_name='ticket_estado_nuevo')

    def __str__(self):
        return f"Movimiento {self.id} - Ticket {self.ticket.id} - {self.estado_nuevo}"


class TickeTrasferir(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="ticketTrasferir")
    operador_anterior = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='operadorAnterio')
    operador_nuevo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='operadorNuevo')
    fecha = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField()

    def __str__(self):
        return f"Trasferencia {self.id} - Ticket {self.ticket.id} - {self.operador_nuevo}"
