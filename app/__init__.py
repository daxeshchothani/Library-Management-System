from flask import Flask
from config import Config
from app.extensions import db
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Import models
    from app.models import Book, Member, BorrowedBook

    # Create the database tables
    with app.app_context():
        db.create_all()

    from app import routes
    app.register_blueprint(routes.bp)

    return app