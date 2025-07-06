const CartRepository = require('../../infrastructure/repositories/cart_repo');
class ListItemsUseCase {
    static async execute(userId) {
        return CartRepository.listItems(userId);
    }
}
module.exports = ListItemsUseCase;
