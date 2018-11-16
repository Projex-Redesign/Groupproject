"""empty message

Revision ID: dddf6f161be1
Revises: 301ed8345d87
Create Date: 2018-09-30 14:31:31.229928

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dddf6f161be1'
down_revision = '301ed8345d87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'academic_year',
               existing_type=mysql.VARCHAR(length=7),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'academic_year',
               existing_type=mysql.VARCHAR(length=7),
               nullable=True)
    # ### end Alembic commands ###