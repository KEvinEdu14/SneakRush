const CartRepository = require('../../infrastructure/repositories/cart_repo');
class ClearCartUseCase {
    static async execute(userId) {
        await CartRepository.clearCart(userId);
        return [];
    }
}
module.exports = ClearCartUseCase;
