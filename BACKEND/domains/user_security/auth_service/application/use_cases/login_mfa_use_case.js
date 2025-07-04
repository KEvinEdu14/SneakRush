const crypto = require('crypto');
const axios  = require('axios');

const { TWO_FA_SEND_URL } = process.env;
const attempts = new Map();               // almacenamiento en memoria

/**
 * Dispara el código 2FA y devuelve { mfa:true, attemptId }
 */
module.exports = async function loginMFA(user) {
  const attemptId = crypto.randomUUID();
  attempts.set(attemptId, { userId: user.id, createdAt: Date.now() });

  await axios.post(TWO_FA_SEND_URL, {
    userId: user.id,
    destination: user.email
  });

  return { mfa: true, attemptId };
};

module.exports.attempts = attempts;
