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

    if (formsetContainer.children.length > 1) {
        const templateAnt = formsetContainer.children[0].cloneNode(true);
        Array.from(formsetContainer.children).forEach(form => {
            form.style.display = 'none';
        });
        templateAnt.querySelectorAll('input[type="number"]').forEach(input => input.value = null);
        templateAnt.querySelectorAll('select').forEach(select => select.selectedIndex = 0);
        formsetContainer.appendChild(templateAnt);
        updateFormIndexes();
        actualizarFormulario();
    }

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
        if (e.target.classList.contains('action-button')) {
            e.preventDefault();
            const form = e.target.closest('.formset-row');
            form.remove();
            updateFormIndexes();
        }
    });
});


// funcion para recortar texto dentro de una cadena 
function obtenerTextoEntre(text, caracterInicio, caracterFin) {
    const inicio = text.indexOf(caracterInicio) + 1;
    const fin = text.indexOf(caracterFin);
    if (inicio > 0 && fin > 0 && inicio < fin) {
        return text.substring(inicio, fin).trim();
    } 
    return null; // Retorna null si los caracteres no se encuentran en el orden correcto
}

function eliminarFormulario(index) {
    const form = document.querySelector(`#detalle-formset-container .formset-row:nth-child(${index + 1})`);
    if(form) {
        form.remove() // Eliminar el formset que contiene el detalle.
    }    
    const row = document.querySelector(`table tbody tr[data-form-index="${index}"]`);
    if (row) {
        row.remove(); // Eliminar la fila de la tabla.
    }
}

function actualizarFormulario() {
    const $tbody = document.querySelector('.tbody'); // Asegúrate de tener un selector correcto
    const productos = document.querySelectorAll('select[name$="-producto"]');
    const cantidades = document.querySelectorAll('input[name$="-cantidad"]');
    // Limpiar el contenido del tbody antes de agregar nuevas filas
    $tbody.innerHTML = '';

    productos.forEach((producto, index) => {
        if(producto.options[producto.selectedIndex].text!='---------'){
            const text = producto.options[producto.selectedIndex].text
            // obtiene el id del texto enviado en el select
            const resultado = parseInt(obtenerTextoEntre(text, ':', '-').trim(),10);
            // console.log('text: ',resultado)
            fetch('/ventas/api/productos')
                .then(response => response.json())
                .then(data => {
                    // console.log(data);  // Aquí puedes manejar el JSON de los productos
                    // Procesar y mostrar los datos en tu frontend
                    for (i=0; i<data.length;i++){
                        if(data[i].id_producto === resultado) {
                            // console.log(data[i])
                            // if data[index].id_producto == producto.options[producto.selectedIndex].text
        
                            // console.log(data[index]);
                            // console.log(producto.options[producto.selectedIndex].text);
        
                            // Verifica que la cantidad no esté vacía
                            const cantidad = cantidades[index] ? cantidades[index].value : '';
                            // Crear la fila
                            const row = document.createElement('tr');
                            row.setAttribute("data-form-index", index);
                            row.innerHTML = `
                                <td>${index + 1}</td>
                                <td>${data[i].id_producto}</td>
                                <td>${data[i].descripcion}</td>
                                <td>${data[i].categoria}</td>
                                <td>${cantidad}</td>
                                <td>${data[i].precio}</td>
                                <td>
                                    <div class="action-buttons">
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
                    }
                })
                .catch(error => console.error('Error:', error));
        }
    });
}