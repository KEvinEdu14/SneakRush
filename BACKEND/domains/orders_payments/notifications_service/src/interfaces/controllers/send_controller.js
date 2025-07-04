const sendNotification = require('../../application/use_cases/send_notification');

module.exports = async (req, res) => {
  try {
    const { to, message } = req.body;
    if (!to || !message) {
      return res.status(400).json({ sent: false, msg: 'to & message required' });
    }
    await sendNotification(to, message);
    return res.status(200).json({ sent: true });
  } catch (err) {
    console.error(err);
    return res.status(500).json({ sent: false });
  }
};
