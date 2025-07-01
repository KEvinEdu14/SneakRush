const express = require('express');
const dotenv = require('dotenv');
const { sequelize } = require('./shared/config/db');

dotenv.config();
const app = express();
app.use(express.json());

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

sequelize.sync()
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Auth service running on port ${PORT}`);
    });
  })
  .catch((err) => {
    console.error('Failed to connect to DB:', err);
  });
