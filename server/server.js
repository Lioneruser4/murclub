const express = require('express');
const mongoose = require('mongoose');
const authRoutes = require('./routes/auth');
const itemRoutes = require('./routes/items');
const app = express();
const port = process.env.PORT || 3000;

// MongoDB bağlantısı
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

// Middleware
app.use(express.json());

// Rotlar
app.use('/api/auth', authRoutes);
app.use('/api/items', itemRoutes);

// Statik dosyalar
app.use(express.static('public'));

// Sunucuyu başlat
app.listen(port, () => {
    console.log(`Sunucu çalışıyor: http://localhost:${port}`);
});
