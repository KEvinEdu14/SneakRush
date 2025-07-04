const app = require('./app');
const { PORT } = require('./infrastructure/config');

app.listen(PORT, () => {
  console.log(`2FA Service running on port ${PORT}`);
});
