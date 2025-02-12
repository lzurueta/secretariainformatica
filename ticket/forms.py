from django import forms
from .models import Ministerio, NivelServicio, EstadoTicket, Ticket, TicketMovimiento, TickeTransferencias


class MinisterioForm(forms.ModelForm):
    class Meta:
        model = Ministerio
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Ministerio'}),
        }

class NivelServicioForm(forms.ModelForm):
    class Meta:
        model = NivelServicio
        fields = ['nombre', 'descripcion', 'tiempo_respuesta']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Nivel de Servicio'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción'}),
            'tiempo_respuesta': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

class EstadoTicketForm(forms.ModelForm):
    class Meta:
        model = EstadoTicket
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del Estado'}),
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'usuario_mail',
            'usuario_telefono',
            'usuario_fuente',
            'tema_ayuda',
            'tema_ayuda_detalle',
            'asignado_a',
        ]

    def __init__(self, *args, user=None, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        if user is not None:
            dede = 1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TicketFormRecepcion(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'causaRaiz',
            'accionAplicada',
            'asignado_a',
        ]

    def __init__(self, *args, user=None, **kwargs):
        super(TicketFormRecepcion, self).__init__(*args, **kwargs)
        if user is not None:
            dede = 1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TicketMovimientoFormNuevo(forms.ModelForm):
    class Meta:
        model = TicketMovimiento
        fields = [
            'ticket',
            'comentario',
            'estado_anterior',
            'estado_nuevo',
        ]

    def __init__(self, *args, user=None, **kwargs):
        super(TicketMovimientoFormNuevo, self).__init__(*args, **kwargs)
        if user is not None:
            dede = 1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TickeTrasferirForm(forms.ModelForm):
    class Meta:
        model = TickeTransferencias
        fields = [
            'ticket',
            'operador_anterior',
            'operador_nuevo',
            'comentario',
        ]

    def __init__(self, *args, user=None, **kwargs):
        super(TickeTrasferirForm, self).__init__(*args, **kwargs)
        if user is not None:
            dede = 1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'