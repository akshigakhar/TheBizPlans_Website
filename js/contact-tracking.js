(function () {
    'use strict';

    const measurementId = 'G-SM08Q6RPKW';
    window.dataLayer = window.dataLayer || [];
    window.gtag = window.gtag || function () {
        window.dataLayer.push(arguments);
    };
    window.gtag('js', new Date());
    // GTM owns pageviews. This Google tag is initialized for contact events.
    window.gtag('config', measurementId, { send_page_view: false });

    const googleTag = document.createElement('script');
    googleTag.async = true;
    googleTag.src = 'https://www.googletagmanager.com/gtag/js?id=' + measurementId;
    document.head.appendChild(googleTag);

    function track(eventName, linkUrl) {
        if (typeof window.gtag !== 'function') return;

        const parameters = { page_path: window.location.pathname };
        if (linkUrl !== undefined) parameters.link_url = linkUrl;
        window.gtag('event', eventName, parameters);
    }

    document.addEventListener('click', function (event) {
        if (!(event.target instanceof Element)) return;

        const link = event.target.closest('a[href]');
        if (!link) return;

        const href = link.getAttribute('href');
        const destination = href.trim().toLowerCase();
        if (destination.startsWith('tel:')) track('click_to_call', href);
        if (destination.includes('wa.me') || destination.includes('whatsapp.com')) {
            track('whatsapp_click', href);
        }
        if (destination.includes('contact') ||
            /(^|\.)setmore\.com$/.test(link.hostname) ||
            destination.startsWith('https://calendly.com/atul_jagga/business-plan-free-consult')) {
            track('book_consult_click', href);
        }
    });

    document.addEventListener('submit', function (event) {
        if (!event.defaultPrevented && event.target.matches('form.contact-form:valid')) {
            track('contact_form_submit');
        }
    });

    document.addEventListener('contact-form-success', function () {
        track('contact_form_submit');
    });
}());
