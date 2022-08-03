"""create users table

Revision ID: 010a4101d0ac
Revises: 4548d4535e2f
Create Date: 2022-08-02 13:32:53.608095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '010a4101d0ac'
down_revision = '4548d4535e2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
     sa.Column('id', sa.Integer(), nullable = False,),
    sa.Column('email', sa.String(), nullable = False),
    sa.Column('password', sa.String(), nullable = False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable = False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop('users')
    pass
