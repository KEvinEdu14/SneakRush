const axios = require('axios');
const jwt   = require('jsonwebtoken');
const { attempts } = require('./login_mfa_use_case');

const { TWO_FA_VALIDATE_URL, JWT_SECRET } = process.env;

/**
 * Valida el código 2FA. Devuelve { ok:true, token } o { ok:false, reason }
 */
module.exports = async ({ attemptId, code }) => {
  const attempt = attempts.get(attemptId);
  if (!attempt) return { ok: false, reason: 'attempt_not_found' };

  const resp = await axios.post(TWO_FA_VALIDATE_URL, {
    userId: attempt.userId,
    code
  });

  if (!resp.data.valid) return { ok: false, reason: 'invalid_code' };

  attempts.delete(attemptId);
  const token = jwt.sign({ sub: attempt.userId }, JWT_SECRET, { expiresIn: '15m' });
  return { ok: true, token };
};
