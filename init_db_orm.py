#!/usr/bin/env python3
"""
Database initialization script using SQLAlchemy ORM
This ensures compatibility between the data and the Flask application
"""

from app import app, db, Author, Book, User, Borrowing
from datetime import datetime, date, timedelta
import os

def init_database():
    """Initialize the database with sample data using SQLAlchemy ORM"""
    
    with app.app_context():
        # Drop and recreate all tables
        db.drop_all()
        db.create_all()
        
        print("Database tables created successfully")
        
        # Create sample authors
        authors_data = [
            {
                'name': 'J.K. Rowling',
                'biography': 'British author best known for the Harry Potter series.',
                'birth_date': date(1965, 7, 31)
            },
            {
                'name': 'George Orwell',
                'biography': 'English novelist and essayist, journalist and critic.',
                'birth_date': date(1903, 6, 25)
            },
            {
                'name': 'Jane Austen',
                'biography': 'English novelist known for her social commentary and wit.',
                'birth_date': date(1775, 12, 16)
            },
            {
                'name': 'Stephen King',
                'biography': 'American author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels.',
                'birth_date': date(1947, 9, 21)
            },
            {
                'name': 'Agatha Christie',
                'biography': 'English writer known for her detective novels.',
                'birth_date': date(1890, 9, 15)
            }
        ]
        
        authors = []
        for author_data in authors_data:
            author = Author(**author_data)
            db.session.add(author)
            authors.append(author)
        
        db.session.commit()
        print(f"Created {len(authors)} authors")
        
        # Create sample books
        books_data = [
            {
                'title': "Harry Potter and the Philosopher's Stone",
                'isbn': '9780747532699',
                'publication_date': date(1997, 6, 26),
                'author_id': 1,
                'copies_available': 3,
                'total_copies': 3
            },
            {
                'title': 'Harry Potter and the Chamber of Secrets',
                'isbn': '9780747538493',
                'publication_date': date(1998, 7, 2),
                'author_id': 1,
                'copies_available': 2,
                'total_copies': 2
            },
            {
                'title': '1984',
                'isbn': '9780451524935',
                'publication_date': date(1949, 6, 8),
                'author_id': 2,
                'copies_available': 5,
                'total_copies': 5
            },
            {
                'title': 'Animal Farm',
                'isbn': '9780451526342',
                'publication_date': date(1945, 8, 17),
                'author_id': 2,
                'copies_available': 4,
                'total_copies': 4
            },
            {
                'title': 'Pride and Prejudice',
                'isbn': '9780141439518',
                'publication_date': date(1813, 1, 28),
                'author_id': 3,
                'copies_available': 2,
                'total_copies': 2
            },
            {
                'title': 'Sense and Sensibility',
                'isbn': '9780141439662',
                'publication_date': date(1811, 10, 30),
                'author_id': 3,
                'copies_available': 1,
                'total_copies': 1
            },
            {
                'title': 'The Shining',
                'isbn': '9780307743657',
                'publication_date': date(1977, 1, 28),
                'author_id': 4,
                'copies_available': 3,
                'total_copies': 3
            },
            {
                'title': 'It',
                'isbn': '9781501142970',
                'publication_date': date(1986, 9, 15),
                'author_id': 4,
                'copies_available': 2,
                'total_copies': 2
            },
            {
                'title': 'Murder on the Orient Express',
                'isbn': '9780062693662',
                'publication_date': date(1934, 1, 1),
                'author_id': 5,
                'copies_available': 4,
                'total_copies': 4
            },
            {
                'title': 'The ABC Murders',
                'isbn': '9780008129590',
                'publication_date': date(1936, 1, 6),
                'author_id': 5,
                'copies_available': 3,
                'total_copies': 3
            }
        ]
        
        books = []
        for book_data in books_data:
            book = Book(**book_data)
            db.session.add(book)
            books.append(book)
        
        db.session.commit()
        print(f"Created {len(books)} books")
        
        # Create sample users
        users_data = [
            {
                'name': 'Alice Johnson',
                'email': 'alice.johnson@email.com',
                'phone': '555-0101',
                'registration_date': date(2023, 1, 15)
            },
            {
                'name': 'Bob Smith',
                'email': 'bob.smith@email.com',
                'phone': '555-0102',
                'registration_date': date(2023, 2, 20)
            },
            {
                'name': 'Carol Davis',
                'email': 'carol.davis@email.com',
                'phone': '555-0103',
                'registration_date': date(2023, 3, 10)
            },
            {
                'name': 'David Wilson',
                'email': 'david.wilson@email.com',
                'phone': '555-0104',
                'registration_date': date(2023, 4, 5)
            },
            {
                'name': 'Emma Brown',
                'email': 'emma.brown@email.com',
                'phone': '555-0105',
                'registration_date': date(2023, 5, 12)
            }
        ]
        
        users = []
        for user_data in users_data:
            user = User(**user_data)
            db.session.add(user)
            users.append(user)
        
        db.session.commit()
        print(f"Created {len(users)} users")
        
        # Create sample borrowings
        borrowings_data = [
            {
                'user_id': 1,
                'book_id': 1,
                'borrow_date': date(2024, 1, 15),
                'due_date': date(2024, 2, 15),
                'status': 'borrowed'
            },
            {
                'user_id': 1,
                'book_id': 3,
                'borrow_date': date(2024, 1, 20),
                'due_date': date(2024, 2, 20),
                'return_date': date(2024, 2, 18),
                'status': 'returned'
            },
            {
                'user_id': 2,
                'book_id': 2,
                'borrow_date': date(2024, 1, 25),
                'due_date': date(2024, 2, 25),
                'status': 'borrowed'
            },
            {
                'user_id': 3,
                'book_id': 5,
                'borrow_date': date(2024, 2, 1),
                'due_date': date(2024, 3, 1),
                'return_date': date(2024, 2, 28),
                'status': 'returned'
            },
            {
                'user_id': 4,
                'book_id': 7,
                'borrow_date': date(2024, 2, 10),
                'due_date': date(2024, 3, 10),
                'status': 'borrowed'
            },
            {
                'user_id': 5,
                'book_id': 9,
                'borrow_date': date(2024, 2, 15),
                'due_date': date(2024, 3, 15),
                'status': 'borrowed'
            }
        ]
        
        borrowings = []
        for borrowing_data in borrowings_data:
            borrowing = Borrowing(**borrowing_data)
            db.session.add(borrowing)
            borrowings.append(borrowing)
        
        db.session.commit()
        print(f"Created {len(borrowings)} borrowings")
        
        # Show statistics
        print(f"\nDatabase Statistics:")
        print(f"- Authors: {Author.query.count()}")
        print(f"- Books: {Book.query.count()}")
        print(f"- Users: {User.query.count()}")
        print(f"- Borrowings: {Borrowing.query.count()}")
        print(f"- Active Borrowings: {Borrowing.query.filter_by(status='borrowed').count()}")
        
        print("\nDatabase initialized successfully with SQLAlchemy ORM!")

if __name__ == '__main__':
    init_database()