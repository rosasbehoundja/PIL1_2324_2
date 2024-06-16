document.addEventListener('DOMContentLoaded', function() {
    const nextButton1 = document.querySelector('.nextButton1');
    const nextButton2 = document.querySelector('.nextButton2');
    const section1 = document.getElementById('section1');
    const section2 = document.getElementById('section2');
    const coverImage = document.getElementById('coverImage');
    let currentStep = 0;

    const contents = [{
            section1: `
        <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Quel physique préférez vous?</h3>

                <div class="option">
                    <label for="Ronde">Athlétique</label>
                    <input type="radio" id="physique" name="physique" value="Athlétique">
                </div>
                <div class="option">
                    <label for="mince">Mince</label>
                    <input type="radio" id="physique" name="physique" value="Minces">
                </div>
                <div class="option">
                    <label for="mince">Moyen</label>
                    <input type="radio" id="physique" name="physique" value="Moyen">
                </div>
                

                <div class="option">
                <label for="En surpoids">En surpoids</label>
                <input type="radio" id="physique" name="physique" value="En surpoids">
            </div>

                <button class="nextButton1">Suivant</button>
            </div>


        </div>

            `,
            section2: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Quel est la tranche d'âge qui vous convient?</h3>

                <div class="option">
                    <label for="age">19-30</label>
                    <input type="radio" id="age" name="age" value="19-30">
                </div>
                <div class="option">
                    <label for="age">30-40</label>
                    <input type="radio" id="age" name="age" value="30-40">
                </div>
                <div class="option">
                    <label for="age">40 et plus</label>                                                                                                                                    
                    <input type="radio" id="age" name="age" value="40 et plus">
                </div>

                <button class="Submit">Soumettre</button>
            </div>


        </div>
            `
        },
        {
            section1: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Voulez-vous que votre partenaire soit?</h3>

                <div class="option">
                    <label for="Chrétien">Chrétien</label>
                    <input type="radio" id="religion" name="religion" value="Chrétien">
                </div>
                <div class="option">
                    <label for="Musulman">Musulman</label>
                    <input type="radio" id="religion" name="religion" value="Musulman">
                </div>
                
               <div class="option">
                    <label for="Aucune">Aucune préférences</label>
                    <input type="radio" id="religion" name="religion" value="Aucune">
                </div>
              <div class="option">
                 <label for="Autre">Autre</label>
                 <input type="radio" id="religion" name="religion" value="Autre">
               </div>

                <button class="nextButton1">Suivant</button>
            </div>


        </div>
            `,
            section2: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Quel niveau d'étude  souhaitez vous que votre partenaire ait?</h3>

                <div class="option">
                    <label for="Ecole secondaire">Ecole secondaire</label>
                    <input type="radio" id="education" name="education" value="Ecole secondaire">
                </div>
                <div class="option">
                    <label for="Licence">Licence</label>
                    <input type="radio" id="education" name="education" value="Licence">
                </div>
               
              
                <div class="option">
                   <label for="Master">Master</label>
                    <input type="radio" id="education" name="education" value="Master">
                </div>
                <div class="option">
                  <label for="Doctorat">Doctorat</label>
                   <input type="radio" id="education" name="education" value="Doctorat">
                </div>
                
                <button class="nextButton2">Suivant</button>
            </div>


        </div>
            `
        }, {
            section1: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>De quel pays voulez-vous qu'il/elle soit?</h3>

                <div class="option">
                    <label for="Cote d'ivoire">Cote d'ivoire</label>
                    <input type="radio" id="origin" name="origin" value="Cote d'ivoire">
                </div>
                <div class="option">
                    <label for="Sénégal">Sénégal</label>
                    <input type="radio" id="origin" name="origin" value="Sénégal">
                </div>
                

                <div class="option">
                    <label for="Mali">Mali</label>
                    <input type="radio" id="origin" name="origin" value="Mali">
                </div>
                
                <div class="option">
                    <label for="Togo">Togo</label>
                    <input type="radio" id="origin" name="origin" value="Togo">
                </div>
                <div class="option">
                    <label for="Burkina-faso">Burkina Faso</label>
                    <input type="radio" id="origin" name="origin" value="Burkina-faso">
                </div>
                

                <div class="option">
                    <label for="Bénin">Bénin</label>
                    <input type="radio" id="origin" name="origin" value="Bénin">
                </div>
                
                <div class="option">
                    <label for="Ghana">Ghana</label>
                    <input type="radio" id="origin" name="origin" value="Ghana">
                </div>
                <button class="nextButton1">Suivant</button>
            </div>


        </div>
            `,
            section2: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Quel style de vie doit avoir votre partenaire ?</h3>

                <div class="option">
                    <label for="Actif">Actif</label>
                    <input type="radio" id="lifestyle"name="lifestyle" value="Actif">
                </div>
                
               <div class="option">
                    <label for="sédentaire">sédentaire</label>
                    <input type="radio" id="Diet" name="Diet" value="Je suis végétarien">
                </div>
             
                <button class="nextButton2">Suivant</button>
            </div>


        </div>
            `
        },

        // Ajoutez d'autres objets de contenu ici
    ];

    function attachEvents() {
        document.querySelector('.nextButton1').addEventListener('click', function() {
            // Déplacer l'image pour cacher la première section en glissant vers la gauche
            coverImage.style.transform = 'translateX(0)';

            // Attendre un instant puis afficher la deuxième section
            setTimeout(function() {
                // Masquer la première section
                section1.classList.remove('active');
                section1.classList.add('hidden');

                // Réinitialiser la position de l'image
                coverImage.style.transform = 'translateX(0)';
                coverImage.style.left = 'auto';
                coverImage.style.left = '0';

                // Afficher la deuxième section
                section2.classList.remove('hidden');
                section2.classList.add('active');
            }, 1000); // Délai de 1 seconde
        });

        document.querySelector('.nextButton2').addEventListener('click', function() {
            // Déplacer l'image pour cacher la deuxième section en glissant vers la droite
            coverImage.style.transform = 'translateX(0)';

            // Attendre un instant puis afficher la première section
            setTimeout(function() {
                // Masquer la deuxième section
                section2.classList.remove('active');
                section2.classList.add('hidden');

                // Réinitialiser la position de l'image
                coverImage.style.transform = 'translateX(0)';
                coverImage.style.left = 'auto';
                coverImage.style.right = '0';

                // Afficher la première section
                section1.classList.remove('hidden');
                section1.classList.add('active');
            }, 1000); // Délai de 1 seconde

            // Changer le contenu après la transition
            setTimeout(function() {
                currentStep = (currentStep + 1) % contents.length;
                section1.innerHTML = contents[currentStep].section1;
                section2.innerHTML = contents[currentStep].section2;

                // Réattacher les événements aux nouveaux boutons
                attachEvents();
            }, 1200); // Délai de 1.2 secondes pour changer le contenu après la transition
        });
    }

    // Attacher les événements initiaux
    attachEvents();
});
document.getElementById('dropdownButton').addEventListener('click', function() {
    document.getElementById('dropdownContent').classList.toggle('show');
});

document.querySelectorAll('.dropdown-item').forEach(function(item) {
    item.addEventListener('click', function() {
        document.getElementById('location').value = this.textContent;
        document.getElementById('dropdownContent').classList.remove('show');
    });
});

window.onclick = function(event) {
    if (!event.target.matches('#dropdownButton')) {
        var dropdowns = document.getElementsByClassName('dropdown-content');
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
    document.getElementById('multiSelectButton').addEventListener('click', function() {
        document.getElementById('multiSelectDropdown').classList.toggle('show');
    });

    document.querySelectorAll('.multi-select-item').forEach(function(item) {
        item.addEventListener('click', function() {
            var input = document.getElementById('multiSelectInput');
            var currentValue = input.value.trim();
            var newValue = this.textContent;

            if (currentValue) {
                input.value = currentValue + ', ' + newValue;
            } else {
                input.value = newValue;
            }

            document.getElementById('multiSelectDropdown').classList.remove('show');
        });
    });

    window.onclick = function(event) {
        if (!event.target.matches('#multiSelectButton')) {
            var dropdowns = document.getElementsByClassName('multi-select-dropdown');
            for (var i = 0; i < dropdowns.length; i++) {
                var openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    }
}