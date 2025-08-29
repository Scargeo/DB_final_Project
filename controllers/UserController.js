const User = require('../models/User');

class UserController {
    // Get all users
    static async getAllUsers(req, res) {
        try {
            const users = await User.getAll();
            res.json({
                success: true,
                data: users,
                count: users.length
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to fetch users',
                message: error.message
            });
        }
    }

    // Get user by ID
    static async getUserById(req, res) {
        try {
            const { id } = req.params;
            const user = await User.getById(id);
            
            if (!user) {
                return res.status(404).json({
                    success: false,
                    error: 'User not found'
                });
            }

            res.json({
                success: true,
                data: user
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to fetch user',
                message: error.message
            });
        }
    }

    // Create new user
    static async createUser(req, res) {
        try {
            const { username, email } = req.body;
            
            if (!username || !email) {
                return res.status(400).json({
                    success: false,
                    error: 'Username and email are required'
                });
            }

            const userId = await User.create({ username, email });
            const newUser = await User.getById(userId);

            res.status(201).json({
                success: true,
                data: newUser,
                message: 'User created successfully'
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to create user',
                message: error.message
            });
        }
    }

    // Update user
    static async updateUser(req, res) {
        try {
            const { id } = req.params;
            const { username, email } = req.body;

            if (!username || !email) {
                return res.status(400).json({
                    success: false,
                    error: 'Username and email are required'
                });
            }

            const updated = await User.update(id, { username, email });
            
            if (!updated) {
                return res.status(404).json({
                    success: false,
                    error: 'User not found'
                });
            }

            const updatedUser = await User.getById(id);
            res.json({
                success: true,
                data: updatedUser,
                message: 'User updated successfully'
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to update user',
                message: error.message
            });
        }
    }

    // Delete user
    static async deleteUser(req, res) {
        try {
            const { id } = req.params;
            const deleted = await User.delete(id);
            
            if (!deleted) {
                return res.status(404).json({
                    success: false,
                    error: 'User not found'
                });
            }

            res.json({
                success: true,
                message: 'User deleted successfully'
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to delete user',
                message: error.message
            });
        }
    }
}

module.exports = UserController;