const eliminacion = document.querySelectorAll('.btnDelete');
const editar = document.querySelectorAll('.btnEditar');

(function(){
    
    animacion(document.title, "¡Productos Actualizados!", "success", "Finalizar");

    eliminacion.forEach(btn =>{
        btn.addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                text: "¿Desea eliminar este producto?",
                icon: "warning",
                cancelButtonText: "Cancelar",
                cancelButtonColor: "#DDDDDD",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#dc3545",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: ()=>{
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });

    editar.forEach(btn =>{
        btn.addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                text: "¿Desea editar este producto?",
                icon: "question",
                cancelButtonText: "Cancelar",
                cancelButtonColor: "#DDDDDD",
                showCancelButton: true,
                confirmButtonText: "Editar",
                confirmButtonColor: "#46a2fd",
                backdrop: true,
                showLoaderOnConfirm: true,
                preConfirm: ()=>{
                    location.href = e.target.href;
                },
                allowOutsideClick: () => false,
                allowEscapeKey: () => false,
            });
        });
    });


})();