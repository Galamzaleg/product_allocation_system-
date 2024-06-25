function loadTableData(url, tableId) {
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById(tableId);
            tableBody.innerHTML = '';
            data.forEach(row => {
                const tr = document.createElement('tr');
                for (const key in row) {
                    const td = document.createElement('td');
                    td.textContent = row[key];
                    tr.appendChild(td);
                }
                tableBody.appendChild(tr);
            });
        })
        .catch(error => console.error('Error loading table data:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('asinsTable')) {
        loadTableData('/api/asins', 'asinsTable');
    }
    if (document.getElementById('clientsTable')) {
        loadTableData('/api/clients', 'clientsTable');
    }
    if (document.getElementById('storesTable')) {
        loadTableData('/api/stores', 'storesTable');
    }
    if (document.getElementById('ungatingStatusesTable')) {
        loadTableData('/api/ungating', 'ungatingStatusesTable');
    }
    if (document.getElementById('preordersTable')) {
        loadTableData('/api/preorders', 'preordersTable');
    }
    if (document.getElementById('palletsTable')) {
        loadTableData('/api/pallets', 'palletsTable');
    }
});
