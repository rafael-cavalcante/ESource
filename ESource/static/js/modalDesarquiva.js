const confirmDesarquivaModal = document.getElementById('confirmDesarquivaModal');
confirmDesarquivaModal.addEventListener('show.bs.modal', function (event) {
  const button = event.relatedTarget;
  const itemId = button.getAttribute('data-item-id');
  const itemName = button.getAttribute('data-item-name');
  const itemUrl = button.getAttribute('data-item-url');

  // Atualizar o texto dentro do modal
  const itemNameSpan = confirmDesarquivaModal.querySelector('#itemNameInModal');
  itemNameSpan.textContent = itemName;

  // Atualizar a action do formulário
  const form = confirmDesarquivaModal.querySelector('#desarquivaForm');
  form.action = `/${itemUrl}/${itemId}/`;
});