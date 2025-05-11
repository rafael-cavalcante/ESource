new DataTable('#example', {
    language: {
        paginate: {
            first: 'Primeira',
            previous: '<i class="bi bi-chevron-left"></i>',
            next: '<i class="bi bi-chevron-right"></i>',
            last: 'Última'
        },
        url: 'https://cdn.datatables.net/plug-ins/2.3.0/i18n/pt-BR.json',
    },
    layout: {
        topStart: 'pageLength',
        topEnd: 'search',
        bottomStart: 'paging',
        bottomEnd: 'info',
    },
    responsive: true,
});