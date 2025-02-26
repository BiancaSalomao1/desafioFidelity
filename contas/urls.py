from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar, name="registrar"),
    path('login/', views.logar, name="login"),
    path('logout/', views.sair, name="logout"),
]
