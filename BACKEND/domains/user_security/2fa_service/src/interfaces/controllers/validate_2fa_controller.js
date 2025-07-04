const validate2faCode = require('../../application/use_cases/validate_2fa_code');
const redisClient = require('../../infrastructure/redis/redis_client');

module.exports = async (req, res) => {
  try {
    const { userId, code } = req.body;
    if (!userId || !code) {
      return res.status(400).json({ valid: false, message: 'userId and code are required.' });
    }
    const valid = await validate2faCode(userId, code, redisClient);
    return res.status(200).json({ valid });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ valid: false, message: 'Failed to validate code' });
  }
};
