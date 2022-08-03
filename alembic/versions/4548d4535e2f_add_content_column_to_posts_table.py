"""add content column to posts table

Revision ID: 4548d4535e2f
Revises: 7d23a4b0428a
Create Date: 2022-08-02 12:35:45.662348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4548d4535e2f'
down_revision = '7d23a4b0428a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
