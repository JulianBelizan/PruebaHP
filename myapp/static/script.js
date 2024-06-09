// Capturar el movimiento de la pantalla para que, al hacerlo, se ejecute la funcion
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    // Recupero el elemento con el id indicado
    var backButton = document.getElementById("back-to-top");
    // Aca indico que si la pantalla se mueve 20 pixeles desde el inicio, agregue al boton la clase "show" que desde css le da una opacidad del 100%, body.scrollTop y documentElement.scrollTop hacen lo mismo pero por un tema de compatibilidad se usan ambos
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        backButton.classList.add("show");
    } else {
        backButton.classList.remove("show");
    }
}
// Por ultimo, al hacer click en el boton, dirige la vista hacia 0 en vertical, que seria el inicio de la pagina.
document.getElementById("back-to-top").addEventListener("click", function() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
});