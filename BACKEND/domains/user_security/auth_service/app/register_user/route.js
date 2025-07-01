const express = require('express');
const { registerUser } = require('./controller');
const validateRegister = require('./validator');
const { validationResult } = require('express-validator');

const router = express.Router();

router.post('/', validateRegister, (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() });
  }
  registerUser(req, res, next);
});

module.exports = router;
