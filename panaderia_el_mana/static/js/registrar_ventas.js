function agregarProducto() {
    // Clona el primer formulario de detalle y lo ajusta para el nuevo índice
    const container = document.getElementById('detalle-form-container');
    const totalForms = document.getElementById("id_form-TOTAL_FORMS");
    
    // Clonar el primer formulario del formset
    let newForm = container.children[0].cloneNode(true);
    
    // Obtener el nuevo índice para el formset y ajustar los elementos del nuevo formulario
    let formCount = parseInt(totalForms.value);
    newForm.innerHTML = newForm.innerHTML.replace(/form-\d+/g, `form-${formCount}`);
    
    // Limpiar los valores de entrada en el formulario clonado
    const inputs = newForm.querySelectorAll('input');
    inputs.forEach(input => input.value = "");
    
    // Añadir el formulario clonado al contenedor y actualizar el TOTAL_FORMS
    container.appendChild(newForm);
    totalForms.value = formCount + 1;
}