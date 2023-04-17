"""add remaining COlumn in the posts table 

Revision ID: 4bb4fa1fb2a8
Revises: a882594be9ec
Create Date: 2023-04-17 01:56:00.196175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bb4fa1fb2a8'
down_revision = 'a882594be9ec'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column(
        'published',sa.Boolean(),nullable=False,server_default='True'),)
    op.add_column('posts',sa.Column(
        'created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')),)


def downgrade() -> None:
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
