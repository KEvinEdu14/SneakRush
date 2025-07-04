const express = require('express');
const send2faController = require('../controllers/send_2fa_controller');
const validate2faController = require('../controllers/validate_2fa_controller');

const router = express.Router();

router.post('/2fa/send', send2faController);
router.post('/2fa/validate', validate2faController);

module.exports = router;
