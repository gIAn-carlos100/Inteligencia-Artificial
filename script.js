// Intersection Observer for scroll animations
document.addEventListener("DOMContentLoaded", () => {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Initial trigger for hero section so it animates immediately on load
    setTimeout(() => {
        const heroElements = document.querySelectorAll('.fade-in');
        heroElements.forEach(el => el.classList.add('visible'));
    }, 100);

    // Observe other elements
    document.querySelectorAll('.slide-up').forEach(el => {
        observer.observe(el);
    });
});
