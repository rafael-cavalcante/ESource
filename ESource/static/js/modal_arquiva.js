const modal_confirmacao_arquivar = document.getElementById('modal_confirmacao_arquivar');

modal_confirmacao_arquivar.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget;
    const item_id = button.getAttribute('data-item-id');
    const item_nome = button.getAttribute('data-item-name');
    const item_url = button.getAttribute('data-item-url');

    // Atualizar o texto dentro do modal
    const item_nome_modal = modal_confirmacao_arquivar.querySelector('#item_nome_modal');
    item_nome_modal.textContent = item_nome;

    // Atualizar a action do formulário
    const form = modal_confirmacao_arquivar.querySelector('#form_arquivar');
    form.action = `/${item_url}/${item_id}/`;
});