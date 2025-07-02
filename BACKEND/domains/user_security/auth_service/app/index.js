const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const { sequelize } = require('./shared/config/db');

dotenv.config();
const app = express();
app.use(cors());
app.use(express.json());

// Health-check para ALB
app.get('/health', (_req, res) => res.status(200).send('OK'));

// Import routes
const registerRoutes = require('./register_user/route');
const loginRoutes = require('./login_user/route');
const refreshRoutes = require('./refresh_token/route');

// Mount routes
app.use('/api/auth/register', registerRoutes);
app.use('/api/auth/login', loginRoutes);
app.use('/api/auth/refresh-token', refreshRoutes);

// DB connection and start
const PORT = process.env.PORT || 8000;
const HOST = '0.0.0.0';

if (process.env.NODE_ENV !== 'test') {
  sequelize.sync().then(() => {
    app.listen(PORT, HOST, () => {
      console.log(`Auth service running on ${HOST}:${PORT}`);
    });
  });
}

module.exports = app;
