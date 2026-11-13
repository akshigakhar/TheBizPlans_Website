(function () {
    'use strict';
    const form = document.getElementById('markup-calculator');
    if (!form) return;
    const mode = document.getElementById('calculation-mode');
    const cost = document.getElementById('cost');
    const price = document.getElementById('price');
    const target = document.getElementById('target-markup');
    const outputs = ['markup-result', 'margin-result', 'profit-result', 'price-result'].map(id => document.getElementById(id));
    const error = document.getElementById('calculator-error');
    const format = new Intl.NumberFormat('en-CA', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    function calculate() {
        const useMarkup = mode.value === 'markup';
        const active = useMarkup ? target : price;
        [cost, price, target].forEach(input => input.removeAttribute('aria-invalid'));
        const c = cost.valueAsNumber;
        const value = active.valueAsNumber;
        const validCost = Number.isFinite(c) && c > 0;
        const validValue = Number.isFinite(value) && (useMarkup ? value >= 0 : value > 0);
        if (!validCost) cost.setAttribute('aria-invalid', 'true');
        if (!validValue) active.setAttribute('aria-invalid', 'true');
        const p = useMarkup ? c * (1 + value / 100) : value;
        const profit = p - c;
        const markup = profit / c * 100;
        const margin = profit / p * 100;
        if (!validCost || !validValue || ![p, profit, markup, margin].every(Number.isFinite) || p <= 0) {
            outputs.forEach(output => { output.textContent = '—'; });
            error.textContent = !validCost || !validValue ? 'Enter a cost and selling price greater than zero, or a target markup of zero or higher.' : 'These values are too large to calculate. Enter smaller amounts.';
            return;
        }
        error.textContent = '';
        [markup, margin, profit, p].forEach((value, index) => {
            outputs[index].textContent = (index < 2 ? format.format(value) : new Intl.NumberFormat('en-CA', { style: 'currency', currency: 'CAD', currencyDisplay: 'narrowSymbol' }).format(value)) + (index < 2 ? '%' : '');
        });
    }
    mode.addEventListener('change', () => {
        const useMarkup = mode.value === 'markup';
        document.getElementById('price-field').hidden = useMarkup;
        document.getElementById('markup-field').hidden = !useMarkup;
        price.disabled = useMarkup;
        price.required = !useMarkup;
        target.disabled = !useMarkup;
        target.required = useMarkup;
        calculate();
    });
    form.addEventListener('input', calculate);
    form.addEventListener('submit', event => event.preventDefault());
    calculate();
}());
