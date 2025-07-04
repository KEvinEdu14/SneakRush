const { User } = require('../../models/user_model');
const bcrypt   = require('bcrypt');
const axios    = require('axios');
const loginMFA = require('../../application/use_cases/login_mfa_use_case');

/*───────────────────────────
   Variables de entorno
───────────────────────────*/
const {
  JWT_SECRET,                       // (por si tu use-case lo necesita)
  LOGIN_HISTORY_URL                 // ej.: http://login_history:4000/logins
} = process.env;

// ⇒  fallback si la variable no está definida
const LOGIN_HISTORY_ENDPOINT = LOGIN_HISTORY_URL || 'http://login_history:4000/logins';

/*───────────────────────────
   Controlador de login
───────────────────────────*/
exports.loginController = async (req, res) => {
  const { email, password } = req.body;

  try {
    /* 1️⃣ Buscar usuario */
    const user = await User.findOne({ where: { email } });
    if (!user) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    /* 2️⃣ Verificar contraseña */
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    /* 3️⃣ Registrar intento en login_history */
    try {
      await axios.post(LOGIN_HISTORY_ENDPOINT, {
        user_id: user.id,
        ip: req.ip || req.connection.remoteAddress
      });
      console.log('Login-history notificado para usuario:', user.id);
    } catch (err) {
      console.error('Error notificando login-history:', err.message);
    }

    /* 4️⃣ Disparar MFA (2fa_service) */
    const payload = await loginMFA(user);   // { mfa:true, attemptId: '...' }
    return res.status(200).json(payload);

  } catch (err) {
    console.error(err);
    return res.status(500).json({ message: 'Server error', error: err.message });
  }
};
