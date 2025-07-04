const TwoFactorCode = require('../../domain/entities/two_factor_code');
const { CODE_EXPIRATION_MINUTES } = require('../../infrastructure/config/index');
const crypto = require('crypto');

module.exports = async (userId, destination, redisClient, notification) => {
  // Generar código aleatorio de 6 dígitos
  const code = (crypto.randomInt(100000, 1000000)).toString();
  const expiresAt = Date.now() + (CODE_EXPIRATION_MINUTES * 60 * 1000);

  // Guardar código en Redis
  await redisClient.setEx(`2fa:${userId}`, CODE_EXPIRATION_MINUTES * 60, code);

  // Enviar código vía notificación
  await notification.send(destination, code);

  return new TwoFactorCode(userId, code, expiresAt);
};
