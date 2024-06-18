function previewImage(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
        document.querySelector('.photo-input-label svg').src = e.target.result;
        document.querySelector('.photo-input-text').textContent = '';
      };
      reader.readAsDataURL(input.files[0]);
    }
  }