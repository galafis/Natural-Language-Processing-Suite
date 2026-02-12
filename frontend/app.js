/**
 * Modern JavaScript Application
 * Author: Gabriel Demetrios Lafis
 * ES6+ features and modern web APIs
 */

class ApplicationManager {
    constructor() {
        this.initialized = false;
        this.data = new Map();
        this.init();
    }

    async init() {
        console.log('Initializing application...');
        
        // Modern async initialization
        await this.loadResources();
        this.setupEventListeners();
        this.startPerformanceMonitoring();
        
        this.initialized = true;
        console.log('Application initialized successfully');
    }

    async loadResources() {
        // Simulate async resource loading
        return new Promise(resolve => {
            setTimeout(() => {
                this.data.set('loadTime', Date.now());
                resolve();
            }, 100);
        });
    }

    setupEventListeners() {
        // Run UI setup immediately if DOM is ready, otherwise wait for it
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                this.enhanceUI();
                this.setupNlpProcessor();
            });
        } else {
            this.enhanceUI();
            this.setupNlpProcessor();
        }

        // Intersection Observer for animations
        if ('IntersectionObserver' in window) {
            this.setupScrollAnimations();
        }
    }

    enhanceUI() {
        // Add interactive features
        const techCards = document.querySelectorAll('.tech-card');
        techCards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.1}s`;
            card.classList.add('fade-in');
            
            card.addEventListener('click', () => {
                this.showTechDetails(card.querySelector('h3').textContent);
            });
        });

        // Add loading states
        const features = document.querySelectorAll('.feature');
        features.forEach(feature => {
            feature.addEventListener('mouseenter', () => {
                feature.style.transform = 'scale(1.02)';
                feature.style.transition = 'transform 0.3s ease';
            });
            
            feature.addEventListener('mouseleave', () => {
                feature.style.transform = 'scale(1)';
            });
        });
    }

    setupNlpProcessor() {
        const processButton = document.getElementById('process-button');
        const nlpInput = document.getElementById('nlp-input');
        const nlpOutput = document.getElementById('nlp-output');

        if (processButton && nlpInput && nlpOutput) {
            processButton.addEventListener('click', async () => {
                const text = nlpInput.value;
                if (text.trim() === '') {
                    nlpOutput.textContent = 'Please enter some text to process.';
                    return;
                }

                nlpOutput.textContent = 'Processing...';
                try {
                    const response = await fetch('/api/process', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ text: text })
                    });
                    const data = await response.json();
                    nlpOutput.textContent = `Original: ${data.original_text}\nProcessed: ${data.processed_text}`;
                } catch (error) {
                    console.error('Error processing text:', error);
                    nlpOutput.textContent = 'Error processing text. Please try again.';
                }
            });
        }
    }

    setupScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.feature, .tech-card').forEach(el => {
            observer.observe(el);
        });
    }

    showTechDetails(tech) {
        const details = {
            'Python': 'Backend processing with Flask. Data handling with pandas and numpy.',
            'JavaScript': 'ES6+ features, async/await, Web APIs, DOM manipulation.',
            'R': 'Statistical analysis with ggplot2, dplyr, corrplot.',
            'HTML5/CSS3': 'Semantic markup, responsive design, CSS Grid, Flexbox, animations.'
        };

        if (details[tech]) {
            this.showNotification(`${tech}: ${details[tech]}`);
        }
    }

    showNotification(message) {
        // Create modern notification
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 1rem 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            z-index: 1000;
            animation: slideIn 0.3s ease;
            max-width: 400px;
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    startPerformanceMonitoring() {
        // Log basic performance metrics
        if ('performance' in window) {
            const perfData = {
                loadTime: performance.now(),
                memory: navigator.deviceMemory || 'unknown',
                connection: navigator.connection?.effectiveType || 'unknown'
            };
            
            console.log('Performance metrics:', perfData);
        }
    }

    // Public API methods
    getData(key) {
        return this.data.get(key);
    }

    setData(key, value) {
        this.data.set(key, value);
        return this;
    }

    async processData(data) {
        // Simulate data processing
        return new Promise(resolve => {
            setTimeout(() => {
                const processed = Array.isArray(data) 
                    ? data.map(item => ({ ...item, processed: true }))
                    : { ...data, processed: true };
                resolve(processed);
            }, 100);
        });
    }
}

// CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
    
    .fade-in {
        animation: fadeIn 0.6s ease forwards;
    }
    
    .animate-in {
        animation: fadeIn 0.8s ease forwards;
    }
`;
document.head.appendChild(style);

// Initialize application
const app = new ApplicationManager();
