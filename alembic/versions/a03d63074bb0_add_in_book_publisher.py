"""Add in book publisher

Revision ID: a03d63074bb0
Revises: d139105ae9ed
Create Date: 2023-06-22 21:01:56.616263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a03d63074bb0'
down_revision = 'd139105ae9ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('publisher', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'publisher')
    # ### end Alembic commands ###
