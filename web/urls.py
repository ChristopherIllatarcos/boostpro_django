from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('suitecontrol/', views.suitecontrol, name='suitecontrol'), 
    path('contacto/', views.contacto, name='contacto'),
    path('proyectos/avacif/', views.avacif_view, name='avacif_demo'), 
    path('blog/<slug:slug>/', views.detalle_post, name='detalle_post'),
    path('preguntas-frecuentes/', views.faq_list, name='faq_list'),
    
    #================================RUTAS SERVICIOS====================================#
    
    path('servicios/consulta/', views.consulta_view, name='consulta_detalle'),
    path('servicios/intervencion/', views.intervencion_view, name='intervencion_detalle'),
    path('servicios/optimizacion/', views.optimizacion_view, name='optimizacion_detalle'),
    

    
    
    
]