from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
from django.conf import settings
from django.utils.html import strip_tags
from .forms import ContactoForm
from .models import Servicio, Proyecto, Post, FAQ

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # 1. Guardamos en la base de datos
            form.save()

            # 2. Extraemos datos para el correo
            nombre = form.cleaned_data['nombre']
            email_cliente = form.cleaned_data['email']
            asunto_cliente = form.cleaned_data.get('asunto', 'Nuevo Contacto')
            mensaje_cliente = form.cleaned_data['mensaje']

            # --- ENVÍO DE CORREOS ---
            try:
                # Correo para ti (Notificación)
                asunto_para_ti = f"🚀 NUEVO LEAD: {asunto_cliente}"
                cuerpo_para_ti = f"Nombre: {nombre}\nEmail: {email_cliente}\nMensaje: {mensaje_cliente}"
                send_mail(asunto_para_ti, cuerpo_para_ti, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

                # Respuesta automática para el cliente
                asunto_auto = "Confirmación de contacto - BoostPro.cl"
                html_content = f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; border: 1px solid #eee; padding: 20px;">
                    <h2 style="color: #0dcaf0;">¡Hola {nombre}!</h2>
                    <p>He recibido tu mensaje sobre <strong>{asunto_cliente}</strong>.</p>
                    <p>Te responderé a la brevedad para ayudarte con tu requerimiento.</p>
                    <hr>
                    <p style="font-size: 12px; color: #666;"><strong>Chris - Linux Developer</strong><br>BoostPro.cl</p>
                </div>
                """
                msg = EmailMultiAlternatives(asunto_auto, strip_tags(html_content), settings.EMAIL_HOST_USER, [email_cliente])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, '¡Mensaje enviado con éxito! Revisa tu correo.')
            except Exception as e:
                
                messages.warning(request, 'Error al enviar el correo, pero el mensaje fue guardado.')
            
            return redirect('home')
    else:
        form = ContactoForm()
    
    servicios = Servicio.objects.filter(activo=True)
    proyectos = Proyecto.objects.all().order_by('orden') 
    posts = Post.objects.all().order_by('-fecha_publicacion')[:3]
   
    
    return render(request, 'web/home.html', {
        'form': form,
        'servicios': servicios,
        'proyectos': proyectos,
        'posts': posts
        
    })  

def suitecontrol(request):
    return render(request, 'web/suitecontrol.html')

def contacto(request):
    return redirect('home')

def avacif_view(request):
    return render(request, 'web/includes/avacif.html')

def detalle_post(request, slug):
    # Buscamos el post específico
    post = get_object_or_404(Post, slug=slug)
    
    # IMPORTANTE: Usa un template nuevo, no el 'include'
    return render(request, 'web/detalle_post.html', {
        'post': post
    })
    

def faq_list(request):
    faqs = FAQ.objects.all().order_by('orden')
    return render(request, 'web/faq_list.html', {'faqs': faqs})


#==========================VISTAS SERVICIOS=================================

def consulta_view(request):
    return render(request, 'web/servicios/consulta.html')

def intervencion_view(request):
    return render(request, 'web/servicios/intervencion.html')

def optimizacion_view(request):
    return render(request, 'web/servicios/optimizacion.html')


#============================ERROR 404==================================================

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404