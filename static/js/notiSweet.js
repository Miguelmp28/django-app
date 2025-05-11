const animacion = (tittleText, text, icon, confirmButtonText)=>{
    Swal.fire({
        tittleText: tittleText,
        text: text,
        icon: icon, //warging, info, success, error
        confirmButtonText: confirmButtonText,
    });
};
