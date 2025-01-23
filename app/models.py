from app import db
from book_alchemy import app


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    date_of_death = db.Column(db.Date)

    def __repr__(self):
        return (
            f"<Author(id={self.id}',"
            f"name='{self.name}', "
            f"birth_date='{self.birth_date}', "
            f"date_of_death='{self.date_of_death}')>"
        )

    def __str__(self):
        if self.date_of_death is None:
            return f"{self.name} was born {self.birth_date}"
        return (
            f"{self.name} was born {self.birth_date} "
            f"and died {self.date_of_death}"  # noqa E501
        )


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(13))
    title = db.Column(db.String(100))
    publication_year = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))


with app.app_context():
    db.create_all()


# create ORM classes here
# with app.app_context():
#     db.create_all()
