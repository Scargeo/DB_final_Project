const express = require('express');
const UserController = require('../controllers/UserController');

const router = express.Router();

// User routes
router.get('/', UserController.getAllUsers);
router.get('/:id', UserController.getUserById);
router.get('/:id/conflicts', UserController.checkConflicts);
router.post('/', UserController.createUser);
router.put('/:id', UserController.updateUser);
router.delete('/:id', UserController.deleteUser);

module.exports = router;