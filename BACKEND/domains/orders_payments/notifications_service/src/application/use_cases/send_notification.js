const Notification = require('../../domain/entities/notification');
const mongoClient = require('../../infrastructure/db/mongo_client');

module.exports = async (to, message) => {
  const db = mongoClient.db('notificationsdb');
  const collection = db.collection('notifications');

  const doc = new Notification(to, message);

  await collection.insertOne(doc);
  // Aquí integrarías un proveedor SMTP o SMS real; ahora solo log
  console.log(`[NOTIFICATION] → ${to} : ${message}`);

  return doc;
};
