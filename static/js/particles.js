/**
 * 4JS Educational Academy - Opening Particle Animation ("Knowledge Wave")
 */

class ParticleWave {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.numParticles = window.innerWidth < 768 ? 100 : 250;
        this.animationId = null;
        this.isActive = true;

        this.colors = ['#86C5D8', '#B8E0CC', '#5FAFC6', '#A8C5A0'];
        this.symbols = ['π', '∑', '√', '∞', 'A', 'B', '+', '-', '×', '÷'];

        this.init();
    }

    init() {
        this.resize();
        window.addEventListener('resize', () => this.resize());

        // Respect reduced motion
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReducedMotion) {
            this.finish();
            return;
        }

        // Check session storage if already played
        if (sessionStorage.getItem('4js_intro_played') === 'true') {
            this.finish();
            return;
        }

        for (let i = 0; i < this.numParticles; i++) {
            this.particles.push(this.createParticle());
        }

        this.animate();

        // Reveal logo
        setTimeout(() => {
            const logo = document.querySelector('.particles-logo');
            if (logo) {
                logo.classList.add('visible');
            }
        }, 500);

        // Sequence: dissolve wave and hide overlay
        setTimeout(() => this.dissolve(), 2500);
        setTimeout(() => this.finish(), 3000);
    }

    createParticle() {
        const isSymbol = Math.random() > 0.8;
        return {
            x: Math.random() * this.canvas.width,
            y: Math.random() * this.canvas.height,
            size: Math.random() * 3 + 1,
            color: this.colors[Math.floor(Math.random() * this.colors.length)],
            speedX: (Math.random() - 0.5) * 1.5,
            speedY: (Math.random() - 0.5) * 1.5,
            angle: Math.random() * Math.PI * 2,
            symbol: isSymbol ? this.symbols[Math.floor(Math.random() * this.symbols.length)] : null,
            baseY: Math.random() * this.canvas.height,
            amplitude: Math.random() * 50 + 20,
            phase: Math.random() * Math.PI * 2,
            dissolving: false
        };
    }

    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }

    animate() {
        if (!this.isActive) return;

        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

        const time = Date.now() * 0.001;

        for (let i = 0; i < this.particles.length; i++) {
            const p = this.particles[i];

            if (!p.dissolving) {
                // Wave motion
                p.x += p.speedX;
                p.y = p.baseY + Math.sin(time * 2 + p.phase) * p.amplitude;

                if (p.x > this.canvas.width) p.x = 0;
                if (p.x < 0) p.x = this.canvas.width;
            } else {
                // Explode outward
                p.x += p.speedX * 5;
                p.y += p.speedY * 5;
                p.size *= 0.9;
            }

            this.ctx.fillStyle = p.color;
            this.ctx.globalAlpha = p.dissolving ? p.size / 4 : 0.6;

            if (p.symbol) {
                this.ctx.font = `${p.size * 5}px Space Grotesk`;
                this.ctx.fillText(p.symbol, p.x, p.y);
            } else {
                this.ctx.beginPath();
                this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                this.ctx.fill();
            }
        }

        this.ctx.globalAlpha = 1;
        this.animationId = requestAnimationFrame(() => this.animate());
    }

    dissolve() {
        for (let p of this.particles) {
            p.dissolving = true;
            // Add explosive velocity away from center
            const dx = p.x - this.canvas.width / 2;
            const dy = p.y - this.canvas.height / 2;
            const dist = Math.sqrt(dx * dx + dy * dy);
            p.speedX = (dx / dist) * (Math.random() * 10 + 5);
            p.speedY = (dy / dist) * (Math.random() * 10 + 5);
        }
    }

    finish() {
        this.isActive = false;
        if (this.animationId) cancelAnimationFrame(this.animationId);
        
        const overlay = document.getElementById('particles-overlay');
        if (overlay) {
            overlay.classList.add('fade-out');
            setTimeout(() => {
                overlay.style.display = 'none';
            }, 800);
        }
        
        sessionStorage.setItem('4js_intro_played', 'true');
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('particles-canvas')) {
        new ParticleWave('particles-canvas');
    }
});
