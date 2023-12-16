// script.js
const botonArriba = document.getElementById('botonArriba');

window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
        botonArriba.style.display = 'block';
    } else {
        botonArriba.style.display = 'none';
    }
});

botonArriba.addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});
