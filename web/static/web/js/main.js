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

    // 4. CORRECCIÓN DE VISIBILIDAD (Lo que pediste)
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