/**
 * 4JS Educational Academy - Custom Study Plan Builder (formerly Taylor-Fit)
 */

document.addEventListener('DOMContentLoaded', () => {
    const steps = document.querySelectorAll('.taylorfit-step');
    const dots = document.querySelectorAll('.taylorfit-step-dot');
    const nextBtns = document.querySelectorAll('.btn-next');
    const backBtns = document.querySelectorAll('.btn-back');
    const submitBtn = document.getElementById('tf-submit');
    const resultDiv = document.querySelector('.taylorfit-result');
    const form = document.getElementById('taylorfit-form');
    
    let currentStep = 0;

    if (!form) return;

    function showStep(index) {
        steps.forEach((s, i) => {
            s.classList.toggle('active', i === index);
            if (dots[i]) {
                dots[i].classList.toggle('active', i === index);
                dots[i].classList.toggle('completed', i < index);
            }
        });
    }

    nextBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Basic validation
            const currentInputs = steps[currentStep].querySelectorAll('input[required], select[required]');
            let valid = true;
            currentInputs.forEach(input => {
                if (!input.value) valid = false;
            });

            if (valid) {
                currentStep++;
                showStep(currentStep);
            } else {
                alert('Please fill out required fields.');
            }
        });
    });

    backBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            currentStep--;
            showStep(currentStep);
        });
    });

    // Checkbox toggles
    const checkboxItems = document.querySelectorAll('.checkbox-item');
    checkboxItems.forEach(item => {
        item.addEventListener('click', () => {
            item.classList.toggle('selected');
            const input = item.querySelector('input');
            input.checked = !input.checked;
        });
    });

    submitBtn.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Collect data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        data.exams = Array.from(formData.getAll('exams'));

        // Generate roadmap visual
        generateRoadmap(data);

        // Hide form, show result
        form.style.display = 'none';
        document.querySelector('.taylorfit-progress').style.display = 'none';
        resultDiv.classList.add('active');

        // Optional: Send to Django backend
        fetch('/api/taylorfit/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Function to get CSRF
            }
        }).catch(err => console.error('Form submission failed silently in frontend view.'));
    });

    function generateRoadmap(data) {
        // Customize text based on input
        const name = data.name || 'Student';
        const target = data.target_grade || 'Top Grades';
        
        document.getElementById('tf-result-name').textContent = `${name}'s Custom Plan`;
        document.getElementById('tf-result-goal').textContent = `Target: ${target}`;
        
        // Update WhatsApp link with prepopulated message
        const waLink = document.getElementById('tf-whatsapp-link');
        const text = `Hi! I just completed the Custom Study Plan Builder for ${name} (Year: ${data.year}). We're interested in tutoring for ${data.exams.join(', ')}. Target: ${target}.`;
        waLink.href = `https://wa.me/447534715058?text=${encodeURIComponent(text)}`;
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
