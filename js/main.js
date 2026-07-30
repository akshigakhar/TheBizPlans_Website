(function (window, document) {
    "use strict";

    const spinner = document.getElementById('spinner');
    if (spinner) {
        spinner.remove();
    }

    if (typeof window.WOW === 'function') {
        new window.WOW().init();
    }

    const stickyNavbar = document.querySelector('.sticky-top');
    const backToTop = document.querySelector('.back-to-top');

    function updateScrollControls() {
        if (stickyNavbar) {
            const isSticky = window.scrollY > 300;
            stickyNavbar.classList.toggle('bg-primary', isSticky);
            stickyNavbar.classList.toggle('shadow-sm', isSticky);
            stickyNavbar.style.top = isSticky ? '0px' : '-150px';
        }

        if (backToTop) {
            backToTop.hidden = window.scrollY <= 100;
        }
    }

    window.addEventListener('scroll', updateScrollControls, { passive: true });
    updateScrollControls();

    if (backToTop) {
        backToTop.addEventListener('click', function (event) {
            event.preventDefault();
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // The remaining enhancements are optional. Pages may include only the
    // libraries needed by their markup without breaking shared behavior.
    const $ = window.jQuery;
    if (!$ || !$.fn) {
        return;
    }

    const counters = $('[data-toggle="counter-up"]');
    if (counters.length && typeof $.fn.counterUp === 'function') {
        counters.counterUp({ delay: 10, time: 2000 });
    }

    const testimonials = $('.testimonial-carousel');
    if (testimonials.length && typeof $.fn.owlCarousel === 'function') {
        testimonials.owlCarousel({
            items: 1,
            autoplay: true,
            smartSpeed: 1000,
            dots: true,
            loop: true,
            nav: true,
            navText: [
                '<i class="bi bi-chevron-left"></i>',
                '<i class="bi bi-chevron-right"></i>'
            ]
        });
    }
})(window, document);
