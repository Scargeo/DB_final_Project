const User = require('../models/User');

class UserController {
    // Get all users
    static async getAllUsers(req, res) {
        try {
            const users = await User.getAll();
            res.json({
                success: true,
                data: users,
                count: users.length,
                mergeProperties: {
                    canMerge: true,
                    conflictResolution: 'last-write-wins',
                    versionControl: 'enabled'
                }
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
                data: user,
                mergeProperties: {
                    version: user.version,
                    lastModified: user.last_modified,
                    canMerge: true,
                    conflictResolution: 'optimistic-locking'
                }
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
                message: 'User created successfully',
                mergeProperties: {
                    version: newUser.version,
                    lastModified: newUser.last_modified,
                    canMerge: true,
                    conflictResolution: 'none-required'
                }
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to create user',
                message: error.message
            });
        }
    }

    // Update user with conflict detection
    static async updateUser(req, res) {
        try {
            const { id } = req.params;
            const { username, email, version } = req.body;

            if (!username || !email) {
                return res.status(400).json({
                    success: false,
                    error: 'Username and email are required'
                });
            }

            // Check for merge conflicts first
            if (version !== undefined) {
                const conflictCheck = await User.checkMergeConflicts(id, { username, email }, version);
                if (conflictCheck.hasConflict) {
                    return res.status(409).json({
                        success: false,
                        error: 'Merge conflict detected',
                        message: conflictCheck.reason,
                        conflictDetails: {
                            currentVersion: conflictCheck.currentVersion,
                            expectedVersion: conflictCheck.expectedVersion,
                            currentData: conflictCheck.currentData
                        },
                        mergeProperties: {
                            canMerge: false,
                            conflictResolution: 'manual-required',
                            conflictReason: conflictCheck.reason
                        }
                    });
                }
            }

            const updated = await User.update(id, { username, email }, version);
            
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
                message: 'User updated successfully',
                mergeProperties: {
                    version: updatedUser.version,
                    lastModified: updatedUser.last_modified,
                    canMerge: true,
                    conflictResolution: 'resolved',
                    previousVersion: version || 'unknown'
                }
            });
        } catch (error) {
            if (error.message.includes('Merge conflict detected')) {
                return res.status(409).json({
                    success: false,
                    error: 'Merge conflict',
                    message: error.message,
                    mergeProperties: {
                        canMerge: false,
                        conflictResolution: 'version-mismatch'
                    }
                });
            }

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
                message: 'User deleted successfully',
                mergeProperties: {
                    canMerge: true,
                    conflictResolution: 'none-required',
                    operation: 'delete'
                }
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to delete user',
                message: error.message
            });
        }
    }

    // Check for merge conflicts
    static async checkConflicts(req, res) {
        try {
            const { id } = req.params;
            const { username, email, version } = req.query;
            
            if (!username || !email) {
                return res.status(400).json({
                    success: false,
                    error: 'Username and email are required for conflict checking'
                });
            }

            const conflictCheck = await User.checkMergeConflicts(
                id, 
                { username, email }, 
                version ? parseInt(version) : null
            );

            res.json({
                success: true,
                data: conflictCheck,
                message: conflictCheck.hasConflict ? 'Conflicts detected' : 'No conflicts found'
            });
        } catch (error) {
            res.status(500).json({
                success: false,
                error: 'Failed to check conflicts',
                message: error.message
            });
        }
    }
}

module.exports = UserController;