document.addEventListener('DOMContentLoaded', function() {
    console.log("Vista de detalle cargada correctamente.");
    
    // Animación simple de entrada para la descripción
    const descripcion = document.querySelector('.proyecto-descripcion-estatica');
    descripcion.style.opacity = '0';
    descripcion.style.transform = 'translateY(20px)';
    descripcion.style.transition = 'all 0.8s ease-out';

    setTimeout(() => {
        descripcion.style.opacity = '1';
        descripcion.style.transform = 'translateY(0)';
    }, 200);
});