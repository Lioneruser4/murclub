let currentEditItemId = null;

// Giysileri yükle
async function loadItems() {
    const response = await fetch('/api/items');
    const items = await response.json();
    const itemList = document.getElementById('itemList');
    itemList.innerHTML = '';

    items.forEach(item => {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'item';
        itemDiv.innerHTML = `
            <span>${item.name} - ${item.price} MurCoin</span>
            <button onclick="editItem('${item._id}')">Düzenle</button>
        `;
        itemList.appendChild(itemDiv);
    });
}

// Giysi düzenleme formunu aç
function editItem(itemId) {
    currentEditItemId = itemId;
    const editForm = document.getElementById('editForm');
    editForm.style.display = 'block';

    // Mevcut bilgileri formda göster
    fetch(`/api/items/${itemId}`)
        .then(response => response.json())
        .then(item => {
            document.getElementById('editName').value = item.name;
            document.getElementById('editPrice').value = item.price;
        });
}

// Değişiklikleri kaydet
async function saveChanges() {
    const name = document.getElementById('editName').value;
    const price = document.getElementById('editPrice').value;

    const response = await fetch(`/api/items/${currentEditItemId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, price })
    });

    if (response.ok) {
        alert('Değişiklikler kaydedildi!');
        loadItems();
        cancelEdit();
    } else {
        alert('Bir hata oluştu.');
    }
}

// Düzenleme formunu kapat
function cancelEdit() {
    document.getElementById('editForm').style.display = 'none';
    currentEditItemId = null;
}

// Sayfa yüklendiğinde giysileri yükle
window.onload = loadItems;
