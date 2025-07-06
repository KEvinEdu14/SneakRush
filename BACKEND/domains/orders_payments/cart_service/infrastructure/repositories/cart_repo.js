const redis = require('../../config/redis');
class CartRepository {
    static async listItems(userId) {
        const data = await redis.hgetall(`cart:${userId}`);
        return Object.entries(data).map(([id, json]) => JSON.parse(json));
    }
    static async addItem(userId, item) {
        await redis.hset(`cart:${userId}`, item.id, JSON.stringify(item));
        return item;
    }
    static async updateItem(userId, item) {
        const exists = await redis.hexists(`cart:${userId}`, item.id);
        if (!exists) return null;
        await redis.hset(`cart:${userId}`, item.id, JSON.stringify(item));
        return item;
    }
    static async removeItem(userId, itemId) {
        const json = await redis.hget(`cart:${userId}`, itemId);
        if (!json) return null;
        await redis.hdel(`cart:${userId}`, itemId);
        return JSON.parse(json);
    }
    static async clearCart(userId) {
        await redis.del(`cart:${userId}`);
        return true;
    }
}
module.exports = CartRepository;
