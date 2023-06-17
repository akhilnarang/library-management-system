# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.book import Book  # noqa
from app.models.member import Member  # noqa
from app.models.members_books import MembersBooks  # noqa