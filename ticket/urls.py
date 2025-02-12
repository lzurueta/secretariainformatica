from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

urlpatterns = [
    path('TicketHome', login_required(views.TicketHome.as_view()), name="TicketHome"),
    path('TicketHome/<int:opcion>/', login_required(views.TicketHome.as_view()), name="TicketHome"),
    path('TicketHomeGestion/', login_required(views.TicketHomeGestion.as_view()), name="TicketHomeGestionNoID"),
    path('TicketHomeGestion/<int:opcion>/', login_required(views.TicketHomeGestion.as_view()), name="TicketHomeGestion"),
    path('TicketNuevo', login_required(views.TicketNuevo.as_view()), name="TicketNuevo"),
    path('TicketDetalle', login_required(views.TicketDetalle.as_view()), name="TicketDetalle"),
    path('TicketTrabajar/<int:ticket>/', login_required(views.TicketTrabajar.as_view()), name="TicketTrabajar"),
    path('TickeTrasferir', login_required(views.TickeTrasferir.as_view()), name="TickeTrasferir"),
    path('TicketResumen/<int:ticket>/', login_required(views.TicketResumen.as_view()), name="TicketResumen"),
]
