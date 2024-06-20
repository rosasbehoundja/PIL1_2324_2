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
