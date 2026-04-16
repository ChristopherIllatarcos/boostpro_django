from django.contrib import admin
from .models import Contacto, Servicio, Proyecto, Post, FAQ, SuscriptorGuia, RecursoDigital

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
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Esto configura las columnas que verás en la lista del admin
    list_display = ('titulo', 'fecha_publicacion', 'autor')
    
    # Esto permite que el slug se complete solo mientras escribes el título
    prepopulated_fields = {'slug': ('titulo',)}
    
    # Agregamos un buscador por si llegas a tener muchos posts
    search_fields = ('titulo', 'contenido')
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden')
    list_editable = ('orden',) 
    search_fields = ('pregunta', 'respuesta')
    
# REGISTRO DE LOS NUEVOS MODELOS EN EL ADMIN
admin.site.register(SuscriptorGuia)
admin.site.register(RecursoDigital)