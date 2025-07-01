const loginService = require('./service');

const loginUser = async (req, res) => {
  try {
    const { token } = await loginService.authenticate(req.body);
    res.status(200).json({ token });
  } catch (err) {
    res.status(401).json({ error: err.message });
  }
};

module.exports = { loginUser };
