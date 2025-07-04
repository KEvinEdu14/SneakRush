const app = require('./app');
const { PORT } = require('./infrastructure/config');
require('./infrastructure/db/mongo_client');      // inicia conexión Mongo
require('./infrastructure/redis/redis_subscriber'); // inicia suscripción Redis

app.listen(PORT, () => console.log(`Notification Service on ${PORT}`));
