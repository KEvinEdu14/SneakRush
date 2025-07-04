const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();

const { connectDB, sequelize } = require('./db/db');
const { User } = require('./models/user_model');

const loginRoutes = require('./login/routes/login_routes');
const registerRoutes = require('./register/routes/register_routes');
const refreshRoutes = require('./refresh/routes/refresh_token_routes');
const logoutRoutes = require('./logout/routes/logout_routes');
const verifyRoutes = require('./verify_2fa/routes/verify_2fa_routes');
const app = express();
app.use(cors());
app.use(bodyParser.json());

app.use('/api/auth/login', loginRoutes);
app.use('/api/auth/login/verify', verifyRoutes);
app.use('/api/auth/register', registerRoutes);
app.use('/api/auth/refresh', refreshRoutes);
app.use('/api/auth/logout', logoutRoutes);

const PORT = process.env.PORT || 3000;

// Primero conecta a la base de datos y luego sincroniza modelos (crea tablas)
connectDB().then(() => {
  sequelize.sync() // puedes usar { alter: true } en desarrollo
    .then(() => {
      console.log('DB Synced! Starting server...');
      app.listen(PORT, () => {
        console.log(`Auth Service running on port ${PORT}`);
      });
    })
    .catch(err => {
      console.error('Error syncing DB:', err);
      process.exit(1);
    });
});

module.exports = app; // Para testing
