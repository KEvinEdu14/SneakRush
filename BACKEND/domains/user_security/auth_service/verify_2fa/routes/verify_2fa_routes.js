const express = require('express');
const router  = express.Router();
const ctrl    = require('../controllers/verify_2fa_controller');

router.post('/', ctrl);

module.exports = router;
