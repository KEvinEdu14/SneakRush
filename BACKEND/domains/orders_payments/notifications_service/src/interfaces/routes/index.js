const express = require('express');
const router = express.Router();
const sendController = require('../controllers/send_controller');

router.post('/send', sendController);

module.exports = router;
