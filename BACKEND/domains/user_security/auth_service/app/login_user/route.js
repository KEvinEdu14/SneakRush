const express = require('express');
const { loginUser } = require('./controller');
const router = express.Router();
const validateLogin = require('./validator');

router.post('/', validateLogin, loginUser);
router.post('/', loginUser);

module.exports = router;
