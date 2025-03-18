const express = require('express');
const User = require('../models/User');
const router = express.Router();

// Kullanıcı girişi
router.post('/login', async (req, res) => {
    const { telegramId, username } = req.body;

    // Kullanıcıyı bul veya oluştur
    let user = await User.findOne({ telegramId });
    if (!user) {
        user = new User({ telegramId, username });
        await user.save();
    }

    res.json({ success: true, user });
});

module.exports = router;
