"""add content in posts table

Revision ID: d27e8071d072
Revises: 5bc64ea5ba12
Create Date: 2023-04-17 00:06:24.628597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd27e8071d072'
down_revision = '5bc64ea5ba12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
