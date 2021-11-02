"""empty message

Revision ID: 295dfb6770d6
Revises: 8a18d2859b62
Create Date: 2021-11-01 16:49:18.414552

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '295dfb6770d6'
down_revision = '8a18d2859b62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Goals',
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.create_table('Tasks',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['Goals.goal_id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.drop_table('task')
    op.drop_table('goal')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.INTEGER(), server_default=sa.text("nextval('goal_goal_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('goal_id', name='goal_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('task',
    sa.Column('task_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('goal_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goal.goal_id'], name='task_goal_id_fkey'),
    sa.PrimaryKeyConstraint('task_id', name='task_pkey')
    )
    op.drop_table('Tasks')
    op.drop_table('Goals')
    # ### end Alembic commands ###
