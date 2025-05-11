const confirmModal = document.getElementById('confirmModalArquiva');
confirmModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const itemId = button.getAttribute('data-item-id');
    const itemName = button.getAttribute('data-item-name');
    const itemUrl = button.getAttribute('data-item-url');

    // Atualizar o texto dentro do modal
    const itemNameSpan = confirmModal.querySelector('#itemNameInModal');
    itemNameSpan.textContent = itemName;

    // Atualizar a action do formulário
    const form = confirmModal.querySelector('#arquivaForm');
    form.action = `/${itemUrl}/${itemId}/`;
});