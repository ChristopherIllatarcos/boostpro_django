from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('suitecontrol/', views.suitecontrol, name='suitecontrol'), 
    path('contacto/', views.contacto, name='contacto'),
    path('proyectos/avacif/', views.avacif_view, name='avacif_demo'), 
]