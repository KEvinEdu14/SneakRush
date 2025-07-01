const request = require('supertest');
const app = require('../app/index');

describe('POST /api/auth/login', () => {
  it('should fail with invalid credentials', async () => {
    const res = await request(app)
      .post('/api/auth/login')
      .send({ email: 'fake@example.com', password: 'wrongpass' });

    expect(res.statusCode).toEqual(401);
  });
});
