const registerService = require('./service');

const registerUser = async (req, res) => {
  try {
    const user = await registerService.createUser(req.body);
    res.status(201).json({ message: 'User registered successfully', user });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
};

module.exports = { registerUser };
