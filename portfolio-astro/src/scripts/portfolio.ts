import { translations, type Lang } from '../i18n/translations';

const SUPPORTED: Lang[] = ['pt', 'en'];

const resolveKey = (obj: unknown, path: string): unknown =>
  path.split('.').reduce<unknown>((acc, key) => {
    if (acc && typeof acc === 'object' && key in (acc as Record<string, unknown>)) {
      return (acc as Record<string, unknown>)[key];
    }
    return undefined;
  }, obj);

function applyTranslations(lang: Lang) {
  const dict = translations[lang];
  document.querySelectorAll<HTMLElement>('[data-i18n]').forEach((el) => {
    const value = resolveKey(dict, el.dataset.i18n ?? '');
    if (typeof value === 'string') el.textContent = value;
  });
  document.querySelectorAll<HTMLElement>('[data-i18n-html]').forEach((el) => {
    const value = resolveKey(dict, el.dataset.i18nHtml ?? '');
    if (typeof value === 'string') el.innerHTML = value;
  });
  document.documentElement.lang = lang === 'pt' ? 'pt-BR' : 'en';
  const btn = document.getElementById('currentLang');
  if (btn) btn.textContent = lang.toUpperCase();
}

function getInitialLang(): Lang {
  const stored = localStorage.getItem('preferredLanguage');
  if (stored && (SUPPORTED as string[]).includes(stored)) return stored as Lang;
  const browser = navigator.language.toLowerCase();
  return browser.startsWith('pt') ? 'pt' : 'en';
}

function setLanguage(lang: Lang) {
  localStorage.setItem('preferredLanguage', lang);
  applyTranslations(lang);
}

function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;
  const onScroll = () => navbar.classList.toggle('scrolled', window.scrollY > 60);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

function initActiveLink() {
  const sectionIds = ['experiencia', 'sobre', 'projetos', 'contato'];
  const links = Array.from(
    document.querySelectorAll<HTMLAnchorElement>('.nav-links a'),
  );

  const update = () => {
    const scrollY = window.scrollY + 120;
    let active: string | null = null;
    for (const id of sectionIds) {
      const el = document.getElementById(id);
      if (el && el.offsetTop <= scrollY) active = id;
    }
    links.forEach((a) =>
      a.classList.toggle('active', a.getAttribute('href') === `#${active}`),
    );
  };
  update();
  window.addEventListener('scroll', update, { passive: true });
}

function initMobileNav() {
  const toggle = document.getElementById('mobileToggle');
  const mobileNav = document.getElementById('mobileNav');
  if (!toggle || !mobileNav) return;
  const icon = toggle.querySelector('i');

  const open = () => {
    mobileNav.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    icon?.classList.replace('fa-bars', 'fa-times');
    document.body.style.overflow = 'hidden';
  };
  const close = () => {
    mobileNav.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    icon?.classList.replace('fa-times', 'fa-bars');
    document.body.style.overflow = '';
  };

  toggle.addEventListener('click', () =>
    mobileNav.classList.contains('open') ? close() : open(),
  );
  mobileNav.querySelectorAll('a').forEach((a) => a.addEventListener('click', close));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileNav.classList.contains('open')) close();
  });
}

function initLangToggle() {
  const btn = document.getElementById('langToggle');
  btn?.addEventListener('click', () => {
    const current = (localStorage.getItem('preferredLanguage') as Lang) || 'pt';
    setLanguage(current === 'pt' ? 'en' : 'pt');
  });
}

function initReveal() {
  const els = document.querySelectorAll<HTMLElement>('.reveal');
  if (!('IntersectionObserver' in window)) {
    els.forEach((el) => el.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -60px 0px' },
  );
  els.forEach((el) => io.observe(el));
}

function init() {
  applyTranslations(getInitialLang());
  initNavbar();
  initActiveLink();
  initMobileNav();
  initLangToggle();
  initReveal();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}
