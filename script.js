document.addEventListener("DOMContentLoaded", () => {
    alert("¡Bienvenido/a!");
});
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Previene el envío por defecto
    alert("¡Gracias por contactarnos! Hemos recibido tu consulta.");
    this.submit(); // Ahora envía el formulario
});
