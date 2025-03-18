const express = require('express');
const Item = require('../models/Item');
const router = express.Router();

// Tüm giysileri listele
router.get('/items', async (req, res) => {
    const items = await Item.find();
    res.json(items);
});

// Giysi bilgilerini güncelle
router.put('/items/:id', async (req, res) => {
    const { name, price } = req.body;
    const item = await Item.findByIdAndUpdate(req.params.id, { name, price }, { new: true });
    res.json(item);
});

module.exports = router;
