const CartRepository = require('../../infrastructure/repositories/cart_repo');
class RemoveItemUseCase {
    static async execute(userId, itemId) {
        return CartRepository.removeItem(userId, itemId);
    }
}
module.exports = RemoveItemUseCase;
