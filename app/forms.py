from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.datetime import DateField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, Optional, Length, NumberRange


class AuthorForm(FlaskForm):
    name = StringField("Author's Name", validators=[DataRequired()])
    birth_date = DateField(
        "Author's Birth Date", validators=[DataRequired()], format="%Y-%m-%d"
    )
    date_of_death = DateField(
        "Author's Death Date", validators=[Optional()], format="%Y-%m-%d"
    )
    submit = SubmitField("Add Author")


class BookForm(FlaskForm):
    author = SelectField("Author", choices=[], validators=[DataRequired()])

    isbn = StringField(
        "ISBN Number",
        validators=[
            DataRequired(),
            Length(
                min=10,
                max=13,
                message="ISBN must be between 10 and 13 characters",  # noqa E501
            ),  # noqa E501
        ],
    )
    title = StringField("Title", validators=[DataRequired()])
    publication_year = IntegerField(
        "Publication Year",
        validators=[
            DataRequired(),
            NumberRange(
                min=1000, max=2025, message="Year must be a 4-digit number"
            ),  # noqa E501
        ],
    )
    submit = SubmitField("Add Book")


class SortForm(FlaskForm):
    sorting_criteria = SelectField(
        "Sort by",
        choices=[("book", "Book Title"), ("author", "Author Name")],
        validators=[DataRequired()],
    )
    sorting_direction = SelectField(
        "Sort Direction",
        choices=[("asc", "Ascending"), ("desc", "Descending")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Sort Inventory")


class SearchForm(FlaskForm):
    item = SelectField(
        "Search by", choices=[("author", "Author"), ("book", "Book")]
    )  # noqa E501
    search = StringField("Search", validators=[DataRequired()])
    submit = SubmitField("Search")
