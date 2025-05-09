const confirmDeleteModal = document.getElementById("confirmDeleteModal");
confirmDeleteModal.addEventListener("show.bs.modal", function (event) {
  const button = event.relatedTarget;
  const itemId = button.getAttribute("data-item-id");
  const itemName = button.getAttribute("data-item-name");

  // Atualizar o texto dentro do modal
  const itemNameSpan = confirmDeleteModal.querySelector("#itemNameInModal");
  itemNameSpan.textContent = itemName;

  // Atualizar a action do formulário
  const form = confirmDeleteModal.querySelector("#deleteForm");
  form.action = `/delete-item/${itemId}/`;
});
