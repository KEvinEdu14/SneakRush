const request = require('supertest');
const app = require('../src/app');

describe('POST /send', () => {
  it('400 if body missing', async () => {
    const res = await request(app).post('/send').send({});
    expect(res.statusCode).toBe(400);
  });

  it('200 if ok', async () => {
    const res = await request(app)
      .post('/send')
      .send({ to: 'demo@mail.com', message: 'Hi' });
    expect(res.statusCode).toBe(200);
    expect(res.body.sent).toBe(true);
  });
});
