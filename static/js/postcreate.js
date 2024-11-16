function previewImage(event) {
    const preview = document.getElementById('image-preview');
    const file = event.target.files[0];
  
    if (file) {
      const reader = new FileReader();
  
      reader.onload = function () {
        preview.src = reader.result;
        preview.style.display = 'block';
      };
  
      reader.readAsDataURL(file);
    } else {
      preview.src = '';
      preview.style.display = 'none';
    }
  }
  