"""Add phone or back to message for correct working things

Revision ID: 1cd424b0e63d
Revises: f7a9766f83bc
Create Date: 2023-04-17 05:55:04.751529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1cd424b0e63d'
down_revision = 'f7a9766f83bc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users',sa.Column(
        'p_num',sa.String,nullable=True
    ))

    pass


def downgrade() -> None:
    op.drop_column('users','phone_number')
