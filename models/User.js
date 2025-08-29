const { executeQuery } = require('../config/database');

class User {
    constructor(id, username, email, created_at = null) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.created_at = created_at;
    }

    // Create users table
    static async createTable() {
        const query = `
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        `;
        return await executeQuery(query);
    }

    // Get all users
    static async getAll() {
        const query = 'SELECT * FROM users ORDER BY created_at DESC';
        return await executeQuery(query);
    }

    // Get user by ID
    static async getById(id) {
        const query = 'SELECT * FROM users WHERE id = ?';
        const results = await executeQuery(query, [id]);
        return results.length > 0 ? results[0] : null;
    }

    // Create new user
    static async create(userData) {
        const query = 'INSERT INTO users (username, email) VALUES (?, ?)';
        const result = await executeQuery(query, [userData.username, userData.email]);
        return result.insertId;
    }

    // Update user
    static async update(id, userData) {
        const query = 'UPDATE users SET username = ?, email = ? WHERE id = ?';
        const result = await executeQuery(query, [userData.username, userData.email, id]);
        return result.affectedRows > 0;
    }

    // Delete user
    static async delete(id) {
        const query = 'DELETE FROM users WHERE id = ?';
        const result = await executeQuery(query, [id]);
        return result.affectedRows > 0;
    }
}

module.exports = User;