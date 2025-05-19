document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => {
        if (form.action.includes('delete')) {
            if (!confirm('Tem certeza que deseja excluir esta tarefa?')) {
                e.preventDefault();
            }
        }
    });
});