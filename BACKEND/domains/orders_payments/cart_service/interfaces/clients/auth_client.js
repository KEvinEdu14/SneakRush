const axios = require('axios');
const AUTH_SERVICE_URL = process.env.AUTH_SERVICE_URL;
class AuthClient {
    static async getUser(userId) {
        const response = await axios.get(`${AUTH_SERVICE_URL}/users/${userId}`);
        return response.data;
    }
}
module.exports = AuthClient;
