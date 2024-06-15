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
                <h3>Quel est type de corps vous attire plus?</h3>

                <div class="option">
                    <label for="Ronde">Ronde</label>
                    <input type="radio" id="body_type" name="body_type" value="Ronde">
                </div>
                <div class="option">
                    <label for="mince">mince</label>
                    <input type="radio" id="body_type" name="body_type" value="femme">
                </div>
                

                <div class="option">
                <label for=""></label>
                <input type="radio" id="body_type" name="body_type" value="">
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
                <h3>Quel est type de corps vous attire plus?</h3>

                <div class="option">
                    <label for="Ronde">Arrondie</label>
                    <input type="radio" id="body_type" name="body_type" value="Arrondie">
                </div>
                <div class="option">
                    <label for="mince">mince</label>
                    <input type="radio" id="body_type" name="body_type" value="femme">
                </div>
                

                <div class="option">
                <label for="">Athlétique</label>
                <input type="radio" id="body_type" name="body_type" value="Athlétique">
            </div>

                <button class="nextButton1">Suivant</button>
            </div>


        </div>
            `,
            section2: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Quel est votre niveau d'étude?</h3>

                <div class="option">
                    <label for="no_study"> Bac ou moins</label>
                    <input type="radio" id="education" name="education" value="baccalauriat ou moins">
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
                  <label for="Doctorat">Doctorat et plus</label>
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
                <h3>Quel est votre orientation sexuelle?</h3>

                <div class="option">
                    <label for="Hétérosexuel">Hétérosexuel</label>
                    <input type="radio" id="orientation" name="orientation" value="Hétérosexuel">
                </div>
                <div class="option">
                    <label for="Homosexuel">Homosexuel</label>
                    <input type="radio" id="orientation" name="orientation" value="Homosexuel">
                </div>
                

                <div class="option">
                    <label for="Bisexuel">Bisexuel</label>
                    <input type="radio" id="orientation" name="orientation" value="Bisexuel">
                </div>
                

                <button class="nextButton1">Suivant</button>
            </div>


        </div>
            `,
            section2: `
            <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Dites-nous en plus sur votre alimentation: ?</h3>

                <div class="option">
                    <label for="Je n'ai pas de préférence"> Je n'ai pas de préférence</label>
                    <input type="radio" id="Diet" name="Diet" value="Je n'ai pas de préférence">
                </div>
                
               <div class="option">
                    <label for="Je suis végétarien"> Je suis végétarien</label>
                    <input type="radio" id="Diet" name="Diet" value="Je suis végétarien">
                </div>
              <div class="option">
                    <label for="Je suis un halal"> Je suis un halal</label>
                    <input type="radio" id="Diet" name="Diet" value="Je suis un halal">
                </div>
                
                <button class="nextButton2">Suivant</button>
            </div>


        </div>
            `
        },
        {
            section1: `
         <div class="form-container">
              <h2>Questionnaire</h2>

                <div class="form-group">
                     <h3>Fumez -vous ?</h3>
    
                  <div class="option">
                     <label for="Jamais">Jamais</label>
                     <input type="radio" id="smokes" name="smokes" value="Jamais">
                  </div>
               
                   
                   
                    <div class="option">
                        <label for="Souvent">Souvent</label>
                        <input type="radio" id="smokes" name="smokes" value="Parfois">
                    </div>
                    
                  
                    <div class="option">
                       <label for="très souvent">très souvent</label>
                        <input type="radio" id="smokes" name="smokes" value="très souvent">
                    </div>
                    <div class="option">
                       <label for="J'essaie d'abandonner">J'essaie d'abandonner</label>
                        <input type="radio" id="smokes" name="smokes" value="très souvent">
                    </div>
                   
                    <button class="nextButton1">Suivant</button>
                </div>

            </div>


        
            `,
            section2: `
        <div class="form-container">
            <h2>Questionnaire</h2>

            <div class="form-group">
                <h3>Vous droguez-vous ?</h3>

                
                <div class="option">
                    <label for="Jamais">Jamais</label>
                    <input type="radio" id="drugs" name="drugs" value="Jamais">
                </div>
               
                <div class="option">
                <label for="Souvent">Souvent</label>
                 <input type="radio" id="education" name="education" value="Souvent">
              </div>
                <div class="option">
                   <label for="très souvent">très souvent</label>
                    <input type="radio" id="drugs" name="drugs" value="très souvent">
                </div>
               
               
                <button class="nextButton2">Suivant</button>
            </div>


        </div>
            `
        }
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
}