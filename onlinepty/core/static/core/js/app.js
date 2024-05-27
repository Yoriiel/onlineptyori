//Smooth Scroll

function smoothScroll(target, duration) {
  const targetElement = document.querySelector(target);
  const targetPosition = targetElement.getBoundingClientRect().top;
  const startPosition = window.pageYOffset;
  const distance = targetPosition - startPosition;
  let startTime = null;

  function animation(currentTime) {
    if (startTime === null) startTime = currentTime;
    const timeElapsed = currentTime - startTime;
    const run = ease(timeElapsed, startPosition, distance, duration);
    window.scrollTo(0, run);
    if (timeElapsed < duration) requestAnimationFrame(animation);
  }

  // Easing function
  function ease(t, b, c, d) {
    t /= d / 2;
    if (t < 1) return c / 2 * t * t + b;
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
  }

  requestAnimationFrame(animation);
}


//Ampliar imagenes
function openModal(imageSrc) {
  const modal = document.getElementById('myModal');
  const modalImg = document.getElementById('modalImg');

  modal.style.display = 'flex';
  modal.style.justifyContent ='center';
  modal.style.alignItems ='center';
  modalImg.src = imageSrc;
}

function closeModal() {
  const modal = document.getElementById('myModal');
  modal.style.display = 'none';
}

//despliegue de telefono

function telefono(){
  var telef= document.getElementById("muestra")
  if(telef.style.display==="none")
  {
    telef.style.display="block"
  }

  else{
    telef.style.display="none"
  }

}
// despliegue de gps
function gps(){
  var telef= document.getElementById("gps")
  if(telef.style.display==="none")
  {
    telef.style.display="block"
  }

  else{
    telef.style.display="none"
  }

}

//carrusel
let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function nextSlide() {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide + 1) % slides.length;
  slides[currentSlide].classList.add('active');
}

function prevSlide() {
  slides[currentSlide].classList.remove('active');
  currentSlide = (currentSlide - 1 + slides.length) % slides.length;
  slides[currentSlide].classList.add('active');
}

document.addEventListener('DOMContentLoaded', function() {
  slides[currentSlide].classList.add('active');
  setInterval(nextSlide, 5000); // Cambiar de slide cada 5 segundos
});


//header function
document.addEventListener("DOMContentLoaded", function() {
  var slides = document.querySelectorAll(".slide img");
  var header = document.querySelector(".header");
  var currentSlide = 0; // Variable para mantener el índice de la diapositiva actual

  // Función para cambiar la imagen del encabezado
  function changeHeaderBackground() {
      // Obtener la URL de la imagen de la diapositiva actual
      var imageUrl = slides[currentSlide].src;
      // Establecer la imagen de fondo del encabezado
      header.style.backgroundImage = "url(" + imageUrl + ")";
      // Incrementar el índice de la diapositiva actual
      currentSlide = (currentSlide + 1) % slides.length;
  }

  // Llamar a la función para cambiar la imagen del encabezado cada 2 segundos
  setInterval(changeHeaderBackground, 4000);
});

//submit busqueda
   window.onload = function() {
            var destino = document.getElementById('buscar');
            destino.scrollIntoView({ behavior: 'smooth' });
        };

//slider dos

let currentIndex = 0;
const slideElements = document.querySelectorAll('.sli');

function nextSlide() {
  slideElements[currentIndex].classList.remove('active');
  currentIndex = (currentIndex + 1) % slideElements.length;
  slideElements[currentIndex].classList.add('active');
}

function prevSlide() {
  slideElements[currentIndex].classList.remove('active');
  currentIndex = (currentIndex - 1 + slideElements.length) % slideElements.length;
  slideElements[currentIndex].classList.add('active');
}

document.addEventListener('DOMContentLoaded', function() {
  slideElements[currentIndex].classList.add('active');
  setInterval(nextSlide, 5000); // Cambiar de slide cada 5 segundos
});

// Header function
document.addEventListener("DOMContentLoaded", function() {
  var slideImages = document.querySelectorAll(".sli img");
  var header = document.querySelector(".headerdos");
  var currentSlideIndex = 0; // Variable para mantener el índice de la diapositiva actual

  // Función para cambiar la imagen del encabezado
  function changeHeaderBackground() {
      // Obtener la URL de la imagen de la diapositiva actual
      var imageUrl = slideImages[currentSlideIndex].src;
      // Establecer la imagen de fondo del encabezado
      header.style.backgroundImage = "url(" + imageUrl + ")";
      // Incrementar el índice de la diapositiva actual
      currentSlideIndex = (currentSlideIndex + 1) % slideImages.length;
  }

  // Llamar a la función para cambiar la imagen del encabezado cada 2 segundos
  setInterval(changeHeaderBackground, 4000);
});

function showText() {
  document.getElementById("texto").style.display = "inline-block";
}

function hideText() {
  document.getElementById("texto").style.display = "none";
}


//una palabra a la vez tablero led

var palabras = document.querySelectorAll('.texto .palabra');

    // Itera sobre cada palabra y muestra una por una con un intervalo de tiempo
    palabras.forEach(function(palabra, index) {
        setTimeout(function() {
            palabra.style.visibility = 'visible'; // Muestra la palabra
        }, index * 10000); // Cambia 1000 por el tiempo deseado en milisegundos
    });

