"""create remaining columns in posts table

Revision ID: a5e79439f9d0
Revises: 9ddf4c0e1f9c
Create Date: 2022-08-02 14:00:36.106127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5e79439f9d0'
down_revision = '9ddf4c0e1f9c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('published', sa.Boolean(), nullable = True, server_default = 'TRUE'))
    op.add_column("posts", sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable = False))
    pass

 
def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
