const { createClient } = require('redis');
const sendNotification = require('../../application/use_cases/send_notification');

const {
  REDIS_EVENTS_URL = 'redis://redis_2fa:6379',
  REDIS_CHANNEL    = 'notification_events'
} = process.env;

const sub = createClient({ url: REDIS_EVENTS_URL });

(async () => {
  try {
    await sub.connect();
    console.log('[Redis] subscriber connected');

    await sub.subscribe(REDIS_CHANNEL, async (msg) => {
      const { to, message } = JSON.parse(msg);
      console.log('[Redis] Event received →', to);
      await sendNotification(to, message);
    });
  } catch (err) {
    console.error('[Redis] subscriber error', err);
    process.exit(1);
  }
})();

module.exports = sub;
