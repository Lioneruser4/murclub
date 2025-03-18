const socket = io();

// Lobi sohbeti
const messages = document.getElementById('messages');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message) {
        socket.emit('sendMessage', message);
        messageInput.value = '';
    }
});

socket.on('newMessage', (data) => {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${data.id}: ${data.message}`;
    messages.appendChild(messageElement);
    messages.scrollTop = messages.scrollHeight;
});

// Coin toplama
const collectButton = document.getElementById('collectButton');
const countdown = document.getElementById('countdown');

let countdownTime = 3 * 60 * 60; // 3 saat (saniye cinsinden)

function updateCountdown() {
    const hours = Math.floor(countdownTime / 3600);
    const minutes = Math.floor((countdownTime % 3600) / 60);
    const seconds = countdownTime % 60;
    countdown.textContent = `${hours}:${minutes}:${seconds}`;
    if (countdownTime > 0) {
        countdownTime--;
        setTimeout(updateCountdown, 1000);
    } else {
        collectButton.disabled = false;
    }
}

collectButton.addEventListener('click', () => {
    fetch('/collectCoins', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ telegramId: user.telegramId })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('10 MurCoin kazandınız!');
            countdownTime = 3 * 60 * 60;
            collectButton.disabled = true;
            updateCountdown();
        } else {
            alert(data.message);
        }
    });
});

updateCountdown();
