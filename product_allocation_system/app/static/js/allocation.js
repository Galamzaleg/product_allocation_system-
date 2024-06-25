document.getElementById('generateCartForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const clientName = document.getElementById('clientName').value;
    const clientID = document.getElementById('clientID').value;
    const storeID = document.getElementById('storeID').value;

    fetch('/generate_pallets', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ clientName, clientID, storeID })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            loadTableData('/api/pallets', 'cartTable');
        } else {
            alert('Error: ' + data.message);
        }
    })
    .catch(error => console.error('Error generating cart:', error));
});
