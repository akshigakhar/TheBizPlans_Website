(function (document, window) {
    "use strict";

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
