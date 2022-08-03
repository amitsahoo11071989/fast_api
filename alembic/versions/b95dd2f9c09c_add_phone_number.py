"""add phone number

Revision ID: b95dd2f9c09c
Revises: 6cb54121f4a8
Create Date: 2022-08-02 14:16:46.249899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b95dd2f9c09c'
down_revision = '6cb54121f4a8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('abobcd')
    op.drop_table('persons')
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_number')
    op.create_table('persons',
    sa.Column('personid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('lastname', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('firstname', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('address', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=255), autoincrement=False, nullable=True)
    )
    op.create_table('abobcd',
    sa.Column('cmd_output', sa.TEXT(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###