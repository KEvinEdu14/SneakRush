const express = require('express');
const { refreshToken } = require('./controller');
const router = express.Router();

router.post('/', refreshToken);

module.exports = router;
