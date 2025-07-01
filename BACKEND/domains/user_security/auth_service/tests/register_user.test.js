const request = require('supertest');
const app = require('../app/index'); // asegúrate de exportarlo en index.js

describe('POST /api/auth/register', () => {
  it('should return 201 on successful registration', async () => {
    const res = await request(app)
      .post('/api/auth/register')
      .send({
        email: `test${Date.now()}@example.com`,
        password: 'password123'
      });

    expect(res.statusCode).toEqual(201);
    expect(res.body).toHaveProperty('message');
  });
});
