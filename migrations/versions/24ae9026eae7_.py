"""empty message

Revision ID: 24ae9026eae7
Revises: c33bfd1144d7
Create Date: 2021-11-01 14:24:09.713250

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24ae9026eae7'
down_revision = 'c33bfd1144d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tasks', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Tasks', 'Goals', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Tasks', type_='foreignkey')
    op.drop_column('Tasks', 'goal_id')
    # ### end Alembic commands ###
