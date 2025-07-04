require('dotenv').config();

module.exports = {
  PORT: process.env.PORT || 4002,
  REDIS_URL: process.env.REDIS_URL,
  NOTIFICATION_SERVICE_URL: process.env.NOTIFICATION_SERVICE_URL,
  CODE_EXPIRATION_MINUTES: parseInt(process.env.CODE_EXPIRATION_MINUTES || '5', 10),
  JWT_SECRET: process.env.JWT_SECRET || 'default_secret'
};
