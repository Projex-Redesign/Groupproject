"""empty message

Revision ID: 7635c651d2a4
Revises: b257c39bc0bb
Create Date: 2018-09-30 17:53:36.699519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7635c651d2a4'
down_revision = 'b257c39bc0bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('team_member_ibfk_1', 'team_member', type_='foreignkey')
    op.create_foreign_key(None, 'team_member', 'team', ['team_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'team_member', type_='foreignkey')
    op.create_foreign_key('team_member_ibfk_1', 'team_member', 'team', ['team_id'], ['id'])
    # ### end Alembic commands ###