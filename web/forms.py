from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']
        
        # Quitamos bg-dark y text-white para volver a la claridad
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control border-info-subtle shadow-sm', 
                'placeholder': 'Tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-info-subtle shadow-sm', 
                'placeholder': 'tu@email.com'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control border-info-subtle shadow-sm', 
                'placeholder': '+56 9 ...'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control border-info-subtle shadow-sm', 
                'placeholder': '¿En qué puedo ayudarte?'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control border-info-subtle shadow-sm', 
                'rows': 4, 
                'placeholder': 'Cuéntame los detalles de tu equipo o proyecto...'
            }),
        }