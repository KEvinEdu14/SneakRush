require('dotenv').config();
const express = require('express');
const cartRoutes = require('./interfaces/routes/cart_routes');

const app = express();
app.use(express.json());
app.use('/cart', cartRoutes);

// error handler
app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: err.message });
});

const PORT = process.env.PORT || 4001;
app.listen(PORT, () => console.log(`Cart service listening on port ${PORT}`));
