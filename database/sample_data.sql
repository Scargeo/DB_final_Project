-- Sample data for Library Management System
-- Insert sample authors
INSERT INTO authors (name, biography, birth_date) VALUES
('J.K. Rowling', 'British author best known for the Harry Potter series.', '1965-07-31'),
('George Orwell', 'English novelist and essayist, journalist and critic.', '1903-06-25'),
('Jane Austen', 'English novelist known for her social commentary and wit.', '1775-12-16'),
('Stephen King', 'American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels.', '1947-09-21'),
('Agatha Christie', 'English writer known for her detective novels.', '1890-09-15');

-- Insert sample books
INSERT INTO books (title, isbn, publication_date, author_id, copies_available, total_copies) VALUES
('Harry Potter and the Philosopher''s Stone', '9780747532699', '1997-06-26', 1, 3, 3),
('Harry Potter and the Chamber of Secrets', '9780747538493', '1998-07-02', 1, 2, 2),
('1984', '9780451524935', '1949-06-08', 2, 5, 5),
('Animal Farm', '9780451526342', '1945-08-17', 2, 4, 4),
('Pride and Prejudice', '9780141439518', '1813-01-28', 3, 2, 2),
('Sense and Sensibility', '9780141439662', '1811-10-30', 3, 1, 1),
('The Shining', '9780307743657', '1977-01-28', 4, 3, 3),
('It', '9781501142970', '1986-09-15', 4, 2, 2),
('Murder on the Orient Express', '9780062693662', '1934-01-01', 5, 4, 4),
('The ABC Murders', '9780008129590', '1936-01-06', 5, 3, 3);

-- Insert sample users
INSERT INTO users (name, email, phone, registration_date) VALUES
('Alice Johnson', 'alice.johnson@email.com', '555-0101', '2023-01-15'),
('Bob Smith', 'bob.smith@email.com', '555-0102', '2023-02-20'),
('Carol Davis', 'carol.davis@email.com', '555-0103', '2023-03-10'),
('David Wilson', 'david.wilson@email.com', '555-0104', '2023-04-05'),
('Emma Brown', 'emma.brown@email.com', '555-0105', '2023-05-12');

-- Insert sample borrowings
INSERT INTO borrowings (user_id, book_id, borrow_date, due_date, status) VALUES
(1, 1, '2024-01-15', '2024-02-15', 'borrowed'),
(1, 3, '2024-01-20', '2024-02-20', 'returned'),
(2, 2, '2024-01-25', '2024-02-25', 'borrowed'),
(3, 5, '2024-02-01', '2024-03-01', 'returned'),
(4, 7, '2024-02-10', '2024-03-10', 'borrowed'),
(5, 9, '2024-02-15', '2024-03-15', 'borrowed');

-- Update return_date for returned books
UPDATE borrowings SET return_date = '2024-02-18' WHERE id = 2;
UPDATE borrowings SET return_date = '2024-02-28' WHERE id = 4;