from app.db import db
from app.models import Author, Book
from app.logger import setup_logger
from sqlalchemy import func

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

    @staticmethod
    def sort_inventory(sorting_criteria, sorting_direction):
        logger.info(
            f"Sorting books by {sorting_criteria} in {sorting_direction} order"
        )  # noqa E501

        criteria_mapping = {"book": Book.title, "author": Author.name}

        direction_mapping = {
            "asc": lambda field: field.asc(),
            "desc": lambda field: field.desc(),
        }

        criteria_column = criteria_mapping.get(sorting_criteria)
        direction_function = direction_mapping.get(sorting_direction)

        criteria_result = (
            db.session.query(Book, Author)
            .join(Author, Book.author_id == Author.id)
            .order_by(direction_function(criteria_column))
            .all()
        )
        for row in criteria_result:
            logger.info(row)
        return criteria_result

    @staticmethod
    def search_inventory(item, search):
        logger.info(f"Searching for {item} with {search}")
        search = search.strip().lower()
        search_mapping = {"author": Author.name, "book": Book.title}
        search_column = search_mapping.get(item)
        search_result = (
            db.session.query(Book, Author)
            .join(Author, Book.author_id == Author.id)
            .filter(func.lower(search_column).like(f"%{search}%"))
            .all()
        )
        for row in search_result:
            logger.info(row)
        return search_result

    @staticmethod
    def delete_book(title_to_delete):
        logger.info(f"Deleting book with {title_to_delete}")
        delete_result = (
            db.session.query(Book)
            .where(Book.title == title_to_delete)
            .delete()  # noqa E501
        )
        db.session.commit()
        return delete_result
