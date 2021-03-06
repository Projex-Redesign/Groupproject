"""empty message

Revision ID: efa51de53f0a
Revises: 5c1b3a81305e
Create Date: 2018-11-17 22:51:06.879150

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'efa51de53f0a'
down_revision = '5c1b3a81305e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('settings', 'notification_period',
               existing_type=mysql.DOUBLE(asdecimal=True),
               nullable=False)
    op.add_column('users', sa.Column('is_staff', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_student', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_student')
    op.drop_column('users', 'is_staff')
    op.alter_column('settings', 'notification_period',
               existing_type=mysql.DOUBLE(asdecimal=True),
               nullable=True)
    # ### end Alembic commands ###
