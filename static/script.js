document.addEventListener('DOMContentLoaded', () => {
    // --- PAGE LOAD ANIMATIONS ---
    document.body.classList.remove('loading');
    setTimeout(() => {
        const revealItems = document.querySelectorAll('.reveal-item');
        revealItems.forEach(item => item.classList.add('active'));
    }, 100);

    // --- MOBILE MENU TOGGLE ---
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.getElementById('nav-links');
    const navItems = document.querySelectorAll('.nav-link');

    if (mobileMenu) {
        mobileMenu.addEventListener('click', () => {
            navLinks.classList.toggle('active');
        });

        navItems.forEach(item => {
            item.addEventListener('click', () => {
                navLinks.classList.remove('active');
            });
        });
    }

    // --- NAVBAR SCROLL EFFECT ---
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // --- INTERSECTION OBSERVER FOR SCROLL REVEAL ---
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    const elementsToAnimate = document.querySelectorAll('.reveal-on-scroll');
    elementsToAnimate.forEach(el => observer.observe(el));

    // --- FORM HANDLING & BACKEND INTEGRATION ---
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        const formFeedback = document.getElementById('form-feedback');
        const submitBtn = contactForm.querySelector('.submit-btn');
        const btnText = submitBtn.querySelector('.btn-text');

        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = {
                name: document.getElementById('name').value,
                email: document.getElementById('email').value,
                message: document.getElementById('message').value
            };

            // UI Loading state
            submitBtn.disabled = true;
            btnText.textContent = 'Transmitting...';
            formFeedback.textContent = 'Initializing Data Transfer...';
            formFeedback.className = 'feedback-msg msg-loading';

            try {
                // Send to Flask backend
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });

                const result = await response.json();

                if (response.ok) {
                    formFeedback.textContent = 'Transmission Successful ✅';
                    formFeedback.className = 'feedback-msg msg-success';
                    contactForm.reset();
                } else {
                    formFeedback.textContent = result.message || 'Transmission Failed ❌';
                    formFeedback.className = 'feedback-msg msg-error';
                }
            } catch (error) {
                console.error('Error during transmission:', error);
                formFeedback.textContent = 'Network Error. Connection Lost ❌';
                formFeedback.className = 'feedback-msg msg-error';
            } finally {
                submitBtn.disabled = false;
                btnText.textContent = 'Initiate Transfer';
                
                // Clear message after 6 seconds
                setTimeout(() => {
                    if (formFeedback.className.includes('msg-success') || formFeedback.className.includes('msg-error')) {
                        formFeedback.textContent = '';
                        formFeedback.className = 'feedback-msg';
                    }
                }, 6000);
            }
        });
    }

    // --- CANVAS PARTICLE SYSTEM ---
    initParticles();
});

function initParticles() {
    const canvas = document.getElementById('particle-canvas');
    if(!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let width, height;
    let particles = [];
    
    function resize() {
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width;
        canvas.height = height;
    }
    
    window.addEventListener('resize', resize);
    resize();
    
    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            // Slow, floaty movement
            this.vx = (Math.random() - 0.5) * 0.4;
            this.vy = (Math.random() - 0.5) * 0.4;
            this.size = Math.random() * 1.5 + 0.5;
            this.alpha = Math.random() * 0.5 + 0.1;
        }
        
        update() {
            this.x += this.vx;
            this.y += this.vy;
            
            // Wrap around edges
            if (this.x < 0) this.x = width;
            if (this.x > width) this.x = 0;
            if (this.y < 0) this.y = height;
            if (this.y > height) this.y = 0;
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 240, 255, ${this.alpha})`;
            ctx.fill();
        }
    }
    
    // Create particles based on screen width
    const particleCount = Math.min(window.innerWidth / 20, 100);
    for (let i = 0; i < particleCount; i++) {
        particles.push(new Particle());
    }
    
    function animate() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
            p.update();
            p.draw();
        });
        requestAnimationFrame(animate);
    }
    
    animate();
}
