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
        const template = formsetContainer.children[0].cloneNode(true);
        template.style.display = '';

        if (formCount >= 10) {
            alert("No puedes agregar más de 10 productos.");
            return;
        }    
        // Ocultar el último formulario si existe
        if (formCount > 0) {
            const lastForm = formsetContainer.children[formCount - 1];
            lastForm.style.display = 'none';
        }
        // Limpiar los valores del formulario clonado
        template.querySelectorAll('input[type="number"]').forEach(input => input.value = null);
        template.querySelectorAll('select').forEach(select => select.selectedIndex = 0);

        formsetContainer.appendChild(template);
        updateFormIndexes();
        actualizarFormulario();
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

function actualizarFormulario() {
    const $tbody = document.querySelector('.tbody'); // Asegúrate de tener un selector correcto
    const productos = document.querySelectorAll('select[name$="-producto"]');
    const cantidades = document.querySelectorAll('input[name$="-cantidad"]');
    // Limpiar el contenido del tbody antes de agregar nuevas filas
    $tbody.innerHTML = '';

    productos.forEach((producto, index) => {
        if(producto.options[producto.selectedIndex].text!='Seleccione'){
            // console.log('text',producto.options[producto.selectedIndex].text)

            // Verifica que la cantidad no esté vacía
            const cantidad = cantidades[index] ? cantidades[index].value : '';
            // Crear la fila
            const row = document.createElement('tr');
            row.setAttribute("data-form-index", index);
            row.innerHTML = `
                <td>${index + 1}</td>
                <td></td>
                <td>${producto.options[producto.selectedIndex].text.split(' ')[0]}</td>
                <td></td>
                <td>${cantidad}</td>
                <td>${producto.options[producto.selectedIndex].text.split(' ').pop()}</td>
                <td>
                    <div class="action-buttons">
                        <button class="action-button edit-button" onclick="editarFormulario(${index})">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                            </svg>
                        </button>
                        <button class="action-button delete-button" onclick="eliminarFormulario(${index})">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                <path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5m3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0z"/>
                                <path d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4zM2.5 3h11V2h-11z"/>
                            </svg>
                        </button>
                    </div>
                </td>
            `;

            // Agregar la fila al tbody
            $tbody.appendChild(row);
        }
    });
}