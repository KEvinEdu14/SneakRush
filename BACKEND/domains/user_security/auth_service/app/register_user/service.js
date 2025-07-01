const User = require('./model');
const { hashPassword } = require('../shared/utils/hash');

const createUser = async ({ email, password }) => {
  const existing = await User.findOne({ where: { email } });
  if (existing) throw new Error('User already exists');

  const password_hash = await hashPassword(password);
  const user = await User.create({ email, password_hash });

  return {
    id: user.id,
    email: user.email,
    createdAt: user.createdAt
  };
};

module.exports = { createUser };
