document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    let searchInput = document.getElementById('search-input').value;
    if (searchInput && /^\d+$/.test(searchInput)) {
      window.location.href = '/capitulo/' + searchInput;
    } else {
      Swal.fire({
        icon: 'error',
        title: 'Error',
        text: 'Ingresa un número de episodio válido',
      });
    }
  });
