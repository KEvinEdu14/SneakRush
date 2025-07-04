require('dotenv').config();

module.exports = {
  PORT: process.env.PORT || 4003,
  MONGO_URL: process.env.MONGO_URL,
  REDIS_EVENTS_URL: process.env.REDIS_EVENTS_URL,
  REDIS_CHANNEL: process.env.REDIS_CHANNEL || 'notification_events'
};
