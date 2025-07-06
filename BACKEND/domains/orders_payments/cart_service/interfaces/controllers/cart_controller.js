const AddItemUseCase = require('../../application/use_cases/add_item');
const ListItemsUseCase = require('../../application/use_cases/list_items');
const UpdateItemUseCase = require('../../application/use_cases/update_item');
const RemoveItemUseCase = require('../../application/use_cases/remove_item');
const ClearCartUseCase = require('../../application/use_cases/clear_cart');

class CartController {
    static async addItem(req, res, next) {
        try {
            const { userId } = req.params;
            const item = await AddItemUseCase.execute(userId, req.body);
            res.status(201).json(item);
        } catch (err) {
            next(err);
        }
    }
    static async listItems(req, res, next) {
        try {
            const items = await ListItemsUseCase.execute(req.params.userId);
            res.json(items);
        } catch (err) {
            next(err);
        }
    }
    static async updateItem(req, res, next) {
        try {
            const { userId, itemId } = req.params;
            const item = await UpdateItemUseCase.execute(userId, itemId, req.body);
            if (!item) return res.status(404).json({ message: 'Item not found' });
            res.json(item);
        } catch (err) {
            next(err);
        }
    }
    static async removeItem(req, res, next) {
        try {
            const { userId, itemId } = req.params;
            const item = await RemoveItemUseCase.execute(userId, itemId);
            if (!item) return res.status(404).json({ message: 'Item not found' });
            res.json(item);
        } catch (err) {
            next(err);
        }
    }
    static async clearCart(req, res, next) {
        try {
            const items = await ClearCartUseCase.execute(req.params.userId);
            res.json(items);
        } catch (err) {
            next(err);
        }
    }
}
module.exports = CartController;
