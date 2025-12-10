function setupSearch(inputId, tableId) {
    const input = document.getElementById(inputId);
    const table = document.getElementById(tableId);

    if (!input || !table) return;

    input.addEventListener('keyup', () => {
        const filter = input.value.toLowerCase();
        const rows = table.getElementsByTagName('tr');

        for (let i = 1; i < rows.length; i++) {
            const row = rows[i];
            const rowText = row.textContent.toLowerCase();
            row.style.display = rowText.includes(filter) ? '' : 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    setupSearch('searchInput', 'inventoryTable');
    setupSearch('categorySearchInput', 'categoryTable');
    setupSearch('maintenanceSearchInput', 'maintenanceTable');
});
