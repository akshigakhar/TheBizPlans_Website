/* Keep the queue available before contact/generator interactions. Load GTM only
   after page resources, then yield the main thread to rendering and input. */
(function () {
    'use strict';
    window.dataLayer = window.dataLayer || [];
    var started = false;
    function start() {
        if (started) return;
        started = true;
        window.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
        var script = document.createElement('script');
        script.async = true;
        script.src = 'https://www.googletagmanager.com/gtm.js?id=GTM-NNJ2WX8Q';
        document.head.appendChild(script);
    }
    function schedule() {
        window.setTimeout(function () {
            if (window.requestIdleCallback) window.requestIdleCallback(start, { timeout: 3000 });
            else start();
        }, 1500);
    }
    if (document.readyState === 'complete') schedule();
    else window.addEventListener('load', schedule, { once: true });
}());
