from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

class SistemaHome(View):

    def get_context_data(self, **kwargs):
        context = {
            'titulo': "Profile",
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'sistema/profile.html'
        return render(request, template_name, self.get_context_data())

class ProfileView(View):

    def get_context_data(self, **kwargs):
        context = {
            'titulo': "Profile",
        }
        return context

    def get(self, request, *args, **kwargs):
        template_name = 'sistema/profile.html'
        return render(request, template_name, self.get_context_data())


