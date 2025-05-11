const eliminar = document.querySelectorAll('.btEliminar');
const editacion = document.querySelectorAll('.btEditar');

(function(){
    
    animacion(document.title, "¡Clientes Actualizados!", "success", "Finalizar");

    eliminar.forEach(btn =>{
        btn.addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                text: "¿Desea eliminar este cliente?",
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

    editacion.forEach(btn =>{
        btn.addEventListener('click', function(e){
            e.preventDefault();
            Swal.fire({
                text: "¿Desea editar este cliente?",
                icon: "question",
                cancelButtonText: "Cancelar",
                cancelButtonColor: "#DDDDDD",
                showCancelButton: true,
                confirmButtonText: "Editar",
                confirmButtonColor: "#22ab63",
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