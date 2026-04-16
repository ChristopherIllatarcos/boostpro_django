// Usamos una constante para el formulario y verificamos que exista
const leadForm = document.getElementById('lead-form-pagina');

if (leadForm) {
    leadForm.addEventListener('submit', function(e) {
        e.preventDefault();

        // 1. Definimos el formulario para sacar la URL del atributo data-url
        const form = e.target; 
        const url = form.getAttribute('data-url'); 
        
        const email = document.getElementById('email-guia').value;
        const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

        // 2. Usamos la variable 'url' en lugar de la etiqueta de Django
        fetch(url, { 
            method: 'POST',
            headers: { 
                'X-CSRFToken': csrftoken, 
                'Content-Type': 'application/x-www-form-urlencoded' 
            },
            body: 'email=' + encodeURIComponent(email)
        })
        .then(response => {
            if (response.ok) {
                document.getElementById('registro-seccion').style.display = 'none';
                document.getElementById('descarga-seccion').style.display = 'block';
            } else {
                alert("Hubo un error al procesar el correo, compa.");
            }
        })
        .catch(error => {
            console.error('Error en el fetch:', error);
        });
    });
}

//========== Código para mostrar el Toast de seguridad después de 5 segundos ==========

document.addEventListener('DOMContentLoaded', function () {
    // 1. Buscamos el elemento HTML del Toast por su ID
    const securityToastEl = document.getElementById('securityToast');

    // 2. Si el elemento existe en la página actual...
    if (securityToastEl) {
        // 3. Inicializamos el componente Toast de Bootstrap
        const securityToast = new bootstrap.Toast(securityToastEl);

        // 4. Establecemos un retraso de 5000ms (5 segundos) antes de mostrarlo
        setTimeout(function () {
            securityToast.show(); // ¡Muestra el Toast con animación!
        }, 5000);
    }
});




function iniciarAnalisis() {
    const sintoma = document.getElementById('sintoma').value;
    document.getElementById('pantalla-inicio').classList.add('d-none');
    document.getElementById('pantalla-carga').classList.remove('d-none');

    const logs = [
        "[INFO] Conectando con el kernel local...",
        "[WAIT] Analizando procesos en segundo plano...",
        "[WARN] Detectada fragmentación de archivos críticos...",
        "[INFO] Verificando integridad de registros...",
        "[INFO] Comprobando latencia de hardware...",
        "[FIN] Análisis completado con éxito."
    ];

    let i = 0;
    let progreso = 0;
    const logTexto = document.getElementById('log-texto');
    const barra = document.getElementById('barra-progreso');

    const intervalo = setInterval(() => {
        if (i < logs.length) {
            logTexto.innerText = logs[i];
            progreso += 100 / logs.length;
            barra.style.width = progreso + "%";
            i++;
        } else {
            clearInterval(intervalo);
            mostrarResultado(sintoma);
        }
    }, 800); // Velocidad de los mensajes
}

function mostrarResultado(sintoma) {
    document.getElementById('pantalla-carga').classList.add('d-none');
    document.getElementById('pantalla-resultado').classList.remove('d-none');
    
    let mensaje = "";
    let wpMsg = "";

    if (sintoma === "lento") {
        mensaje = "Se detectó saturación de RAM y servicios de inicio innecesarios. Tu sistema necesita un 'Debloat' profundo.";
        wpMsg = "Hola, hice el escaneo y mi PC está lento. Necesito una optimización.";
    } else if (sintoma === "seguridad") {
        mensaje = "Alerta: Se encontraron firmas de procesos no firmados. Se recomienda blindaje digital inmediato.";
        wpMsg = "Hola, el escaneo detectó riesgos de seguridad. ¿Me puedes ayudar?";
    } else {
        mensaje = "Inestabilidad detectada en controladores de hardware. Tu sistema requiere mantenimiento preventivo.";
        wpMsg = "Hola, el escaneo arrojó inestabilidad. Necesito soporte técnico.";
    }

    document.getElementById('veredicto').innerText = mensaje;
    document.getElementById('btn-whatsapp').href = `https://wa.me/56975122538?text=${encodeURIComponent(wpMsg)}`;
}