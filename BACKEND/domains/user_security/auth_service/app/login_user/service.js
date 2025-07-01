const User = require('../register_user/model');
const { comparePassword } = require('../shared/utils/hash');
const jwt = require('jsonwebtoken');

const authenticate = async ({ email, password }) => {
  const user = await User.findOne({ where: { email } });
  if (!user) throw new Error('Invalid credentials');

  const isMatch = await comparePassword(password, user.password_hash);
  if (!isMatch) throw new Error('Invalid credentials');

  const token = jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: process.env.JWT_EXPIRES_IN || '1h' }
  );

  return { token };
};

module.exports = { authenticate };
