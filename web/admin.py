from django.contrib import admin
from .models import Contacto, Servicio, Proyecto, Post, FAQ, SuscriptorGuia, RecursoDigital, ImagenProyecto

# Register your models here.

#==========================ADMIN PARA  LOS CONTACTOS===============================#
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

#==========================ADMIN PARA  LOS SERVICIOS DE DESARROLLO A MEDIDA===============================#
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'activo')
    list_editable = ('precio', 'activo') # Edita precios sin entrar al registro
    search_fields = ('titulo',)
    

# Personalización del Header y Título del Panel
admin.site.site_header = "Panel de Control BoostPro"
admin.site.site_title = "Administración de BoostPro"
admin.site.index_title = "Bienvenido al Sistema de Gestión de Servicios y TI"


#==========================IMÁGENES DENTRO DEL PROYECTO===============================#
class ImagenProyectoInline(admin.TabularInline):
    model = ImagenProyecto
    extra = 3  # Te deja 3 espacios listos para subir fotos de Servipro de una

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Mantiene tu configuración de lista
    list_display = ('titulo', 'orden') 
    list_editable = ('orden',)
    
    # AGREGAMOS ESTA LÍNEA: Vincula la galería con la edición del proyecto
    inlines = [ImagenProyectoInline]

#==========================ADMIN PARA  LOS POST===============================#    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Esto configura las columnas que verás en la lista del admin
    list_display = ('titulo', 'fecha_publicacion', 'autor')
    
    # Esto permite que el slug se complete solo mientras escribes el título
    prepopulated_fields = {'slug': ('titulo',)}
    
    # Agregamos un buscador por si llegas a tener muchos posts
    search_fields = ('titulo', 'contenido')

#==========================ADMIN PARA  LOS FAQ===============================#    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'orden')
    list_editable = ('orden',) 
    search_fields = ('pregunta', 'respuesta')
    
# REGISTRO DE LOS NUEVOS MODELOS EN EL ADMIN
admin.site.register(SuscriptorGuia)
admin.site.register(RecursoDigital)

