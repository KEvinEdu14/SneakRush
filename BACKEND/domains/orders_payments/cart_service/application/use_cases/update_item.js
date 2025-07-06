const CartRepository = require('../../infrastructure/repositories/cart_repo');
class UpdateItemUseCase {
    static async execute(userId, itemId, { quantity }) {
        const items = await CartRepository.listItems(userId);
        const existing = items.find(i => i.id === itemId);
        if (!existing) return null;
        existing.quantity = quantity;
        return CartRepository.updateItem(userId, existing);
    }
}
module.exports = UpdateItemUseCase;
