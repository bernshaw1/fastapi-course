"""add user table

Revision ID: 9615337f0b7d
Revises: 5538c791bcfe
Create Date: 2022-07-05 10:36:59.320015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9615337f0b7d'
down_revision = '5538c791bcfe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
