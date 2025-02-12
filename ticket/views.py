from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.views import View
from ticket.forms import TicketForm, TicketFormRecepcion, TicketMovimientoFormNuevo, TickeTrasferirForm
from ticket.models import NivelServicio, Ticket, EstadoTicket, TicketMovimiento, TickeTransferencias

from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
class TicketHomeGestion(View):

    def get_context_data(self, **kwargs):
        opcion = self.kwargs.get('opcion')
        if opcion:
            oTicket = Ticket.objects.filter(estado=opcion).order_by('-fecha_creacion')
            estadoNombre = EstadoTicket.objects.get(id=opcion).nombre
        else:
            oTicket = Ticket.objects.filter(estado=1).order_by('-fecha_creacion')
            estadoNombre = 'Pendiente'

        context = {
            'titulo': "Soporte",
            'tituloOpcion': "Tickets "+estadoNombre,
            'misticket': Ticket.objects.filter(estado=1, asignado_a=self.request.user).order_by('-fecha_creacion'),
            'ticket': oTicket,
            'estados': EstadoTicket.objects.all(),
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'ticket/tickethomegestion.html'
        return render(request, template_name, self.get_context_data())

class TicketHome(View):
    def get_context_data(self, **kwargs):
        opcion = self.kwargs.get('opcion')
        if opcion:
            oTicket = Ticket.objects.filter(estado=opcion, asignado_a=self.request.user).order_by('-fecha_creacion')
            estadoNombre = EstadoTicket.objects.get(id=opcion).nombre
        else:
            oTicket = Ticket.objects.filter(estado=4, asignado_a=self.request.user).order_by('-fecha_creacion')
            estadoNombre = 'Pendiente'
        context = {
            'titulo': "Soporte",
            'estadoNombre': estadoNombre,
            'misticket': oTicket,
            'estados': EstadoTicket.objects.exclude(id__in=[1]),
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'ticket/home.html'
        return render(request, template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):
        form = TickeTrasferirForm(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.operador_anterior = User.objects.get(username=self.request.user)
            oTicket = Ticket.objects.get(id=form.instance.ticket.id)
            oTicket.estado = EstadoTicket.objects.get(id=form.instance.estado_nuevo.id)
            oTicket.save()
            form.save()
            return redirect("TicketHome")
        else:

            context = {
                'titulo': "Soporte",
                "form": form,
                "niveles_servicio": NivelServicio.objects.all(),
                "asignado_a": User.objects.filter(profile__tipoUsuario='Interno').values('id', 'first_name',
                                                                                         'last_name',
                                                                                         'profile__area__nombre')
            }
            return redirect('TicketHome')


class TicketResumen(View):

    def get_context_data(self, **kwargs):
        context = {
            'titulo': "Soporte",
            'tituloOpcion': "Tickets ",
            'ticket': Ticket.objects.get(id=self.kwargs.get('ticket')),
            'ticketMovimiento': TicketMovimiento.objects.filter(ticket=self.kwargs.get('ticket')).order_by('fecha'),
            'tickeTransferencias': TickeTransferencias.objects.filter(ticket=self.kwargs.get('ticket')).order_by('-fecha'),
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'ticket/ticketResumen.html'
        return render(request, template_name, self.get_context_data())


class TicketTrabajar(View):
    template_name = 'ticket/ticketTrabajar.html'

    def get_context_data(self, **kwargs):
        form = TicketMovimientoFormNuevo()
        ticketId = self.kwargs.get('ticket')
        context = {
            'titulo': "Soporte",
            'ticket': Ticket.objects.get(id=ticketId),
            'estado': EstadoTicket.objects.all(),
            'form': form,
            'movimientos': TicketMovimiento.objects.filter(ticket=ticketId),
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'ticket/ticketTrabajar.html'
        return render(request, template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = TicketMovimientoFormNuevo(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.instance.operador = User.objects.get(username=self.request.user)
            oTicket = Ticket.objects.get(id=form.instance.ticket.id)
            oTicket.estado = EstadoTicket.objects.get(id=form.instance.estado_nuevo.id)
            oTicket.save()
            form.save()
            return redirect("TicketHome")
        else:

            context = {
                'titulo': "Soporte",
                "form": form,
                "niveles_servicio": NivelServicio.objects.all(),
                "asignado_a": User.objects.filter(profile__tipoUsuario='Interno').values('id', 'first_name',
                                                                                         'last_name',
                                                                                         'profile__area__nombre')
            }
            return redirect('TicketHome')



class TicketNuevo(View):
    template_name = 'ticket/ticketNuevo.html'
    form = TicketForm()

    def get_context_data(self, **kwargs):
        form = TicketForm()
        context = {
            'titulo': "Soporte",
            "form": form,
            "nivel_servicio": NivelServicio.objects.all().values('id', 'nombre'),
            "asignado_a": User.objects.filter(profile__tipoUsuario='Interno').values(
                'id', 'first_name', 'last_name',
                'profile__area__nombre')
        }
        return context

    def get(self, request, *args, **kwargs):
        data = dict()
        data['html_form'] = render_to_string(self.template_name, self.get_context_data(), request=request)
        return JsonResponse(data)

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
            return redirect('TicketHome')


class TicketDetalle(View):
    template_name = 'ticket/ticketDetalle.html'

    def get_context_data(self, **kwargs):
        form = TicketFormRecepcion()
        context = {
            'titulo': "Datalle de Ticket",
            'ticket': Ticket.objects.get(id=self.request.GET['id']),
            'form': form,
            "nivele_servicio": NivelServicio.objects.all(),
            "asignado_a": User.objects.filter(profile__tipoUsuario='Interno').values('id', 'first_name',
                                                                                     'last_name',
                                                                                     'profile__area__nombre')
        }
        return context

    def get(self, request, *args, **kwargs):
        data = dict()
        data['html_form'] = render_to_string(self.template_name, self.get_context_data(), request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        form = TicketFormRecepcion(request.POST)
        if form.is_valid():
            form.save(commit=False)
            ticketUpdate = Ticket.objects.get(id=request.POST['ticketId'])
            ticketUpdate.causaRaiz = request.POST['causaRaiz']
            ticketUpdate.accionAplicada = request.POST['accionAplicada']
            ticketUpdate.asignado_a = User.objects.get(id=request.POST['asignado_a'])
            ticketUpdate.estado = EstadoTicket.objects.get(id=4)
            ticketUpdate.save()
            return redirect("TicketHomeGestion/1")
        else:
            print(form.errors)
            return redirect('TicketHomeGestion')


class TickeTrasferir(View):
    template_name = 'ticket/ticketTrasferir.html'
    form = TickeTrasferirForm()

    def get_context_data(self, **kwargs):
        form = TickeTrasferirForm()
        context = {
            'titulo': "Soporte",
            "form": form,
            "operador_nuevo": User.objects.filter(profile__tipoUsuario='Interno'),
            'ticket': Ticket.objects.get(id=self.request.GET['id']),
        }
        return context

    def get(self, request, *args, **kwargs):
        data = dict()
        data['html_form'] = render_to_string(self.template_name, self.get_context_data(), request=request)
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        form = TickeTrasferirForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            ticketUpdate = Ticket.objects.get(id=request.POST['ticket'])
            ticketUpdate.asignado_a = User.objects.get(id=request.POST['operador_nuevo'])
            ticketUpdate.save()

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
            return redirect('TicketHome')




