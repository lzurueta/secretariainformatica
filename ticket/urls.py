from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import TicketNuevo, obtener_usuario_por_cuit, testajax

from . import views

urlpatterns = [
    path('TicketHome', login_required(views.TicketHome.as_view()), name="TicketHome"),
    path('TicketHomeGestion', login_required(views.TicketHomeGestion.as_view()), name="TicketHomeGestion"),
    path('testajax', testajax, name="testajax"),
    path('TicketNuevo/', login_required(views.TicketNuevo.as_view()), name="TicketNuevo"),
    path('obtener-usuario', obtener_usuario_por_cuit, name='obtener_usuario_por_cuit'),
]
