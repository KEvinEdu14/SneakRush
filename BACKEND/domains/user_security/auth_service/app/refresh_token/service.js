const jwt = require('jsonwebtoken');
const User = require('../register_user/model');

const generateNewToken = async ({ token }) => {
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET, {
      ignoreExpiration: true
    });

    const user = await User.findByPk(decoded.userId);
    if (!user) throw new Error('User not found');

    const newToken = jwt.sign(
      { userId: user.id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN || '1h' }
    );

    return { token: newToken };
  } catch (err) {
    throw new Error('Invalid refresh token');
  }
};

module.exports = { generateNewToken };
