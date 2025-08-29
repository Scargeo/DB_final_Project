#!/usr/bin/env python3
"""
API Testing Script for Library Management System
This script demonstrates all the CRUD operations and API functionality
"""

import requests
import json
from datetime import date, timedelta

BASE_URL = 'http://localhost:5000'

def print_response(response, title):
    """Print formatted response"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"Status Code: {response.status_code}")
    if response.headers.get('content-type', '').startswith('application/json'):
        print(json.dumps(response.json(), indent=2))
    else:
        print(response.text[:500])

def test_api():
    """Test all API endpoints"""
    
    print("🚀 Testing Library Management System API")
    
    # Test home endpoint
    response = requests.get(f"{BASE_URL}/")
    print_response(response, "HOME ENDPOINT")
    
    # Test statistics
    response = requests.get(f"{BASE_URL}/api/stats")
    print_response(response, "INITIAL STATISTICS")
    
    # Test getting all authors
    response = requests.get(f"{BASE_URL}/api/authors")
    print_response(response, "GET ALL AUTHORS")
    
    # Test getting all books
    response = requests.get(f"{BASE_URL}/api/books")
    print_response(response, "GET ALL BOOKS (first 2)")
    if response.status_code == 200:
        books = response.json()[:2]  # Show only first 2
        print(json.dumps(books, indent=2))
    
    # Test getting all users
    response = requests.get(f"{BASE_URL}/api/users")
    print_response(response, "GET ALL USERS")
    
    # Test getting all borrowings
    response = requests.get(f"{BASE_URL}/api/borrowings")
    print_response(response, "GET ALL BORROWINGS (first 2)")
    if response.status_code == 200:
        borrowings = response.json()[:2]  # Show only first 2
        print(json.dumps(borrowings, indent=2))
    
    # Test creating a new author
    new_author = {
        "name": "Isaac Asimov",
        "biography": "American writer and professor of biochemistry, best known for his works of science fiction.",
        "birth_date": "1920-01-02"
    }
    response = requests.post(f"{BASE_URL}/api/authors", json=new_author)
    print_response(response, "CREATE NEW AUTHOR")
    author_id = response.json().get('id') if response.status_code == 201 else None
    
    # Test creating a new book for the author
    if author_id:
        new_book = {
            "title": "Foundation",
            "isbn": "9780553293357",
            "publication_date": "1951-05-01",
            "author_id": author_id,
            "copies_available": 3,
            "total_copies": 3
        }
        response = requests.post(f"{BASE_URL}/api/books", json=new_book)
        print_response(response, "CREATE NEW BOOK")
        book_id = response.json().get('id') if response.status_code == 201 else None
    
    # Test creating a new user
    new_user = {
        "name": "Sarah Connor",
        "email": "sarah.connor@email.com",
        "phone": "555-0199"
    }
    response = requests.post(f"{BASE_URL}/api/users", json=new_user)
    print_response(response, "CREATE NEW USER")
    user_id = response.json().get('id') if response.status_code == 201 else None
    
    # Test creating a borrowing
    if user_id and book_id:
        new_borrowing = {
            "user_id": user_id,
            "book_id": book_id,
            "due_date": str(date.today() + timedelta(days=14))
        }
        response = requests.post(f"{BASE_URL}/api/borrowings", json=new_borrowing)
        print_response(response, "CREATE NEW BORROWING")
        borrowing_id = response.json().get('id') if response.status_code == 201 else None
        
        # Test returning the book
        if borrowing_id:
            response = requests.put(f"{BASE_URL}/api/borrowings/{borrowing_id}/return")
            print_response(response, "RETURN BOOK")
    
    # Test getting a specific author
    if author_id:
        response = requests.get(f"{BASE_URL}/api/authors/{author_id}")
        print_response(response, f"GET AUTHOR {author_id}")
    
    # Test updating an author
    if author_id:
        update_data = {
            "biography": "American writer and professor of biochemistry, best known for his works of science fiction and popular science books."
        }
        response = requests.put(f"{BASE_URL}/api/authors/{author_id}", json=update_data)
        print_response(response, f"UPDATE AUTHOR {author_id}")
    
    # Test final statistics
    response = requests.get(f"{BASE_URL}/api/stats")
    print_response(response, "FINAL STATISTICS")
    
    print(f"\n{'='*50}")
    print("✅ API Testing Complete!")
    print(f"{'='*50}")

if __name__ == '__main__':
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API server.")
        print("Make sure the Flask application is running on http://localhost:5000")
    except Exception as e:
        print(f"❌ Error: {e}")