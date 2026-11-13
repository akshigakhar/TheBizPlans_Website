/* Standalone EBITDA calculator; no storage, network or generator dependencies. */
(() => {
  'use strict';
  const form = document.querySelector('[data-ebitda-calculator]');
  if (!form) return;
  const results = form.querySelector('[data-results]');
  const error = form.querySelector('[data-error]');
  const money = new Intl.NumberFormat('en-CA', { style: 'currency', currency: 'CAD' });
  const percent = new Intl.NumberFormat('en-CA', { maximumFractionDigits: 2 });
  function calculate() {
    error.textContent = '';
    const values = {};
    let invalid = false;
    for (const input of form.querySelectorAll('input[type=number]')) {
      const blank = input.value === '' && !input.validity.badInput;
      const value = blank && !input.required ? 0 : input.valueAsNumber;
      const valid = Number.isFinite(value) && value >= 0 && input.validity.valid;
      input.setAttribute('aria-invalid', String(!valid));
      input.setAttribute('aria-describedby', 'calculator-error');
      invalid ||= !valid;
      values[input.name] = value;
    }
    const v = values;
    const addBack = form.querySelector('#includes-da').checked ? v.depreciation + v.amortisation : 0;
    const ebitda = v.revenue - v.cogs - v.opex + addBack;
    const margin = v.revenue === 0 ? null : ebitda / v.revenue * 100;
    if (invalid || !Number.isFinite(ebitda) || (margin !== null && !Number.isFinite(margin))) {
      error.textContent = invalid ? 'Enter a non-negative number for revenue and both cost categories. Optional amounts may be blank or non-negative.' : 'These inputs exceed the calculation range. Use smaller values.';
      results.textContent = 'Results are unavailable until the inputs are corrected.';
      return;
    }
    results.replaceChildren();
    const list = document.createElement('dl');
    for (const [label, value] of [['EBITDA', money.format(ebitda)], ['EBITDA margin', margin === null ? 'Undefined (zero revenue)' : percent.format(margin) + '%']]) {
      const pair = document.createElement('div');
      const dt = document.createElement('dt');
      const dd = document.createElement('dd');
      dt.textContent = label;
      dd.textContent = value;
      pair.append(dt, dd);
      list.append(pair);
    }
    results.append(list);
  }
  form.addEventListener('input', calculate);
  form.addEventListener('change', calculate);
  form.addEventListener('submit', event => { event.preventDefault(); calculate(); });
  calculate();
})();
