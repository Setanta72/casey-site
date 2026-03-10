/* WBS Corporate Website — main.js */
(function () {
  'use strict';

  /* Mobile menu toggle */
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      mobileMenu.classList.toggle('open');
      const isOpen = mobileMenu.classList.contains('open');
      hamburger.setAttribute('aria-expanded', isOpen);
      hamburger.querySelectorAll('span')[1].style.opacity = isOpen ? '0' : '1';
      hamburger.querySelectorAll('span')[0].style.transform = isOpen ? 'rotate(45deg) translate(5px, 5px)' : '';
      hamburger.querySelectorAll('span')[2].style.transform = isOpen ? 'rotate(-45deg) translate(5px, -5px)' : '';
    });

    /* Close on outside click */
    document.addEventListener('click', function (e) {
      if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
        mobileMenu.classList.remove('open');
      }
    });
  }

  /* Highlight active nav link based on current page */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-links a, .mobile-menu a');
  navLinks.forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* Subtle scroll shadow on header */
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 10) {
        header.style.boxShadow = '0 2px 20px rgba(28,63,110,0.15)';
      } else {
        header.style.boxShadow = '0 1px 4px rgba(28,63,110,0.08)';
      }
    }, { passive: true });
  }

  /* Contact form — prevent real submission */
  const contactForm = document.querySelector('.contact-form form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const original = btn.textContent;
      btn.textContent = 'Message sent';
      btn.disabled = true;
      btn.style.background = '#2A6041';
      setTimeout(function () {
        btn.textContent = original;
        btn.disabled = false;
        btn.style.background = '';
        contactForm.reset();
      }, 3500);
    });
  }

})();
