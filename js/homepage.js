(function () {
  'use strict';
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('#primary-menu');
  if (!toggle || !menu) return;

  toggle.addEventListener('click', function () {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!open));
    menu.classList.toggle('open', !open);
  });

  document.querySelectorAll('.primary-nav details').forEach(function (item) {
    item.addEventListener('toggle', function () {
      if (!item.open) return;
      document.querySelectorAll('.primary-nav details[open]').forEach(function (other) {
        if (other !== item) other.removeAttribute('open');
      });
    });
  });

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    document.querySelectorAll('.primary-nav details[open]').forEach(function (item) { item.removeAttribute('open'); });
    menu.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.focus();
  });
}());
