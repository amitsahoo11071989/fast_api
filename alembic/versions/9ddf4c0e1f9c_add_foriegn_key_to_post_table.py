"""add foriegn key to post table

Revision ID: 9ddf4c0e1f9c
Revises: 010a4101d0ac
Create Date: 2022-08-02 13:45:49.139277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ddf4c0e1f9c'
down_revision = '010a4101d0ac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('user_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['user_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
