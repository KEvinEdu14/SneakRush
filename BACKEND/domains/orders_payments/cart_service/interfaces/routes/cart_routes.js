const express = require('express');
const CartController = require('../controllers/cart_controller');
const router = express.Router();

router.post('/:userId/items', CartController.addItem);
router.get('/:userId/items', CartController.listItems);
router.put('/:userId/items/:itemId', CartController.updateItem);
router.delete('/:userId/items/:itemId', CartController.removeItem);
router.delete('/:userId', CartController.clearCart);

module.exports = router;
