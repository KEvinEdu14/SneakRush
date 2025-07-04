const { createClient } = require('redis');
const { REDIS_EVENTS_URL, REDIS_CHANNEL } = require('../config');
const sendNotification = require('../../application/use_cases/send_notification');

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
  }
})();

module.exports = sub;
