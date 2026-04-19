from django.db import models
from django.contrib.auth.models import User


# Create your models here.

#==========================NUEVO MODELO PARA CONTACTO===============================#

class Contacto(models.Model):
    # Usamos db_index=True para que las búsquedas por email sean instantáneas
    nombre = models.CharField(max_length=100)
    email = models.EmailField(db_index=True) 
    telefono = models.CharField(max_length=20, blank=True, null=True)
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    # Para saber cuándo te escribieron y ordenar por fecha rápido
    fecha_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"
        ordering = ['-fecha_envio'] # Lo más nuevo primero

    def __str__(self):
        return f"{self.nombre} - {self.asunto}"
    
#==========================NUEVO MODELO PARA SERVICIOS DE DESARROLLO A MEDIDA===============================#

class Servicio(models.Model):
    # Para gestionar tus servicios de $20.000 y $15.000 desde el Admin
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0) # Ideal para Pesos Chilenos
    icono_fa = models.CharField(max_length=50, help_text="Clase de FontAwesome (ej: fas fa-rocket)")
    imagen = models.ImageField(upload_to='servicios/', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    
 #==========================NUEVO MODELO PARA PROYECTOS DE SOFTWARE===============================#   

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/img/', null=True, blank=True)
    video = models.FileField(upload_to='proyectos/video/', null=True, blank=True) # <-- NUEVO
    link_github = models.URLField(blank=True)
    link_demo = models.URLField(blank=True) 
    orden = models.IntegerField(default=0)
    tecnologias = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo
    
# ================= NUEVO MODELO PARA GALERÍA =================
class ImagenProyecto(models.Model):
    # Relacionamos CADA imagen con UN Proyecto
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='proyectos/galeria/')
    descripcion_alt = models.CharField(max_length=100, blank=True, help_text="Texto alternativo opcional")

    def __str__(self):
        return f"Imagen de {self.proyecto.titulo}"
    
#==========================NUEVO MODELO PARA BLOG===============================#
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) # Para que la URL sea boostpro.cl/blog/mi-post
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog/', null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
#==========================NUEVO MODELO PARA PREGUNTAS FRECUENTES===============================#

class FAQ(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    orden = models.IntegerField(default=0, help_text="Orden en que se mostrará")

    class Meta:
        verbose_name = "Pregunta Frecuente"
        verbose_name_plural = "Preguntas Frecuentes"
        ordering = ['orden']

    def __str__(self):
        return self.pregunta
    
    
#==========================NUEVO MODELO PARA SUSCRIPTORES GUIA===============================#

class SuscriptorGuia(models.Model):
    email = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

#==========================NUEVO MODELO PARA RECURSOS DIGITALES (GUÍAS, EBOOKS, ETC)===============================#
class RecursoDigital(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='guias/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    



    
