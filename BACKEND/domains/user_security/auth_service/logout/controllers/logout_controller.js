exports.logoutController = (req, res) => {
  // Blacklist para token si aplica
  res.json({ message: 'Logged out' });
};
