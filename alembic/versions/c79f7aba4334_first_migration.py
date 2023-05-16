""" first migration

Revision ID: c79f7aba4334
Revises: 
Create Date: 2023-05-16 16:34:58.630724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c79f7aba4334'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('foo',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foo')
    # ### end Alembic commands ###