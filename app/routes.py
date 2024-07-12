from flask import Blueprint, jsonify, request
from app.models import Book, Member, BorrowedBook
from app.extensions import db
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Welcome to the Library Management System"

# Book routes
@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{
        'book_id': book.book_id,
        'title': book.title,
        'author': book.author,
        'published_date': book.published_date.isoformat() if book.published_date else None,
        'isbn': book.isbn,
        'copies_available': book.copies_available
    } for book in books])

@bp.route('/books', methods=['POST'])
def create_book():
    data = request.json
    new_book = Book(
        title=data['title'],
        author=data['author'],
        published_date=datetime.strptime(data['published_date'], '%Y-%m-%d').date(),
        isbn=data['isbn'],
        copies_available=data['copies_available']
    )
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book created successfully'}), 201

@bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        'book_id': book.book_id,
        'title': book.title,
        'author': book.author,
        'published_date': book.published_date.isoformat() if book.published_date else None,
        'isbn': book.isbn,
        'copies_available': book.copies_available
    })

# Member routes
@bp.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{
        'member_id': member.member_id,
        'first_name': member.first_name,
        'last_name': member.last_name,
        'email': member.email,
        'phone_number': member.phone_number,
        'membership_start_date': member.membership_start_date.isoformat(),
        'membership_end_date': member.membership_end_date.isoformat() if member.membership_end_date else None
    } for member in members])

@bp.route('/members', methods=['POST'])
def create_member():
    data = request.json
    new_member = Member(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone_number=data.get('phone_number'),
        membership_start_date=datetime.strptime(data['membership_start_date'], '%Y-%m-%d').date(),
        membership_end_date=datetime.strptime(data['membership_end_date'], '%Y-%m-%d').date() if 'membership_end_date' in data else None
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({'message': 'Member created successfully'}), 201

@bp.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = Member.query.get_or_404(member_id)
    return jsonify({
        'member_id': member.member_id,
        'first_name': member.first_name,
        'last_name': member.last_name,
        'email': member.email,
        'phone_number': member.phone_number,
        'membership_start_date': member.membership_start_date.isoformat(),
        'membership_end_date': member.membership_end_date.isoformat() if member.membership_end_date else None
    })

# BorrowedBook routes
@bp.route('/borrowed-books', methods=['GET'])
def get_borrowed_books():
    borrowed_books = BorrowedBook.query.all()
    return jsonify([{
        'borrow_id': bb.borrow_id,
        'member_id': bb.member_id,
        'book_id': bb.book_id,
        'borrow_date': bb.borrow_date.isoformat(),
        'return_date': bb.return_date.isoformat() if bb.return_date else None
    } for bb in borrowed_books])

@bp.route('/borrowed-books', methods=['POST'])
def create_borrowed_book():
    data = request.json
    new_borrowed_book = BorrowedBook(
        member_id=data['member_id'],
        book_id=data['book_id'],
        borrow_date=datetime.strptime(data['borrow_date'], '%Y-%m-%d').date(),
        return_date=datetime.strptime(data['return_date'], '%Y-%m-%d').date() if 'return_date' in data else None
    )
    db.session.add(new_borrowed_book)
    db.session.commit()
    return jsonify({'message': 'Borrowed book record created successfully'}), 201

@bp.route('/borrowed-books/<int:borrow_id>', methods=['GET'])
def get_borrowed_book(borrow_id):
    borrowed_book = BorrowedBook.query.get_or_404(borrow_id)
    return jsonify({
        'borrow_id': borrowed_book.borrow_id,
        'member_id': borrowed_book.member_id,
        'book_id': borrowed_book.book_id,
        'borrow_date': borrowed_book.borrow_date.isoformat(),
        'return_date': borrowed_book.return_date.isoformat() if borrowed_book.return_date else None
    })