const { v4: uuidv4 } = require('uuid');
const CartRepository = require('../../infrastructure/repositories/cart_repo');
const AuthClient = require('../../interfaces/clients/auth_client');
class AddItemUseCase {
    static async execute(userId, { productId, quantity }) {
        const user = await AuthClient.getUser(userId);
        if (!user) throw new Error('User not found');
        const item = { id: uuidv4(), userId, productId, quantity };
        return CartRepository.addItem(userId, item);
    }
}
module.exports = AddItemUseCase;
