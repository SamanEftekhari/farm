/* ==========================================
   ASIGI FARM
   Slider
========================================== */

document.addEventListener("DOMContentLoaded", function () {

    const slides = document.querySelectorAll(".slide");
    const dots = document.querySelectorAll(".dot");

    // اگر صفحه اسلایدر ندارد (مثل صفحه نقشه)، خارج شو.
    if (slides.length === 0 || dots.length === 0) {
        return;
    }

    let current = 0;
    let timer = null;

    function showSlide(index) {

        slides.forEach(function (slide) {
            slide.classList.remove("active");
        });

        dots.forEach(function (dot) {
            dot.classList.remove("active");
        });

        slides[index].classList.add("active");
        dots[index].classList.add("active");

        current = index;
    }

    function nextSlide() {

        current++;

        if (current >= slides.length) {
            current = 0;
        }

        showSlide(current);
    }

    function startSlider() {

        if (timer) {
            clearInterval(timer);
        }

        timer = setInterval(nextSlide, 5000);
    }

    dots.forEach(function (dot, index) {

        dot.addEventListener("click", function () {

            showSlide(index);

            startSlider();

        });

    });

    showSlide(0);

    startSlider();

});