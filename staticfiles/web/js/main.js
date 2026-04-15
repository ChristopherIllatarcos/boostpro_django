/* --- BoostPro.cl | Lógica Principal --- */

document.addEventListener('DOMContentLoaded', function() {
    
    // 1. Lógica del Loader Bar (Barra de carga superior)
    const loaderBar = document.getElementById('loader-bar');
    if (loaderBar) {
        loaderBar.style.width = '40%';
        window.addEventListener('load', () => {
            loaderBar.style.width = '100%';
            setTimeout(() => { 
                loaderBar.style.opacity = '0'; 
                setTimeout(() => loaderBar.style.display = 'none', 500);
            }, 500);
        });
    }

    // 2. Efecto de Resplandor Dinámico (Glow Point) en Glass-Cards
    document.querySelectorAll('.glass-card').forEach(card => {
        const glow = document.createElement('div');
        glow.className = 'glow-point';
        card.appendChild(glow);

        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            glow.style.display = 'block';
            glow.style.left = `${x}px`;
            glow.style.top = `${y}px`;
        });

        card.addEventListener('mouseleave', () => {
            glow.style.display = 'none';
        });
    });

    // 3. Animaciones Suaves para el Scroll (Opcional, mejora UX)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

   
    // Esto asegura que las tarjetas tengan opacidad total al aparecer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.glass-card').forEach(card => {
        // Configuramos el estado inicial directamente para no romper el CSS
        card.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(card);
    });
});

//--------------------------------------------------------------------------------------

// Botón Volver Arriba
const backToTopBtn = document.getElementById("backToTop");

// Solo ejecutamos si el botón existe en el HTML actual
if (backToTopBtn) {
    window.onscroll = function() {
        // Si bajamos más de 300px, mostramos el botón
        if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
            backToTopBtn.style.display = "block";
        } else {
            backToTopBtn.style.display = "none";
        }
    };

    // Al hacer clic, sube con efecto suave
    backToTopBtn.onclick = function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };
}

// Función para mostrar el popup de soporte en BoostPro.cl cada 5 minutos
window.addEventListener('load', () => {
    const promoModalElement = document.getElementById('promoModal');
    
    if (promoModalElement) {
        const myModal = new bootstrap.Modal(promoModalElement);
        const interval = 5 * 60 * 1000; // 5 minutos en milisegundos
        const now = new Date().getTime();
        const lastShown = localStorage.getItem('promoModalLastShown');

        // Verificamos si nunca se ha mostrado O si ya pasaron los 5 minutos
        if (!lastShown || (now - lastShown) > interval) {
            
            // Esperar 8 segundos antes de mostrarlo (para que el usuario vea el video primero)
            setTimeout(() => {
                myModal.show();
                // Guardamos el momento exacto en que se mostró
                localStorage.setItem('promoModalLastShown', now);
            }, 8000); 
        }
    }
});


// Esperar a que el DOM esté cargado
document.addEventListener('DOMContentLoaded', function() {
    
    // Verificar si el elemento del terminal existe en la página actual
    const typedElement = document.querySelector('#typed');
    
    if (typedElement) {
        new Typed('#typed', {
            stringsElement: '#typed-strings',
            typeSpeed: 35,      // Velocidad de escritura
            startDelay: 1000,   // Espera 1 segundo antes de empezar
            backSpeed: 0,       // No queremos que borre, solo que escriba
            loop: true,         // Que se repita el ciclo
            cursorChar: '█',    // Cursor sólido estilo Bash
            contentType: 'html' // Permite interpretar las etiquetas de color span
        });
    }
});


// Función para animar los contadores
const startCounters = () => {
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // A menor número, más rápido sube

    counters.forEach(counter => {
        const updateCount = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;
            const inc = target / speed;

            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 15);
            } else {
                counter.innerText = target + "+";
            }
        };
        updateCount();
    });
};

/*===========================================================================*/


// Usamos una función tradicional para evitar errores de redeclaración de const/let
function iniciarContadoresPro() {
    const counters = document.querySelectorAll('.counter');
    const speed = 100;

    counters.forEach(counter => {
        const target = +counter.getAttribute('data-target');
        
        const updateCount = () => {
            const currentText = counter.innerText.replace(/[^0-9]/g, '');
            const count = +currentText;
            const inc = Math.max(target / speed, 1);

            if (count < target) {
                counter.innerText = Math.ceil(count + inc);
                setTimeout(updateCount, 20);
            } else {
                // Formateo final
                if (target === 100) {
                    counter.innerText = "100%";
                } else if (target >= 50) {
                    counter.innerText = target + "+";
                } else {
                    counter.innerText = target;
                }
            }
        };
        updateCount();
    });
}

// Observer con nombre único para evitar conflictos
(function() {
    const observerOptions = { threshold: 0.2 };
    const counterObserverBoost = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                iniciarContadoresPro();
                counterObserverBoost.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.addEventListener('DOMContentLoaded', () => {
        const targetSection = document.querySelector('.counter');
        if (targetSection) {
            counterObserverBoost.observe(targetSection);
        }
    });
})();


