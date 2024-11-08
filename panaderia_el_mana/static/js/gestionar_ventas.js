// function agregarProducto() {
//     // Clona el primer formulario de detalle y lo ajusta para el nuevo índice
//     const container = document.getElementById('detalle-form-container');
//     const totalForms = document.getElementById("id_form-TOTAL_FORMS");
    
//     // Clonar el primer formulario del formset
//     let newForm = container.children[0].cloneNode(true);
    
//     // Obtener el nuevo índice para el formset y ajustar los elementos del nuevo formulario
//     let formCount = parseInt(totalForms.value);
//     newForm.innerHTML = newForm.innerHTML.replace(/form-\d+/g, `form-${formCount}`);
    
//     // Limpiar los valores de entrada en el formulario clonado
//     const inputs = newForm.querySelectorAll('input');
//     inputs.forEach(input => input.value = "");
    
//     // Añadir el formulario clonado al contenedor y actualizar el TOTAL_FORMS
//     container.appendChild(newForm);
//     totalForms.value = formCount + 1;
// }

// function anularVenta(idVenta) {
//     var form = document.createElement('form');
//     form.method = 'POST';
//     form.action = `/url/to/anular/${idVenta}/`; // ajusta la URL según tu ruta 
//     var csrfToken = document.createElement('input');
//     csrfToken.type = 'hidden';
//     csrfToken.name = 'csrfmiddlewaretoken';
//     csrfToken.value = '{{ csrf_token }}'; // Asegúrate de que el token CSRF esté disponible 
//     form.appendChild(csrfToken);
//     document.body.appendChild(form);
//     form.submit();
// }

// function confirmCancel(url) {
//     if (confirm("¿Estás seguro de que deseas anular esta venta?")) {
//         var form = document.createElement('form');
//         form.method = 'POST';
//         form.action = url;

//         var csrfToken = document.createElement('input');
//         csrfToken.type = 'hidden';
//         csrfToken.name = 'csrfmiddlewaretoken';
//         csrfToken.value = '{{ csrf_token }}'; // asegúrate de que el token CSRF esté disponible
//         form.appendChild(csrfToken);
//         document.body.appendChild(form);
//         form.submit();
//     }
// }


function confirmCancel(url) {
    Swal.fire({
        title: 'Anular la venta',
        text: "¿Estás seguro de que deseas anular esta venta?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            let formulario = document.getElementById('formulario_anular')
            formulario.action = url
            formulario.submit()
        }
    });
}