/* Standalone browser calculators. No storage, network requests or generator dependencies. */
(() => {
  'use strict';
  const money = value => new Intl.NumberFormat('en-CA', { style: 'currency', currency: 'CAD' }).format(value);
  const number = value => new Intl.NumberFormat('en-CA', { maximumFractionDigits: 2 }).format(value);
  const payment = (principal, annualRate, months) => {
    const r = annualRate / 1200;
    return r === 0 ? principal / months : principal * r / -Math.expm1(-months * Math.log1p(r));
  };
  const form = document.querySelector('[data-calculator]');
  if (!form) return;
  const results = form.querySelector('[data-results]');
  const error = form.querySelector('[data-error]');
  function render(rows, note = '') {
    results.replaceChildren();
    const list = document.createElement('dl');
    for (const [label, value] of rows) {
      const pair = document.createElement('div');
      const term = document.createElement('dt');
      const detail = document.createElement('dd');
      term.textContent = label;
      detail.textContent = value;
      pair.append(term, detail);
      list.append(pair);
    }
    results.append(list);
    if (note) {
      const p = document.createElement('p');
      p.className = 'mt-3';
      p.textContent = note;
      results.append(p);
    }
  }
  function calculate() {
    error.textContent = '';
    try {
      const values = {};
      for (const input of form.querySelectorAll('input[type=number]')) {
        const value = input.valueAsNumber;
        const valid = input.value.trim() !== '' && Number.isFinite(value) && value >= 0 && input.validity.valid;
        input.setAttribute('aria-invalid', String(!valid));
        input.setAttribute('aria-describedby', input.id === 'prime' ? 'prime-help calculator-error' : 'calculator-error');
        if (!valid) throw new Error('Enter a non-negative number for every amount and rate, within any stated limit. Years must be a positive whole number.');
        values[input.name || input.id] = value;
      }
      const v = values;
      const kind = form.dataset.calculator;
      let rows = [], note = '';
      if (kind === 'break-even') {
        const contribution = v.price - v.variable;
        if (contribution <= 0) {
          render([['Contribution per unit', money(contribution)]], v.fixed > 0 ? 'No achievable break-even volume: price must exceed variable cost to cover fixed costs.' : 'Zero sales covers zero fixed costs; each additional sale contributes zero or less. No positive break-even sales target is calculated.');
          return;
        }
        const units = Math.ceil(v.fixed / contribution);
        rows = [['Break-even units (rounded up)', number(units)], ['Revenue at that volume', money(units * v.price)], ['Contribution per unit', money(contribution)]];
      } else if (kind === 'markup') {
        const profit = v.price - v.cost;
        rows = [['Gross profit per unit', money(profit)], ['Markup on cost', v.cost === 0 ? 'Undefined (zero cost)' : number(profit / v.cost * 100) + '%'], ['Gross margin on price', v.price === 0 ? 'Undefined (zero price)' : number(profit / v.price * 100) + '%']];
      } else if (kind === 'startup') {
        const sums = ['once', 'operating'].map(group => [...form.querySelectorAll(`[data-group="${group}"] [data-amount]`)].reduce((sum, el) => sum + el.valueAsNumber, 0));
        rows = [['One-time subtotal', money(sums[0])], ['First-three-months subtotal', money(sums[1])], ['Startup total', money(sums[0] + sums[1])]];
      } else {
        if (v.years <= 0 || !Number.isInteger(v.years) || !Number.isSafeInteger(v.years * 12)) throw new Error('Enter a positive whole number of years.');
        const months = v.years * 12;
        if (kind === 'loan') {
          const monthly = payment(v.principal, v.rate, months);
          rows = [['Monthly payment', money(monthly)], ['Total interest', money(Math.max(0, monthly * months - v.principal))], ['Total repaid', money(monthly * months)]];
        } else {
          const fee = (v.term + v.loc) * 0.02;
          const financed = form.elements.finance.checked;
          const termBalance = v.term * (financed ? 1.02 : 1);
          const locBalance = v.loc * (financed ? 1.02 : 1);
          if (termBalance > 1000000 || locBalance > 150000 || termBalance + locBalance > 1150000) throw new Error('The financed balance, including any financed registration fee, must stay within $1,000,000 term, $150,000 LOC and $1,150,000 combined. Reduce the advance or pay the fee separately.');
          const monthly = payment(termBalance, v.prime + 3, months);
          const locInterest = locBalance * (v.prime + 5) / 1200;
          const interest = Math.max(0, monthly * months - termBalance) + locInterest * months;
          rows = [['Term rate ceiling', number(v.prime + 3) + '%'], ['LOC rate ceiling', number(v.prime + 5) + '%'], ['Term balance to amortize', money(termBalance)], ['LOC balance outstanding at end', money(locBalance)], ['Monthly term payment', money(monthly)], ['Monthly LOC interest only', money(locInterest)], ['Combined monthly payment + interest', money(monthly + locInterest)], ['Registration fee', money(fee)], ['Upfront registration fee', money(financed ? 0 : fee)], ['Total interest over selected period', money(interest)], ['Total cost including principal, fee and interest', money(v.term + v.loc + fee + interest)]];
          note = 'LOC principal is not repaid by the displayed monthly interest. Total cost includes settling it at the end. Category limits and lender approval are not assessed.';
        }
      }
      if (rows.some(([, value]) => /NaN|∞|Infinity/.test(value))) throw new Error('These inputs exceed the calculation range. Use smaller values.');
      render(rows, note);
    } catch (err) {
      error.textContent = err.message;
      results.textContent = 'Results are unavailable until the inputs are corrected.';
    }
  }
  error.id = 'calculator-error';
  let nextRow = 0;
  for (const button of form.querySelectorAll('[data-add]')) button.hidden = false;
  // Removal is also progressive enhancement; no inactive controls without JS.
  for (const button of form.querySelectorAll('[data-remove]')) button.hidden = false;
  form.addEventListener('click', event => {
    const remove = event.target.closest('[data-remove]');
    if (remove) {
      const group = remove.closest('[data-group]');
      remove.closest('.cost-row').remove();
      group.querySelector('[data-add]').focus();
      calculate();
    }
    const add = event.target.closest('[data-add]');
    if (!add) return;
    const row = document.createElement('div');
    row.className = 'cost-row';
    const id = `custom-cost-${nextRow++}`;
    row.innerHTML = `<div><label for="${id}-label">Category</label><input class="form-control" id="${id}-label" value="Other cost"></div><div><label for="${id}">Amount ($)</label><input class="form-control" id="${id}" data-amount type="number" min="0" step="any" value="0"></div><button type="button" class="btn btn-outline-secondary" data-remove aria-label="Remove custom cost">Remove</button>`;
    add.closest('[data-group]').querySelector('[data-rows]').append(row);
    row.querySelector('input').focus();
    calculate();
  });
  form.addEventListener('submit', event => { event.preventDefault(); calculate(); });
  form.addEventListener('input', calculate);
  form.addEventListener('change', calculate);
  calculate();
})();
