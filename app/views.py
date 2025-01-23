from flask import Blueprint, redirect, url_for, render_template, flash, request

from app.forms import AuthorForm, BookForm
from app.models import Author
from app.services import DBLogic as dbl
from app.logger import setup_logger


logger = setup_logger(__name__)

main = Blueprint("main", __name__)


@main.before_request
def before_request():
    ip_address = request.remote_addr
    logger.info(f"Incoming request from {ip_address}")


@main.route("/")
def index():
    books = dbl.get_books()
    return render_template("home.html", books=books)


@main.route("/add_author", methods=["GET", "POST"])
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        name = form.name.data
        birth_date = form.birth_date.data
        date_of_death = form.date_of_death.data
        response = dbl.add_author(name, birth_date, date_of_death)
        flash(f"Author {response.name} added to the database")
        return redirect(url_for("main.index"))
    return render_template("add_author.html", form=form)


@main.route("/add_book", methods=["GET", "POST"])
def add_book():
    form = BookForm()
    authors = Author.query.all()
    form.author.choices = [
        (author.id, f"{author.name} ({author.birth_date})")
        for author in authors  # noqa E501
    ]
    if form.validate_on_submit():
        isbn = form.isbn.data
        title = form.title.data
        publication_year = form.publication_year.data
        author_id = form.author.data
        response = dbl.add_book(isbn, title, publication_year, author_id)
        flash(f"Book {response.title} added to the database")
        return redirect(url_for("main.index"))
    return render_template("add_book.html", form=form)
