const axios = require('axios');
const { NOTIFICATION_SERVICE_URL } = require('../config');

module.exports = {
  send: async (destination, code) => {
    // Aquí se puede integrar el microservicio real de notificación (email/SMS)
    await axios.post(NOTIFICATION_SERVICE_URL, {
      to: destination,
      message: `Your verification code is: ${code}`
    });
  }
};
