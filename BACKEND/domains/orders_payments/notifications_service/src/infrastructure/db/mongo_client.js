const { MongoClient } = require('mongodb');
const { MONGO_URL } = require('../config');

const client = new MongoClient(MONGO_URL);

(async () => {
  try {
    if (!client.topology) await client.connect();
    console.log('[Mongo] connected');
  } catch (err) {
    console.error('[Mongo] connection error', err);
  }
})();

module.exports = client;
