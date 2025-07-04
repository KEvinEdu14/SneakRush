const request = require('supertest');
const app = require('../src/app');

describe('POST /api/2fa/validate', () => {
  it('should return 400 if missing params', async () => {
    const res = await request(app).post('/api/2fa/validate').send({});
    expect(res.statusCode).toBe(400);
  });
});
