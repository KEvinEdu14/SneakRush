const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const { sequelize } = require('./shared/config/db');

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

// Health check
app.get('/health', (_, res) => res.send('OK'));

// Rutas
app.use('/api/auth/register', require('./register_user/route'));
app.use('/api/auth/login',    require('./login_user/route'));
app.use('/api/auth/refresh-token', require('./refresh_token/route'));

// Arranque
const PORT = process.env.PORT || 8000;
sequelize.sync().then(() => {
  app.listen(PORT, () => console.log(`Auth service listening on ${PORT}`));
});
module.exports = app;
