const bcrypt = require('bcrypt');
const { User } = require('../../models/user_model');

exports.registerController = async (req, res) => {
  const { email, password } = req.body;
  try {
    const exists = await User.findOne({ where: { email } });
    if (exists) {
      return res.status(409).json({ message: 'User already exists' });
    }
    const hashedPassword = await bcrypt.hash(password, 10);
    const user = await User.create({ email, password: hashedPassword });
    res.status(201).json({ message: 'User created', user: { id: user.id, email: user.email } });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
