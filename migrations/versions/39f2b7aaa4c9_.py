"""empty message

Revision ID: 39f2b7aaa4c9
Revises: 
Create Date: 2021-10-30 20:09:13.636443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39f2b7aaa4c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###