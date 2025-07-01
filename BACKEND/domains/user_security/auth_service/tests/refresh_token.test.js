const request = require('supertest');
const app = require('../app/index');

describe('POST /api/auth/refresh-token', () => {
  it('should fail with invalid token', async () => {
    const res = await request(app)
      .post('/api/auth/refresh-token')
      .send({ token: 'invalid.token.here' });

    expect(res.statusCode).toEqual(403);
  });
});
