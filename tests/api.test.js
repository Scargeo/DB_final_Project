const request = require('supertest');
const app = require('../index');

describe('API Endpoints', () => {
    test('GET / should return API info', async () => {
        const response = await request(app).get('/');
        expect(response.status).toBe(200);
        expect(response.body.message).toBe('Database Final Project API');
        expect(response.body.version).toBe('1.0.0');
    });

    test('GET /health should return health status', async () => {
        const response = await request(app).get('/health');
        expect(response.status).toBe(200);
        expect(response.body.status).toBe('healthy');
    });
});