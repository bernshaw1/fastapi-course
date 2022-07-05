"""add last few columns

Revision ID: 5691739503fd
Revises: 63fe15d5a41d
Create Date: 2022-07-05 11:15:01.137519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5691739503fd'
down_revision = '63fe15d5a41d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
