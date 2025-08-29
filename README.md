# Library Management System - Database Final Project

A complete database-driven web application for managing a library system with full CRUD operations and RESTful APIs.

## 🚀 Features

- **Complete Database Schema**: Authors, Books, Users, and Borrowings with proper relationships
- **RESTful API**: Full CRUD operations for all entities
- **Data Validation**: Input validation and error handling
- **Relationship Management**: Foreign key constraints and cascading deletes
- **Statistics**: Library statistics and reporting
- **Sample Data**: Pre-populated with sample authors, books, and users

## 📊 Database Schema

### Tables:
- **Authors**: Store author information with biography and birth dates
- **Books**: Book catalog with ISBN, publication dates, and inventory tracking
- **Users**: Library member registration and contact information  
- **Borrowings**: Track book loans, due dates, and return status

### Relationships:
- Authors have many Books (1:N)
- Users have many Borrowings (1:N) 
- Books have many Borrowings (1:N)
- Books belong to Authors (N:1)

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (easily upgradeable to PostgreSQL/MySQL)
- **ORM**: SQLAlchemy
- **Serialization**: Marshmallow
- **API**: RESTful JSON APIs
- **CORS**: Enabled for frontend integration

## 📁 Project Structure

```
DB_final_Project/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── init_db.py            # Database initialization script
├── api/
│   ├── __init__.py
│   └── routes.py         # API endpoints
├── database/
│   ├── schema.sql        # Database schema
│   └── sample_data.sql   # Sample data
├── static/               # Static files (CSS, JS)
└── templates/           # HTML templates
```

## 🚀 Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone <repository-url>
cd DB_final_Project

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Initialize Database

```bash
# Initialize database with schema and sample data
python init_db.py
```

### 3. Run the Application

```bash
# Start the Flask development server
python app.py
```

The API will be available at `http://localhost:5000`

## 📚 API Documentation

### Base URL: `http://localhost:5000`

### Authors API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/authors` | Get all authors |
| GET | `/api/authors/{id}` | Get specific author |
| POST | `/api/authors` | Create new author |
| PUT | `/api/authors/{id}` | Update author |
| DELETE | `/api/authors/{id}` | Delete author |

**Author Object:**
```json
{
  "id": 1,
  "name": "J.K. Rowling",
  "biography": "British author best known for the Harry Potter series.",
  "birth_date": "1965-07-31",
  "created_at": "2024-01-01T00:00:00"
}
```

### Books API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/books` | Get all books |
| GET | `/api/books/{id}` | Get specific book |
| POST | `/api/books` | Create new book |
| PUT | `/api/books/{id}` | Update book |
| DELETE | `/api/books/{id}` | Delete book |

**Book Object:**
```json
{
  "id": 1,
  "title": "Harry Potter and the Philosopher's Stone",
  "isbn": "9780747532699",
  "publication_date": "1997-06-26",
  "author_id": 1,
  "copies_available": 3,
  "total_copies": 3,
  "author": {
    "id": 1,
    "name": "J.K. Rowling"
  }
}
```

### Users API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/users` | Get all users |
| GET | `/api/users/{id}` | Get specific user |
| POST | `/api/users` | Create new user |
| PUT | `/api/users/{id}` | Update user |
| DELETE | `/api/users/{id}` | Delete user |

**User Object:**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice.johnson@email.com",
  "phone": "555-0101",
  "registration_date": "2023-01-15"
}
```

### Borrowings API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/borrowings` | Get all borrowings |
| GET | `/api/borrowings/{id}` | Get specific borrowing |
| POST | `/api/borrowings` | Create new borrowing |
| PUT | `/api/borrowings/{id}` | Update borrowing |
| PUT | `/api/borrowings/{id}/return` | Return a book |

**Borrowing Object:**
```json
{
  "id": 1,
  "user_id": 1,
  "book_id": 1,
  "borrow_date": "2024-01-15",
  "due_date": "2024-02-15", 
  "return_date": null,
  "status": "borrowed"
}
```

### Statistics API

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/stats` | Get library statistics |

## 📝 Example API Usage

### Create a new author:
```bash
curl -X POST http://localhost:5000/api/authors \
  -H "Content-Type: application/json" \
  -d '{
    "name": "J.R.R. Tolkien",
    "biography": "English author and scholar, best known for The Hobbit and The Lord of the Rings.",
    "birth_date": "1892-01-03"
  }'
```

### Create a new book:
```bash
curl -X POST http://localhost:5000/api/books \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The Hobbit",
    "isbn": "9780547928227",
    "publication_date": "1937-09-21",
    "author_id": 6,
    "copies_available": 2,
    "total_copies": 2
  }'
```

### Borrow a book:
```bash
curl -X POST http://localhost:5000/api/borrowings \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "book_id": 1,
    "due_date": "2024-03-15"
  }'
```

### Return a book:
```bash
curl -X PUT http://localhost:5000/api/borrowings/1/return
```

## 🧪 Testing

You can test the API using:
- **cURL** commands (examples above)
- **Postman** collection
- **Python requests** library
- **Frontend application**

## 🔧 Configuration

- **Database**: SQLite file (`library.db`) - easily configurable to PostgreSQL/MySQL
- **CORS**: Enabled for cross-origin requests
- **Debug Mode**: Enabled in development
- **Secret Key**: Configure for production use

## 📈 Future Enhancements

- User authentication and authorization
- Book categories and genres
- Advanced search and filtering
- Email notifications for overdue books
- Book reservations
- Fine calculation for overdue books
- Admin dashboard
- Frontend web application

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is created for educational purposes as a database final project.