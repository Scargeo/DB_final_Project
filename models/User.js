const { executeQuery } = require('../config/database');

class User {
    constructor(id, username, email, created_at = null, version = 1, last_modified = null) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.created_at = created_at;
        this.version = version;
        this.last_modified = last_modified;
    }

    // Create users table
    static async createTable() {
        const query = `
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                version INT DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
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

    // Update user with optimistic locking
    static async update(id, userData, expectedVersion = null) {
        // If version is provided, check for conflicts (optimistic locking)
        if (expectedVersion !== null) {
            const currentUser = await this.getById(id);
            if (!currentUser) {
                throw new Error('User not found');
            }
            
            if (currentUser.version !== expectedVersion) {
                throw new Error(`Merge conflict detected. Expected version ${expectedVersion}, but current version is ${currentUser.version}. Please refresh and try again.`);
            }
        }
        
        const query = 'UPDATE users SET username = ?, email = ?, version = version + 1 WHERE id = ?';
        const result = await executeQuery(query, [userData.username, userData.email, id]);
        return result.affectedRows > 0;
    }

    // Delete user
    static async delete(id) {
        const query = 'DELETE FROM users WHERE id = ?';
        const result = await executeQuery(query, [id]);
        return result.affectedRows > 0;
    }

    // Check for conflicts before merge
    static async checkMergeConflicts(id, userData, expectedVersion) {
        const currentUser = await this.getById(id);
        if (!currentUser) {
            return { hasConflict: true, reason: 'User not found' };
        }

        if (expectedVersion && currentUser.version !== expectedVersion) {
            return { 
                hasConflict: true, 
                reason: 'Version mismatch',
                currentVersion: currentUser.version,
                expectedVersion: expectedVersion,
                currentData: currentUser
            };
        }

        // Check for field-level conflicts
        const conflicts = [];
        if (currentUser.username !== userData.username) {
            conflicts.push('username');
        }
        if (currentUser.email !== userData.email) {
            conflicts.push('email');
        }

        return {
            hasConflict: false,
            conflicts: conflicts,
            mergeProperties: {
                id: currentUser.id,
                version: currentUser.version,
                lastModified: currentUser.last_modified,
                canMerge: true
            }
        };
    }
}

module.exports = User;