(() => {
  'use strict';
  const table = document.getElementById('ideas-comparison');
  if (!table) return;
  const difficulty = { Easy: 0, Moderate: 1, Hard: 2 };
  const headers = [...table.tHead.rows[0].cells];
  headers.forEach((header, column) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'btn btn-link p-0 text-start fw-bold text-white';
    button.textContent = header.textContent + ' ↕';
    button.setAttribute('aria-label', 'Sort by ' + header.textContent);
    header.textContent = '';
    header.append(button);
    header.setAttribute('aria-sort', 'none');
    button.addEventListener('click', () => {
      const ascending = header.getAttribute('aria-sort') !== 'ascending';
      const rows = [...table.tBodies[0].rows];
      const value = row => {
        const text = row.cells[column].textContent.trim();
        if (column === 1) return Number(text.match(/[\d,]+/)[0].replace(/,/g, ''));
        if (column === 3) return difficulty[text];
        if (column === 2) {
          const lower = Number(text.match(/\d+/)[0]);
          return lower * (text.includes('month') ? 30 : 7);
        }
        return text;
      };
      rows.sort((a, b) => {
        const first = value(a), second = value(b);
        const result = typeof first === 'number' ? first - second : first.localeCompare(second);
        return ascending ? result : -result;
      });
      rows.forEach(row => table.tBodies[0].append(row));
      headers.forEach(item => item.setAttribute('aria-sort', 'none'));
      header.setAttribute('aria-sort', ascending ? 'ascending' : 'descending');
    });
  });
})();
