const { Sequelize } = require('sequelize');

const sequelize = new Sequelize(
  process.env.DB_NAME,       // sneakrush
  process.env.DB_USER,       // postgres
  process.env.DB_PASSWORD,   // tu password
  {
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    dialect: 'postgres',
    logging: false,
    dialectOptions: {
      ssl: {
        require: true,
        rejectUnauthorized: false  // esto permite certificados autofirmados
      }
    }
  }
);

module.exports = { sequelize };
