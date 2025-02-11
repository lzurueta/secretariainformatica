from django import forms

from ticket.models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'usuario_mail',
            'usuario_telefono',
            'tema_ayuda',
            'tema_ayuda_detalle',
        ]

    def __init__(self, *args, user=None, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        if user is not None:
            dede = 1
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'