from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ticket.forms import TicketForm
from ticket.models import NivelServicio, Ticket


# Create your views here.
class TicketHomeGestion(View):

    def get_context_data(self, **kwargs):
        context = {
            'titulo': "Soporte",
            'misticket': Ticket.objects.filter(estado=1, asignado_a=self.request.user),
            'ticket': Ticket.objects.filter(estado=1),
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'ticket/tickethomegestion.html'
        return render(request, template_name, self.get_context_data())

class TicketHome(View):

    def get_context_data(self, **kwargs):
        context = {
            'titulo': "Soporte",
            'misticket': Ticket.objects.filter(estado=1, asignado_a=self.request.user),
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'ticket/home.html'
        return render(request, template_name, self.get_context_data())


def obtener_usuario_por_cuit(request):
    cuit = request.GET.get('cuit', None)  # Captura el CUIT de la URL
    if cuit:
        try:
            usuario = User.objects.get(username=cuit)  # El CUIT es el username
            nombre_completo = f"{usuario.first_name} {usuario.last_name}"
            return JsonResponse({'success': True, 'nombre_completo': nombre_completo})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Usuario no encontrado'})
    return JsonResponse({'success': False, 'error': 'CUIT no proporcionado'})


class TicketNuevo(View):
    def get(self, request, *args, **kwargs):
        form = TicketForm()
        context = {
            'titulo': "Soporte",
            "form": form,
            "nivel_servicio": NivelServicio.objects.all().values('id', 'nombre'),
            "asignado_a": User.objects.filter(profile__tipoUsuario='Interno').values('id', 'first_name', 'last_name',
                                                                                     'profile__area__nombre')
        }
        return render(request, "ticket/nuevo.html", context)

    def post(self, request, *args, **kwargs):
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.usuario_solicitante = User.objects.get(username=request.POST['usuario_solicitante'])
            form.instance.nivel_servicio = NivelServicio.objects.get(id=request.POST['nivel_servicio'])
            form.save()
            return redirect("TicketHome")
        else:
            print(form.errors)
            context = {
                'titulo': "Soporte",
                "form": form,
                "niveles_servicio": NivelServicio.objects.all(),
                "asignado_a": User.objects.filter(profile__tipoUsuario='Interno').values('id', 'first_name',
                                                                                         'last_name',
                                                                                         'profile__area__nombre')
            }
            return render(request, "ticket/nuevo.html", context)



