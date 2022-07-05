"""add content column

Revision ID: 5538c791bcfe
Revises: 7ad41855411d
Create Date: 2022-07-05 10:32:45.192082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5538c791bcfe'
down_revision = '7ad41855411d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
