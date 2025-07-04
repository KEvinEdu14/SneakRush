const verifyUC = require('../../application/use_cases/verify_2fa_use_case');

module.exports = async (req, res) => {
  const { attemptId, code } = req.body;
  const result = await verifyUC({ attemptId, code });

  if (!result.ok) return res.status(401).json(result);
  return res.status(200).json({ token: result.token });
};
