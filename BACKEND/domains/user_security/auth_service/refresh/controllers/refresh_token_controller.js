const jwt = require('jsonwebtoken');

exports.refreshTokenController = (req, res) => {
  const { token } = req.body;
  if (!token) return res.status(401).json({ message: 'Token missing' });
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET, { ignoreExpiration: true });
    // Opcional: check si el token fue invalidado (token blacklist)
    const newToken = jwt.sign({ id: payload.id, email: payload.email }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ token: newToken });
  } catch (err) {
    res.status(403).json({ message: 'Invalid token' });
  }
};
