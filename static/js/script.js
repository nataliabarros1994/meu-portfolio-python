/**
 * Portfolio JavaScript - Natália Barros
 * Scripts para interatividade e animações
 */

// ============================================
// DOM READY
// ============================================
document.addEventListener('DOMContentLoaded', function() {
    initBackToTop();
    initNavbarScroll();
    initSmoothScroll();
    initProjectFilters();
    initFormValidation();
    initLazyLoading();
    initTooltips();
});

// ============================================
// BACK TO TOP BUTTON
// ============================================
function initBackToTop() {
    const backToTopBtn = document.getElementById('backToTop');

    if (!backToTopBtn) return;

    // Mostrar/ocultar botão baseado no scroll
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }
    });

    // Scroll suave ao topo
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// ============================================
// NAVBAR SCROLL EFFECT
// ============================================
function initNavbarScroll() {
    const navbar = document.querySelector('.navbar');

    if (!navbar) return;

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.padding = '0.5rem 0';
            navbar.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
        } else {
            navbar.style.padding = '1rem 0';
            navbar.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        }
    });
}

// ============================================
// SMOOTH SCROLL
// ============================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Ignorar se for apenas "#"
            if (href === '#') return;

            e.preventDefault();

            const target = document.querySelector(href);
            if (target) {
                const offsetTop = target.offsetTop - 80; // 80px para compensar navbar fixa

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ============================================
// PROJECT FILTERS
// ============================================
function initProjectFilters() {
    const filterButtons = document.querySelectorAll('[data-filter]');

    if (filterButtons.length === 0) return;

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            const filterValue = this.getAttribute('data-filter');

            // Atualizar botão ativo
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            // Filtrar projetos
            const projects = document.querySelectorAll('.project-card');

            projects.forEach(project => {
                if (filterValue === 'all') {
                    project.parentElement.style.display = 'block';
                } else {
                    const category = project.getAttribute('data-category');
                    if (category === filterValue) {
                        project.parentElement.style.display = 'block';
                    } else {
                        project.parentElement.style.display = 'none';
                    }
                }
            });
        });
    });
}

// ============================================
// FORM VALIDATION
// ============================================
function initFormValidation() {
    const forms = document.querySelectorAll('.needs-validation');

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

            form.classList.add('was-validated');
        }, false);
    });

    // Validação em tempo real para o formulário de contato
    const contactForm = document.getElementById('contactForm');

    if (contactForm) {
        const inputs = contactForm.querySelectorAll('input, textarea');

        inputs.forEach(input => {
            input.addEventListener('blur', function() {
                if (this.checkValidity()) {
                    this.classList.remove('is-invalid');
                    this.classList.add('is-valid');
                } else {
                    this.classList.remove('is-valid');
                    this.classList.add('is-invalid');
                }
            });

            // Remover classes de validação ao começar a digitar
            input.addEventListener('input', function() {
                this.classList.remove('is-valid', 'is-invalid');
            });
        });
    }
}

// ============================================
// LAZY LOADING DE IMAGENS
// ============================================
function initLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');

    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    } else {
        // Fallback para navegadores antigos
        images.forEach(img => {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        });
    }
}

// ============================================
// TOOLTIPS BOOTSTRAP
// ============================================
function initTooltips() {
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        [...tooltipTriggerList].map(tooltipTriggerEl =>
            new bootstrap.Tooltip(tooltipTriggerEl)
        );
    }
}

// ============================================
// ANIMATED COUNTER
// ============================================
function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);

    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            element.textContent = target + '+';
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(start) + '+';
        }
    }, 16);
}

// Ativar contadores quando entrarem na viewport
const counters = document.querySelectorAll('.hero-stats h3');
if (counters.length > 0 && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.textContent);
                animateCounter(entry.target, target);
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => counterObserver.observe(counter));
}

// ============================================
// SEARCH FUNCTIONALITY
// ============================================
function initProjectSearch() {
    const searchInput = document.querySelector('input[name="busca"]');

    if (!searchInput) return;

    // Adicionar ícone de loading
    const form = searchInput.closest('form');
    if (form) {
        form.addEventListener('submit', function() {
            const button = form.querySelector('button[type="submit"]');
            if (button) {
                button.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Buscando...';
                button.disabled = true;
            }
        });
    }
}

// ============================================
// COPY TO CLIPBOARD
// ============================================
function copyToClipboard(text, successMessage = 'Copiado!') {
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(successMessage, 'success');
        });
    } else {
        // Fallback para navegadores antigos
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        document.body.appendChild(textArea);
        textArea.select();

        try {
            document.execCommand('copy');
            showToast(successMessage, 'success');
        } catch (err) {
            showToast('Erro ao copiar', 'error');
        }

        document.body.removeChild(textArea);
    }
}

// ============================================
// TOAST NOTIFICATION
// ============================================
function showToast(message, type = 'info') {
    // Criar elemento de toast
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} position-fixed top-0 end-0 m-3`;
    toast.style.zIndex = '9999';
    toast.style.minWidth = '250px';
    toast.innerHTML = `
        <div class="d-flex align-items-center">
            <i class="bi bi-${type === 'success' ? 'check-circle' : 'info-circle'} me-2"></i>
            <span>${message}</span>
        </div>
    `;

    document.body.appendChild(toast);

    // Remover após 3 segundos
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.5s';
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}

// ============================================
// DARK MODE TOGGLE (Opcional)
// ============================================
function initDarkMode() {
    const darkModeToggle = document.getElementById('darkModeToggle');

    if (!darkModeToggle) return;

    // Verificar preferência salva
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        document.body.classList.add('dark-mode');
        darkModeToggle.checked = true;
    }

    // Toggle dark mode
    darkModeToggle.addEventListener('change', function() {
        if (this.checked) {
            document.body.classList.add('dark-mode');
            localStorage.setItem('theme', 'dark');
        } else {
            document.body.classList.remove('dark-mode');
            localStorage.setItem('theme', 'light');
        }
    });
}

// ============================================
// ANALYTICS (Opcional - Google Analytics)
// ============================================
function trackEvent(category, action, label) {
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            'event_category': category,
            'event_label': label
        });
    }
}

// Track cliques em projetos
document.querySelectorAll('.project-card a').forEach(link => {
    link.addEventListener('click', function() {
        const projectTitle = this.closest('.project-card').querySelector('.project-title')?.textContent;
        trackEvent('Project', 'Click', projectTitle);
    });
});

// Track envio de formulário de contato
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function() {
        trackEvent('Contact', 'Submit', 'Contact Form');
    });
}

// ============================================
// PERFORMANCE OPTIMIZATION
// ============================================
// Debounce function para otimizar eventos de scroll/resize
function debounce(func, wait = 10) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Aplicar debounce em eventos de scroll
window.addEventListener('scroll', debounce(() => {
    // Código de scroll otimizado aqui
}, 10));

// ============================================
// CONSOLE MESSAGE
// ============================================
console.log('%c👋 Olá, Developer!', 'font-size: 20px; font-weight: bold; color: #007bff;');
console.log('%cGostou do código? Vamos trabalhar juntos!', 'font-size: 14px; color: #6c757d;');
console.log('%cContato: natalia@exemplo.com', 'font-size: 12px; color: #6c757d;');

// ============================================
// EXPORT FUNCTIONS (para uso em outros scripts)
// ============================================
window.portfolioUtils = {
    copyToClipboard,
    showToast,
    trackEvent,
    debounce
};
