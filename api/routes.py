from flask import request, jsonify
from app import app, db, Author, Book, User, Borrowing
from app import author_schema, authors_schema, book_schema, books_schema
from app import user_schema, users_schema, borrowing_schema, borrowings_schema
from datetime import datetime, date, timedelta

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Home route
@app.route('/')
def index():
    return jsonify({
        'message': 'Library Management System API',
        'version': '1.0',
        'endpoints': {
            'authors': '/api/authors',
            'books': '/api/books', 
            'users': '/api/users',
            'borrowings': '/api/borrowings'
        }
    })

# AUTHOR ROUTES
@app.route('/api/authors', methods=['GET'])
def get_authors():
    """Get all authors"""
    authors = Author.query.all()
    return jsonify(authors_schema.dump(authors))

@app.route('/api/authors/<int:id>', methods=['GET'])
def get_author(id):
    """Get a specific author"""
    author = Author.query.get_or_404(id)
    return jsonify(author_schema.dump(author))

@app.route('/api/authors', methods=['POST'])
def create_author():
    """Create a new author"""
    try:
        data = request.get_json()
        
        # Parse birth_date if provided
        if 'birth_date' in data and data['birth_date']:
            data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        
        author = Author(
            name=data['name'],
            biography=data.get('biography'),
            birth_date=data.get('birth_date')
        )
        
        db.session.add(author)
        db.session.commit()
        
        return jsonify(author_schema.dump(author)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/authors/<int:id>', methods=['PUT'])
def update_author(id):
    """Update an existing author"""
    try:
        author = Author.query.get_or_404(id)
        data = request.get_json()
        
        author.name = data.get('name', author.name)
        author.biography = data.get('biography', author.biography)
        
        if 'birth_date' in data and data['birth_date']:
            author.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        
        db.session.commit()
        return jsonify(author_schema.dump(author))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/authors/<int:id>', methods=['DELETE'])
def delete_author(id):
    """Delete an author"""
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return jsonify({'message': 'Author deleted successfully'})

# BOOK ROUTES
@app.route('/api/books', methods=['GET'])
def get_books():
    """Get all books"""
    books = Book.query.all()
    return jsonify(books_schema.dump(books))

@app.route('/api/books/<int:id>', methods=['GET'])
def get_book(id):
    """Get a specific book"""
    book = Book.query.get_or_404(id)
    return jsonify(book_schema.dump(book))

@app.route('/api/books', methods=['POST'])
def create_book():
    """Create a new book"""
    try:
        data = request.get_json()
        
        # Validate author exists
        author = Author.query.get(data['author_id'])
        if not author:
            return jsonify({'error': 'Author not found'}), 400
        
        # Parse publication_date if provided
        if 'publication_date' in data and data['publication_date']:
            data['publication_date'] = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
        
        book = Book(
            title=data['title'],
            isbn=data.get('isbn'),
            publication_date=data.get('publication_date'),
            author_id=data['author_id'],
            copies_available=data.get('copies_available', 1),
            total_copies=data.get('total_copies', 1)
        )
        
        db.session.add(book)
        db.session.commit()
        
        return jsonify(book_schema.dump(book)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book(id):
    """Update an existing book"""
    try:
        book = Book.query.get_or_404(id)
        data = request.get_json()
        
        book.title = data.get('title', book.title)
        book.isbn = data.get('isbn', book.isbn)
        book.copies_available = data.get('copies_available', book.copies_available)
        book.total_copies = data.get('total_copies', book.total_copies)
        
        if 'publication_date' in data and data['publication_date']:
            book.publication_date = datetime.strptime(data['publication_date'], '%Y-%m-%d').date()
        
        if 'author_id' in data:
            author = Author.query.get(data['author_id'])
            if not author:
                return jsonify({'error': 'Author not found'}), 400
            book.author_id = data['author_id']
        
        db.session.commit()
        return jsonify(book_schema.dump(book))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """Delete a book"""
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

# USER ROUTES
@app.route('/api/users', methods=['GET'])
def get_users():
    """Get all users"""
    users = User.query.all()
    return jsonify(users_schema.dump(users))

@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    """Get a specific user"""
    user = User.query.get_or_404(id)
    return jsonify(user_schema.dump(user))

@app.route('/api/users', methods=['POST'])
def create_user():
    """Create a new user"""
    try:
        data = request.get_json()
        
        # Parse registration_date if provided
        if 'registration_date' in data and data['registration_date']:
            data['registration_date'] = datetime.strptime(data['registration_date'], '%Y-%m-%d').date()
        
        user = User(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            registration_date=data.get('registration_date', date.today())
        )
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify(user_schema.dump(user)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    """Update an existing user"""
    try:
        user = User.query.get_or_404(id)
        data = request.get_json()
        
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.phone = data.get('phone', user.phone)
        
        if 'registration_date' in data and data['registration_date']:
            user.registration_date = datetime.strptime(data['registration_date'], '%Y-%m-%d').date()
        
        db.session.commit()
        return jsonify(user_schema.dump(user))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Delete a user"""
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

# BORROWING ROUTES
@app.route('/api/borrowings', methods=['GET'])
def get_borrowings():
    """Get all borrowings"""
    borrowings = Borrowing.query.all()
    return jsonify(borrowings_schema.dump(borrowings))

@app.route('/api/borrowings/<int:id>', methods=['GET'])
def get_borrowing(id):
    """Get a specific borrowing"""
    borrowing = Borrowing.query.get_or_404(id)
    return jsonify(borrowing_schema.dump(borrowing))

@app.route('/api/borrowings', methods=['POST'])
def create_borrowing():
    """Create a new borrowing"""
    try:
        data = request.get_json()
        
        # Validate user and book exist
        user = User.query.get(data['user_id'])
        book = Book.query.get(data['book_id'])
        
        if not user:
            return jsonify({'error': 'User not found'}), 400
        if not book:
            return jsonify({'error': 'Book not found'}), 400
        if book.copies_available < 1:
            return jsonify({'error': 'No copies available'}), 400
        
        # Parse dates
        borrow_date = date.today()
        if 'borrow_date' in data and data['borrow_date']:
            borrow_date = datetime.strptime(data['borrow_date'], '%Y-%m-%d').date()
        
        due_date = borrow_date + timedelta(days=14)  # Default 2 weeks
        if 'due_date' in data and data['due_date']:
            due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
        
        borrowing = Borrowing(
            user_id=data['user_id'],
            book_id=data['book_id'],
            borrow_date=borrow_date,
            due_date=due_date,
            status='borrowed'
        )
        
        # Decrease available copies
        book.copies_available -= 1
        
        db.session.add(borrowing)
        db.session.commit()
        
        return jsonify(borrowing_schema.dump(borrowing)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/borrowings/<int:id>/return', methods=['PUT'])
def return_book(id):
    """Return a borrowed book"""
    try:
        borrowing = Borrowing.query.get_or_404(id)
        
        if borrowing.status == 'returned':
            return jsonify({'error': 'Book already returned'}), 400
        
        borrowing.return_date = date.today()
        borrowing.status = 'returned'
        
        # Increase available copies
        book = Book.query.get(borrowing.book_id)
        book.copies_available += 1
        
        db.session.commit()
        return jsonify(borrowing_schema.dump(borrowing))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/borrowings/<int:id>', methods=['PUT'])
def update_borrowing(id):
    """Update a borrowing"""
    try:
        borrowing = Borrowing.query.get_or_404(id)
        data = request.get_json()
        
        if 'due_date' in data and data['due_date']:
            borrowing.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
        
        if 'status' in data:
            borrowing.status = data['status']
        
        db.session.commit()
        return jsonify(borrowing_schema.dump(borrowing))
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# STATISTICS ROUTES
@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get library statistics"""
    stats = {
        'total_authors': Author.query.count(),
        'total_books': Book.query.count(),
        'total_users': User.query.count(),
        'active_borrowings': Borrowing.query.filter_by(status='borrowed').count(),
        'total_borrowings': Borrowing.query.count(),
        'available_books': db.session.query(db.func.sum(Book.copies_available)).scalar() or 0
    }
    return jsonify(stats)