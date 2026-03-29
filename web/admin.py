from django.contrib import admin
from .models import Contacto, Servicio, Proyecto

# Register your models here.

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    # Columnas que verás en la tabla principal
    list_display = ('nombre', 'email', 'asunto', 'fecha_envio')
    
    # Buscador rápido (Optimización SQL)
    search_fields = ('nombre', 'email', 'asunto')
    
    # Filtro lateral para ver mensajes por fecha
    list_filter = ('fecha_envio',)
    
    # Hace que la fecha no se pueda editar manualmente
    readonly_fields = ('fecha_envio',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'activo')
    list_editable = ('precio', 'activo') # Edita precios sin entrar al registro
    search_fields = ('titulo',)

# Personalización del Header y Título del Panel
admin.site.site_header = "Panel de Control BoostPro"
admin.site.site_title = "Administración de BoostPro"
admin.site.index_title = "Bienvenido al Sistema de Gestión de Servicios y TI"

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # IMPORTANTE: El primer campo (titulo) NO debe estar en list_editable
    list_display = ('titulo', 'orden') 
    list_editable = ('orden',)