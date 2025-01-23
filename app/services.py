from app.db import db
from app.models import Author, Book
from app.logger import setup_logger

logger = setup_logger(__name__)


class DBLogic:
    @staticmethod
    def add_author(name, birth_date, date_of_death):
        logger.info(f"Adding author..{name=}, {birth_date=}, {date_of_death=}")
        new_author = Author(
            name=name, birth_date=birth_date, date_of_death=date_of_death
        )
        try:
            db.session.add(new_author)
            db.session.commit()
            logger.info("Author added successfully %s", new_author.name)
        except Exception as e:
            logger.error(f"Error adding author: {e}")
            db.session.rollback()
            return None
        return new_author

    @staticmethod
    def add_book(isbn, title, publication_year, author_id):
        logger.info(
            f"Adding book.{isbn=}, {title=}, {publication_year=}, {author_id=}"
        )  # noqa E501
        new_book = Book(
            isbn=isbn,
            title=title,
            publication_year=publication_year,
            author_id=author_id,
        )
        try:
            db.session.add(new_book)
            db.session.commit()
            logger.info("Book added successfully %s", new_book.title)
        except Exception as e:
            logger.error(f"Error adding book: {e}")
            db.session.rollback()
            return None
        return new_book

    @staticmethod
    def get_books():
        logger.info("Getting books...")
        books = (
            db.session.query(Book, Author)
            .join(Author, Book.author_id == Author.id)
            .all()
        )
        return books
