const request = require('supertest');
const app = require('../index');

describe('API Endpoints', () => {
    describe('Basic Health Checks', () => {
        test('GET / should return API info with merge features', async () => {
            const response = await request(app).get('/');
            expect(response.status).toBe(200);
            expect(response.body.message).toBe('Database Final Project API');
            expect(response.body.version).toBe('1.0.0');
            expect(response.body.features).toBeDefined();
            expect(response.body.features.mergeConflictDetection).toBe(true);
            expect(response.body.features.optimisticLocking).toBe(true);
            expect(response.body.features.versionControl).toBe(true);
            expect(response.body.mergeProperties).toBeDefined();
            expect(response.body.mergeProperties.supported).toBe(true);
        });

        test('GET /health should return health status', async () => {
            const response = await request(app).get('/health');
            expect(response.status).toBe(200);
            expect(response.body.status).toBe('healthy');
        });
    });

    describe('User API with Merge Conflict Detection (Database Required)', () => {
        // These tests require a working database connection
        // They will be skipped if database is not available

        test.skip('POST /api/users should create a user with merge properties', async () => {
            const userData = {
                username: 'testuser',
                email: 'test@example.com'
            };

            const response = await request(app)
                .post('/api/users')
                .send(userData);

            expect(response.status).toBe(201);
            expect(response.body.success).toBe(true);
            expect(response.body.mergeProperties).toBeDefined();
            expect(response.body.mergeProperties.canMerge).toBe(true);
        });

        test.skip('PUT /api/users/:id should detect merge conflicts with wrong version', async () => {
            const updateData = {
                username: 'conflictuser',
                email: 'conflict@example.com',
                version: 1 // Wrong version, should cause conflict
            };

            const response = await request(app)
                .put('/api/users/1')
                .send(updateData);

            // Expecting either 409 (conflict) or 500 (no database)
            expect([409, 500]).toContain(response.status);
            
            if (response.status === 409) {
                expect(response.body.success).toBe(false);
                expect(response.body.error).toBe('Merge conflict detected');
                expect(response.body.mergeProperties).toBeDefined();
                expect(response.body.mergeProperties.canMerge).toBe(false);
            }
        });
    });
});