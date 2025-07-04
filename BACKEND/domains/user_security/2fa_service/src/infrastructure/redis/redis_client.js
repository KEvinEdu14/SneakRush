const { createClient } = require('redis');
const { REDIS_URL } = require('../config');

const client = createClient({ url: REDIS_URL });

client.on('error', (err) => console.error('Redis Client Error', err));

(async () => {
  if (!client.isOpen) {
    await client.connect();
  }
})();

module.exports = client;
