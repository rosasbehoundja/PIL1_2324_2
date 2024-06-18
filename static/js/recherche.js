    /*APPARITION USER */
  
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
    menu.classList.remove('active');
    document.removeEventListener('click', handleClickOutside);
    }
    }

    /*APPARITION DE L'ONGLET FILTRAGE*/

    const filterButton = document.querySelector('.filter-button');
    const overlayContainer = document.querySelector('.overlay-container');

    filterButton.addEventListener('click', () => {
    overlayContainer.classList.add('visible');
    overlayContainer.classList.remove('hidden');
    });

    overlayContainer.addEventListener('click', (event) => {
    if (event.target === overlayContainer) {
        overlayContainer.classList.add('hidden');
        overlayContainer.classList.remove('visible');
    }
    });

    const ageInput = document.getElementById('age-range'); //FAIRE DEFILER L'AGE
    const ageValue = document.getElementById('age-value');
    ageInput.addEventListener('input', function() {
    ageValue.textContent = ageInput.value + ' ans';
    });