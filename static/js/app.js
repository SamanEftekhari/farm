/* ===============================
   FARM Slider
================================== */

document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".slide");
    const dots = document.querySelectorAll(".dot");

    let current = 0;

    function showSlide(index) {

        slides.forEach(slide => {
            slide.classList.remove("active");
        });

        dots.forEach(dot => {
            dot.classList.remove("active");
        });

        slides[index].classList.add("active");
        dots[index].classList.add("active");

        current = index;
    }

    function nextSlide() {

        let next = current + 1;

        if (next >= slides.length) {
            next = 0;
        }

        showSlide(next);

    }

    let timer = setInterval(nextSlide, 5000);

    dots.forEach((dot, index) => {

        dot.addEventListener("click", () => {

            clearInterval(timer);

            showSlide(index);

            timer = setInterval(nextSlide, 5000);

        });

    });

});