from django.urls import path

from . import views

urlpatterns = [
    path('TicketNuevo', views.TicketNuevo.as_view(), name="TicketNuevoPub"),

]
