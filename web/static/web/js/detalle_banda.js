/* Lógica de Expansión de Imágenes - Noise Core */

document.addEventListener("DOMContentLoaded", function() {
    const modal = document.getElementById("metal-modal");
    const imgModal = document.getElementById("img-expandida");
    const closeBtn = document.querySelector(".close-modal");

    // Seleccionamos todas las imágenes que tengan la clase .grind-img
    const imagenes = document.querySelectorAll('.grind-img');

    imagenes.forEach(img => {
        img.style.cursor = "zoom-in"; 
        
        img.onclick = function() {
            modal.style.display = "block";
            imgModal.src = this.src;
            // Añadimos una animación de entrada vía JS
            imgModal.style.animation = "zoom-metal 0.3s ease-out";
        }
    });

    // Cerrar al hacer clic en la X
    if (closeBtn) {
        closeBtn.onclick = function() {
            modal.style.display = "none";
        }
    }

    // Cerrar si hacen clic en el fondo oscuro
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});