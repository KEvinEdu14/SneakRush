const express = require('express');
const cors = require('cors');
const routes = require('./interfaces/routes/index');
const { PORT } = require('./infrastructure/config');

const app = express();

app.use(cors());
app.use(express.json());
app.use('/api', routes);

app.get('/health', (req, res) => res.send('2FA Service OK'));

module.exports = app;
