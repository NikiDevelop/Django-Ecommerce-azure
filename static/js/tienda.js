var botonMenu = document.getElementById('boton-menu');
    var opcionesMenu = document.getElementById('opciones-menu');
    
    botonMenu.addEventListener('click', function() {
      opcionesMenu.style.display = opcionesMenu.style.display === 'none' ? 'block' : 'none';
    });