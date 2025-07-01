const refreshService = require('./service');

const refreshToken = async (req, res) => {
  try {
    const { token } = await refreshService.generateNewToken(req.body);
    res.status(200).json({ token });
  } catch (err) {
    res.status(403).json({ error: err.message });
  }
};

module.exports = { refreshToken };
