// script.js
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('nav button');
    const containers = document.querySelectorAll('.container');
    let currentAngle = 0; // Pour suivre l'angle de rotation actuel
    let currentVisibleIndex = 0; // Pour suivre l'index du conteneur actuellement visible

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const targetId = button.getAttribute('data-target');
            const targetContainer = document.getElementById(targetId);

            // Trouver l'index du conteneur cible
            const targetIndex = Array.from(containers).indexOf(targetContainer);
            // Calculer la différence d'angle
            const angleDifference = (targetIndex - currentVisibleIndex) * 90;
            // Mettre à jour l'angle actuel
            currentAngle -= angleDifference;
            // Appliquer la rotation
            document.querySelector('.main-container').style.transform = `rotateY(${currentAngle}deg)`;

            // Attendre que l'animation de rotation soit terminée avant de rendre le conteneur visible
            setTimeout(() => {
                containers.forEach(container => {
                    container.classList.remove('visible');
                });
                targetContainer.classList.add('visible');
                // Mettre à jour l'index visible actuel
                currentVisibleIndex = targetIndex;
            }, 500); // Correspond à la durée de la transition CSS
        });
    });

    // Initialisation : rendre le premier conteneur visible
    containers[currentVisibleIndex].classList.add('visible');
});

document.addEventListener('DOMContentLoaded', (event) => {
    const mySearch = document.getElementById('my-search');
    const mainContent = document.getElementById('main-content');

    mySearch.addEventListener('click', () => {
        if (mainContent.style.display === 'none' || mainContent.style.display === '') {
            mainContent.style.display = 'block';
        } else {
            mainContent.style.display = 'none';
        }
    });
});
const profiles = [{
        img: 'profile3.jpg',
        name: 'profil1, 22 ans'
    },
    {
        img: 'profile1.avif',
        name: 'Profil2, 25 ans'
    },
    {
        img: 'profile2.jpeg',
        name: 'Profil3, 30 ans'
    }
];

let currentIndex = 0;

const profileImg = document.getElementById('profile-img');
const profileName = document.getElementById('profile-name');
const dislikeBtn = document.getElementById('dislike-btn');
const likeBtn = document.getElementById('like-btn');

function updateProfile() {
    profileImg.src = profiles[currentIndex].img;
    profileName.textContent = profiles[currentIndex].name;
}

function showNextProfile() {
    currentIndex = (currentIndex + 1) % profiles.length;
    updateProfile();
}

function sendMessageToProfile() {
    console.log(`
    Message sent to $ {profiles[currentIndex].name}`);
    // Ajoutez ici le code pour envoyer un message au profil, par exemple via une API
}

dislikeBtn.addEventListener('click', showNextProfile);

likeBtn.addEventListener('click', () => {
    sendMessageToProfile();
    showNextProfile();
});

// Initialiser le premier profil
updateProfile();