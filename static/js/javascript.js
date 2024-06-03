document.addEventListener('DOMContentLoaded', () => {
    const steps = Array.from(document.querySelectorAll('.form-step'));
    const nextBtns = document.querySelectorAll('.btn-next, .btn-next1');
    const prevBtns = document.querySelectorAll('.btn-prev');
    const dots = document.querySelectorAll('.dot');
    const passwordField = document.getElementById('password');
    const togglePassword = document.getElementById('togglePassword');
    let currentStep = 0;

    nextBtns.forEach(button => {
        button.addEventListener('click', () => {
            steps[currentStep].classList.remove('form-step-active');
            dots[currentStep].classList.remove('active');
            currentStep++;
            steps[currentStep].classList.add('form-step-active');
            dots[currentStep].classList.add('active');
        });
    });

    prevBtns.forEach(button => {
        button.addEventListener('click', () => {
            steps[currentStep].classList.remove('form-step-active');
            dots[currentStep].classList.remove('active');
            currentStep--;
            steps[currentStep].classList.add('form-step-active');
            dots[currentStep].classList.add('active');
        });
    });
    togglePassword.addEventListener('change', () => {
        if (togglePassword.checked) {
            passwordField.type = 'text';
        } else {
            passwordField.type = 'password';
        }
    });
    document.getElementById('signupForm').addEventListener('submit', (e) => {
        e.preventDefault();
        alert('Formulaire soumis avec succès!');

    });

    function handleSubmit(event) {
        event.preventDefault();
        window.location.href = 'réussite.html';
    }
});