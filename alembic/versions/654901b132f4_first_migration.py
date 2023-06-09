""" first migration

Revision ID: 654901b132f4
Revises: 
Create Date: 2023-05-31 23:16:38.620235

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "654901b132f4"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "foo",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("foo")
    # ### end Alembic commands ###
