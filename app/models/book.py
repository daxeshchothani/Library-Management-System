from app.extensions import db

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.Date)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    copies_available = db.Column(db.Integer, default=0)