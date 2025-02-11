from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View

from general.forms import TicketForm


# Create your views here.
class TicketNuevo(View):
    template_name = 'general/TicketNuevo.html'
    form = TicketForm()

    def get_context_data(self, **kwargs):
        form = TicketForm()
        context = {
            'titulo': "Soporte",
            "form": form,
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
            form.instance.usuario_solicitante_temp = request.POST['usuario_solicitante_temp']
            form.save()
            return redirect("TicketHome")
        else:
            print(form.errors)
            context = {
                'titulo': "Soporte",
                "form": form,
            }
            return redirect('TicketHome', contex='ADM')