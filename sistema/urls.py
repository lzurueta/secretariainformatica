from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('sistemaHome', login_required(views.SistemaHome.as_view()), name="sistemaHome"),
    path('profile', login_required(views.ProfileView.as_view()), name="userProfile"),
    path('logout_view', login_required(views.logout_view.as_view()), name="logout_view"),
]
