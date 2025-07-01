const { body } = require('express-validator');

const validateRegister = [
  body('email')
    .isEmail()
    .withMessage('Email must be valid'),
  body('password')
    .isLength({ min: 6 })
    .withMessage('Password must be at least 6 characters long')
];

module.exports = validateRegister;
