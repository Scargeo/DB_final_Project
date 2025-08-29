#!/usr/bin/env python3
"""
Database initialization script for Library Management System
"""

import sqlite3
import os
from datetime import datetime

def init_database():
    """Initialize the database with schema and sample data"""
    
    # Database file path
    db_path = 'library.db'
    
    # Remove existing database if it exists
    if os.path.exists(db_path):
        os.remove(db_path)
        print(f"Removed existing database: {db_path}")
    
    # Connect to database (creates new file)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Read and execute schema
        with open('database/schema.sql', 'r') as f:
            schema_sql = f.read()
        
        cursor.executescript(schema_sql)
        print("Database schema created successfully")
        
        # Read and execute sample data
        with open('database/sample_data.sql', 'r') as f:
            data_sql = f.read()
        
        cursor.executescript(data_sql)
        print("Sample data inserted successfully")
        
        # Commit changes
        conn.commit()
        print(f"Database initialized successfully: {db_path}")
        
        # Show some statistics
        cursor.execute("SELECT COUNT(*) FROM authors")
        author_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM books") 
        book_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM borrowings")
        borrowing_count = cursor.fetchone()[0]
        
        print(f"\nDatabase Statistics:")
        print(f"- Authors: {author_count}")
        print(f"- Books: {book_count}")
        print(f"- Users: {user_count}")
        print(f"- Borrowings: {borrowing_count}")
        
    except Exception as e:
        print(f"Error initializing database: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == '__main__':
    init_database()