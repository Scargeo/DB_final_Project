-- Library Management System Database Schema
-- Final Database Project

-- Create Authors table
CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    biography TEXT,
    birth_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Books table
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    isbn VARCHAR(13) UNIQUE,
    publication_date DATE,
    author_id INTEGER NOT NULL,
    copies_available INTEGER DEFAULT 1,
    total_copies INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

-- Create Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    registration_date DATE DEFAULT CURRENT_DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Create Borrowings table
CREATE TABLE borrowings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    borrow_date DATE DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'borrowed', -- 'borrowed', 'returned', 'overdue'
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

-- Create indexes for better performance
CREATE INDEX idx_books_author_id ON books(author_id);
CREATE INDEX idx_books_isbn ON books(isbn);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_borrowings_user_id ON borrowings(user_id);
CREATE INDEX idx_borrowings_book_id ON borrowings(book_id);
CREATE INDEX idx_borrowings_status ON borrowings(status);