const send2faCode = require('../../application/use_cases/send_2fa_code');
const redisClient = require('../../infrastructure/redis/redis_client');
const notification = require('../../infrastructure/notifications/send_notification');

module.exports = async (req, res) => {
  try {
    const { userId, destination } = req.body;
    if (!userId || !destination) {
      return res.status(400).json({ message: 'userId and destination are required.' });
    }
    await send2faCode(userId, destination, redisClient, notification);
    return res.status(200).json({ message: '2FA code sent' });
  } catch (error) {
    console.error(error);
    return res.status(500).json({ message: 'Failed to send 2FA code' });
  }
};
