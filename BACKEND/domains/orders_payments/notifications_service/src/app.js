const express = require('express');
const routes = require('./interfaces/routes/index');

const app = express();

app.use(express.json());
app.use('/', routes);

app.get('/health', (_req, res) => res.send('notification_service OK'));

module.exports = app;