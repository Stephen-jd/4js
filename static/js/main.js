/**
 * 4JS Educational Academy - Main Interactions
 */

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initHeroSlider();
    initScrollAnimations();
    initAppleAnimations();
    initCounters();
    initCoursesAccordion();
    initReviewModal();
    initCookieBanner();
});

function initCookieBanner() {
    const banner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-cookies');
    const declineBtn = document.getElementById('decline-cookies');

    if (!banner) return;

    // Check if the user has already made a choice
    const cookieConsent = localStorage.getItem('4js_cookie_consent');

    if (!cookieConsent) {
        // Show banner if no choice was made yet
        setTimeout(() => {
            banner.classList.remove('hidden');
        }, 1500); // Slight delay so it doesn't interrupt page load instantly
    }

    const hideBanner = (choice) => {
        localStorage.setItem('4js_cookie_consent', choice);
        banner.classList.add('hidden');
    };

    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => hideBanner('accepted'));
    }

    if (declineBtn) {
        declineBtn.addEventListener('click', () => hideBanner('declined'));
    }
}

function initAppleAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: stop observing once animated
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-up, .scale-in, .stagger');
    animatedElements.forEach(el => observer.observe(el));
}

function initNavbar() {
    const navbar = document.querySelector('.navbar');
    const mobileToggle = document.querySelector('.navbar-toggle');
    const mobileMenu = document.querySelector('.mobile-menu');
    let lastScrollY = window.scrollY;

    // Scroll behavior
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Hide on scroll down, show on scroll up (if scrolled past hero)
        if (window.scrollY > 300) {
            if (window.scrollY > lastScrollY) {
                navbar.classList.add('hidden');
            } else {
                navbar.classList.remove('hidden');
            }
        }
        lastScrollY = window.scrollY;
    }, { passive: true });

    // Mobile menu toggle
    if (mobileToggle && mobileMenu) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            mobileMenu.classList.toggle('active');
            document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu when clicking a link
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }
}

function initHeroSlider() {
    const slider = document.querySelector('.hero-slider');
    const slides = document.querySelectorAll('.hero-slide');
    const dots = document.querySelectorAll('.hero-dot');
    if (!slider || !slides.length) return;

    let currentSlide = 0;
    const slideDuration = 5000;
    let slideInterval;

    function goToSlide(index) {
        if (dots[currentSlide]) dots[currentSlide].classList.remove('active');
        currentSlide = index;
        slider.style.transform = `translateX(-${currentSlide * 100}%)`;
        if (dots[currentSlide]) dots[currentSlide].classList.add('active');
    }

    function nextSlide() {
        let next = (currentSlide + 1) % slides.length;
        goToSlide(next);
    }

    // Auto play
    slideInterval = setInterval(nextSlide, slideDuration);

    // Dot clicks
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            clearInterval(slideInterval);
            goToSlide(index);
            slideInterval = setInterval(nextSlide, slideDuration);
        });
    });
}

function initScrollAnimations() {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Optional: stop observing once revealed
                // observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .stagger');
    revealElements.forEach(el => observer.observe(el));
}

function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    const speed = 200;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = +counter.getAttribute('data-count');
                const suffix = counter.getAttribute('data-suffix') || '';
                
                const updateCount = () => {
                    const current = +counter.innerText.replace(/[^0-9]/g, '');
                    const inc = target / speed;

                    if (current < target) {
                        counter.innerText = Math.ceil(current + inc) + suffix;
                        setTimeout(updateCount, 20);
                    } else {
                        counter.innerText = target + suffix;
                    }
                };
                
                updateCount();
                observer.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counter.innerText = '0' + (counter.getAttribute('data-suffix') || '');
        observer.observe(counter);
    });
}

function initCoursesAccordion() {
    const cards = document.querySelectorAll('.course-card');
    
    cards.forEach(card => {
        card.addEventListener('click', () => {
            // Close others
            cards.forEach(c => {
                if (c !== card) c.classList.remove('expanded');
            });
            // Toggle current
            card.classList.toggle('expanded');
        });
    });
}

function initReviewModal() {
    const reviewCards = document.querySelectorAll('.review-card');
    const overlay = document.getElementById('review-modal-overlay');
    const modalContent = document.getElementById('review-modal-content');
    const closeBtn = document.querySelector('.review-modal-close');

    if (!overlay) return;

    reviewCards.forEach(card => {
        card.addEventListener('click', () => {
            const html = card.innerHTML;
            if (modalContent) {
                modalContent.innerHTML = html;
                overlay.classList.add('active');
                document.body.style.overflow = 'hidden';
            }
        });
    });

    const close = () => {
        overlay.classList.remove('active');
        document.body.style.overflow = '';
    };

    if (closeBtn) closeBtn.addEventListener('click', close);
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) close();
    });
}
