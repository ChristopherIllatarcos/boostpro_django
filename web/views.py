from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
from django.conf import settings
from django.utils.html import strip_tags
from .forms import ContactoForm
from .models import Servicio, Proyecto 

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Mensaje enviado con éxito!')
            return redirect('home')
    else:
        form = ContactoForm()
    
    # --- AQUÍ ESTÁ EL CAMBIO: Traemos la info de la Base de Datos ---
    servicios = Servicio.objects.filter(activo=True)
    proyectos = Proyecto.objects.all().order_by('orden') 
    
    # Mandamos todo al HTML dentro del diccionario final
    return render(request, 'web/home.html', {
        'form': form,
        'servicios': servicios,
        'proyectos': proyectos
    })


def suitecontrol(request):
    return render(request, 'web/suitecontrol.html')

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Extraemos los datos limpios del Form
            nombre = form.cleaned_data['nombre']
            email_cliente = form.cleaned_data['email']
            telefono = form.cleaned_data['telefono'] # Nuevo campo
            asunto_cliente = form.cleaned_data['asunto']
            mensaje_cliente = form.cleaned_data['mensaje']

            # Guardar en la base de datos (opcional, pero recomendado)
            form.save()

            # --- 1. NOTIFICACIÓN PARA TI (Chris) ---
            asunto_para_ti = f"🚀 NUEVO LEAD: {asunto_cliente}"
            cuerpo_para_ti = f"Nombre: {nombre}\nEmail: {email_cliente}\nTeléfono: {telefono}\nMensaje: {mensaje_cliente}"
            
            try:
                # Envío a ti
                send_mail(asunto_para_ti, cuerpo_para_ti, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

                # --- 2. RESPUESTA AUTOMÁTICA HTML PARA EL CLIENTE ---
                asunto_auto = f"Confirmación de contacto - BoostPro.cl"
                html_content = f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; border: 1px solid #eee; border-radius: 10px; padding: 20px;">
                    <h2 style="color: #0dcaf0; text-align: center;">¡Hola {nombre}!</h2>
                    <p>Gracias por contactar a <strong>BoostPro.cl</strong>. He recibido tu mensaje sobre <strong>{asunto_cliente}</strong>.</p>
                    <p style="background-color: #f8f9fa; padding: 15px; border-left: 5px solid #0dcaf0;">
                        <em>"{mensaje_cliente}"</em>
                    </p>
                    <p>Revisaré los detalles técnicos y te responderé lo antes posible para ayudarte con tu requerimiento.</p>
                    <hr style="border: 0; border-top: 1px solid #eee; margin: 20px 0;">
                    <p style="text-align: center; color: #666; font-size: 12px;">
                        <strong>Chris - Linux Developer</strong><br>
                        Especialista en Soporte, Optimización y Desarrollo de Software<br>
                        Región de Valparaíso, Chile
                    </p>
                    <div style="text-align: center; margin-top: 20px;">
                        <a href="https://wa.me/56926231939" style="background-color: #25d366; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Hablar por WhatsApp</a>
                    </div>
                </div>
                """
                text_content = strip_tags(html_content) 

                msg = EmailMultiAlternatives(asunto_auto, text_content, settings.EMAIL_HOST_USER, [email_cliente])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.success(request, "¡Mensaje enviado con éxito! Revisa tu correo.")
                return redirect('home')
                
            except Exception as e:
                messages.error(request, "Error al enviar el correo, pero el mensaje fue guardado.")
                return redirect('home')
        else:
            messages.error(request, "Hubo un error en el formulario. Revisa los datos.")
    
    # Si es GET, cargamos la home con el formulario
    servicios = Servicio.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'web/home.html', {
        'servicios': servicios,
        'proyectos': proyectos,
        'form': ContactoForm()
    })

def avacif_view(request):
    return render(request, 'web/includes/avacif.html')