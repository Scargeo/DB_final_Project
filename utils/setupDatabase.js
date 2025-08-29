const User = require('../models/User');
const { testConnection } = require('../config/database');

async function setupDatabase() {
    console.log('Setting up database...');
    
    try {
        // Test database connection
        const connected = await testConnection();
        if (!connected) {
            throw new Error('Database connection failed');
        }

        // Create tables
        console.log('Creating users table...');
        await User.createTable();
        console.log('Users table created successfully');

        console.log('Database setup completed successfully!');
    } catch (error) {
        console.error('Database setup failed:', error.message);
        process.exit(1);
    }
}

// Run setup if called directly
if (require.main === module) {
    setupDatabase();
}

module.exports = setupDatabase;