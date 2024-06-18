document.addEventListener('DOMContentLoaded', function() {
    const profileContainer = document.getElementById('profile-container');
    const profiles = document.querySelectorAll('.profile-card');
    let currentIndex = 0;

    function showProfile(index) {
        profiles.forEach((profile, i) => {
            profile.style.display = i === index ? 'block' : 'none';
        });
    }

    function nextProfile() {
        if (currentIndex < profiles.length - 1) {
            currentIndex++;
            showProfile(currentIndex);
        }
    }

    document.querySelectorAll('.reject-button').forEach(button => {
        button.addEventListener('click', nextProfile);
    });

    document.querySelectorAll('.like-button').forEach(button => {
        button.addEventListener('click', nextProfile);
    });

    document.querySelectorAll('.superlike-button').forEach(button => {
        button.addEventListener('click', nextProfile);
    });

    showProfile(currentIndex);
});

// Apparition User
const userToggle = document.querySelector('.profile-img');
const dropdown = document.querySelector('.menu');

userToggle.addEventListener('click', () => {
    if (dropdown.classList.contains('active')) {
        dropdown.classList.remove('active');
        document.removeEventListener('click', handleClickOutside);
    } else {
        dropdown.classList.add('active');
        document.addEventListener('click', handleClickOutside);
    }
});

function handleClickOutside(event) {
    if (!event.target.closest('.profile-dropdown')) {
        dropdown.classList.remove('active');
        document.removeEventListener('click', handleClickOutside);
    }
}