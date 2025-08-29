# Database Final Project - Node.js Implementation

A comprehensive database application built with Node.js, Express, and MySQL for handling database operations with a RESTful API.

## Features

- RESTful API with Express.js
- MySQL database integration with connection pooling
- User management system (CRUD operations)
- Environment-based configuration
- Comprehensive error handling
- Automated testing with Jest
- Development tools with Nodemon

## Project Structure

```
├── config/
│   └── database.js         # Database configuration and connection
├── controllers/
│   └── UserController.js   # User-related business logic
├── models/
│   └── User.js             # User data model and database operations
├── routes/
│   └── users.js            # User API routes
├── tests/
│   └── api.test.js         # API endpoint tests
├── utils/
│   └── setupDatabase.js    # Database setup and initialization
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore patterns
├── index.js                # Main application entry point
└── package.json            # Project dependencies and scripts
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd DB_final_Project
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

4. Set up the database:
```bash
npm run setup
```

## Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=final_project_db

# Server Configuration
PORT=3000
NODE_ENV=development
```

## Usage

### Development Mode
```bash
npm run dev
```

### Production Mode
```bash
npm start
```

### Run Tests
```bash
npm test
```

### Database Setup
```bash
npm run setup
```

## API Endpoints

### Base URL
```
http://localhost:3000
```

### Endpoints

#### General
- `GET /` - API information
- `GET /health` - Health check
- `GET /db-test` - Database connection test

#### Users
- `GET /api/users` - Get all users
- `GET /api/users/:id` - Get user by ID
- `POST /api/users` - Create new user
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

### Example API Usage

#### Create a User
```bash
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "email": "john@example.com"}'
```

#### Get All Users
```bash
curl http://localhost:3000/api/users
```

#### Get User by ID
```bash
curl http://localhost:3000/api/users/1
```

#### Update User
```bash
curl -X PUT http://localhost:3000/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"username": "john_updated", "email": "john.updated@example.com"}'
```

#### Delete User
```bash
curl -X DELETE http://localhost:3000/api/users/1
```

## Technologies Used

- **Node.js** - JavaScript runtime
- **Express.js** - Web framework
- **MySQL2** - MySQL database driver with Promise support
- **dotenv** - Environment variable management
- **CORS** - Cross-Origin Resource Sharing
- **Jest** - Testing framework
- **Supertest** - HTTP assertion library for testing
- **Nodemon** - Development server with auto-restart

## Development Guidelines

1. **Code Style**: Follow standard JavaScript conventions
2. **Error Handling**: Always use try-catch blocks for async operations
3. **Database Queries**: Use parameterized queries to prevent SQL injection
4. **Environment Variables**: Never commit sensitive data like passwords
5. **Testing**: Write tests for all API endpoints

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

ISC