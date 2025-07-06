class CartItem {
    constructor(id, userId, productId, quantity) {
        this.id = id;
        this.userId = userId;
        this.productId = productId;
        this.quantity = quantity;
    }
}
module.exports = CartItem;
