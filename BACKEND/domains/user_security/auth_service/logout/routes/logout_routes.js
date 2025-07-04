const express = require('express');
const router = express.Router();
const { logoutController } = require('../controllers/logout_controller');

router.post('/', logoutController);

module.exports = router;
