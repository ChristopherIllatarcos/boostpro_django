from django.db import models

# Create your models here.


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