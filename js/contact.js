(function (window, document) {
    "use strict";

    const form = document.getElementById("contact-form");
    const successPanel = document.getElementById("contact-success");

    if (!form || !successPanel || !window.fetch) {
        return;
    }

    const submitButton = form.querySelector('button[type="submit"]');
    const submitLabel = form.querySelector(".contact-submit-label");
    const loadingLabel = form.querySelector(".contact-submit-loading");
    const status = form.querySelector(".contact-form-status");
    const unavailableMessage = "We could not send your message online. Please email info@thebizplans.com or call +1 (647) 896-8362.";

    async function readJsonResponse(response) {
        const contentType = response.headers.get("content-type") || "";

        if (!contentType.toLowerCase().includes("application/json")) {
            return null;
        }

        try {
            return await response.json();
        } catch (error) {
            return null;
        }
    }

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        if (!form.reportValidity()) {
            return;
        }

        submitButton.disabled = true;
        submitLabel.hidden = true;
        loadingLabel.hidden = false;
        status.textContent = "";
        status.classList.remove("contact-form-status--error");

        try {
            const response = await window.fetch(form.action, {
                method: "POST",
                body: new window.FormData(form),
                headers: { "Accept": "application/json" }
            });
            const result = await readJsonResponse(response);

            if (!response.ok || !result || !result.success) {
                throw new Error(result && result.message ? result.message : unavailableMessage);
            }

            form.reset();
            form.hidden = true;
            successPanel.hidden = false;
            successPanel.focus();
        } catch (error) {
            status.textContent = error.message || unavailableMessage;
            status.classList.add("contact-form-status--error");
        } finally {
            submitButton.disabled = false;
            submitLabel.hidden = false;
            loadingLabel.hidden = true;
        }
    });
})(window, document);
