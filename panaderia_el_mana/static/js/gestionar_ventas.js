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

// Funcion para anular una venta 
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

// Para agregar productos o detalles a la una venta
document.addEventListener('DOMContentLoaded', function() {
    const addButton = document.getElementById('agregar_producto');
    const formsetContainer = document.getElementById('detalle-formset-container');
    const totalForms = document.getElementById('id_venta-TOTAL_FORMS');

    // Función para actualizar los índices de los formularios
    function updateFormIndexes() {
        const forms = formsetContainer.getElementsByClassName('formset-row');
        for (let i = 0; i < forms.length; i++) {
            const formInputs = forms[i].getElementsByTagName('input');
            const formSelects = forms[i].getElementsByTagName('select');

            for (let input of formInputs) {
                updateElementIndex(input, 'venta', i);
            }
            for (let select of formSelects) {
                updateElementIndex(select, 'venta', i);
            }
        }
        totalForms.value = forms.length;
    }

    // Función para actualizar el índice de un elemento
    function updateElementIndex(element, prefix, index) {
        const idRegex = new RegExp(`(${prefix}-\\d+)`);
        const replacement = `${prefix}-${index}`;
        if (element.id) element.id = element.id.replace(idRegex, replacement);
        if (element.name) element.name = element.name.replace(idRegex, replacement);
    }

    // Agregar nuevo formulario
    addButton.addEventListener('click', function(e) {
        e.preventDefault();
        const formCount = formsetContainer.children.length;
        if (formCount >= 10) {
            alert("No puedes agregar más de 10 productos.");
            return;
        }
        const template = formsetContainer.children[0].cloneNode(true);

        // Limpiar los valores del formulario clonado
        // template.querySelectorAll('input[type="text"]').forEach(input => input.value = '');
        template.querySelectorAll('input[type="number"]').forEach(input => input.value = null);
        template.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

        formsetContainer.appendChild(template);
        updateFormIndexes();
    });

    // Eliminar formulario
    formsetContainer.addEventListener('click', function(e) {
        if (e.target.classList.contains('delete-form')) {
            e.preventDefault();
            const form = e.target.closest('.seccion-form');
            form.remove();
            updateFormIndexes();
        }
    });
});