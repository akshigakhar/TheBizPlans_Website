(function (document, window) {
    "use strict";

    if (document.querySelector(".site-footer") && document.querySelector(".nav-cta")) {
        var bar = document.createElement("nav");
        bar.className = "mobile-consult-bar";
        bar.setAttribute("aria-label", "Contact The Biz Plans");
        bar.innerHTML = '<a class="mobile-consult-bar__call" href="tel:+16478968362">Call +1-647-896-8362</a>' +
            '<a href="/contact.html">Book a free consult</a>';
        document.body.appendChild(bar);
        document.body.classList.add("has-mobile-consult-bar");

        new ResizeObserver(function () {
            document.documentElement.style.setProperty("--mobile-consult-bar-height", bar.offsetHeight + "px");
        }).observe(bar);
    }

    document.querySelectorAll(".site-footer__more").forEach(function (button) {
        button.addEventListener("click", function () {
            var panel = document.getElementById(button.getAttribute("aria-controls"));
            var expanded = button.getAttribute("aria-expanded") === "true";
            if (!panel) return;
            panel.hidden = expanded;
            button.setAttribute("aria-expanded", String(!expanded));
            button.textContent = button.dataset[expanded ? "labelMore" : "labelLess"];
        });
    });

    var mobile = window.matchMedia("(max-width: 575.98px)");
    var categoryButtons = document.querySelectorAll(".site-footer__category-toggle");

    function setCategoryState(button, expanded) {
        var links = document.getElementById(button.getAttribute("aria-controls"));
        if (!links) return;
        button.setAttribute("aria-expanded", String(expanded));
        links.hidden = !expanded;
    }

    function syncCategories() {
        categoryButtons.forEach(function (button) {
            setCategoryState(button, !mobile.matches);
        });
    }

    categoryButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            setCategoryState(button, button.getAttribute("aria-expanded") !== "true");
        });
    });
    mobile.addEventListener("change", syncCategories);
    syncCategories();
}(document, window));
