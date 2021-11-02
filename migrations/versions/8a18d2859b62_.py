"""empty message

Revision ID: 8a18d2859b62
Revises: 24ae9026eae7
Create Date: 2021-11-01 15:05:39.734271

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8a18d2859b62'
down_revision = '24ae9026eae7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.create_table('task',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goal.goal_id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    op.drop_table('Goals')
    op.drop_table('Tasks')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Tasks',
    sa.Column('task_id', sa.INTEGER(), server_default=sa.text('nextval(\'"Tasks_task_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('goal_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['Goals.goal_id'], name='Tasks_goal_id_fkey'),
    sa.PrimaryKeyConstraint('task_id', name='Tasks_pkey')
    )
    op.create_table('Goals',
    sa.Column('goal_id', sa.INTEGER(), server_default=sa.text('nextval(\'"Goals_goal_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('title', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('goal_id', name='Goals_pkey')
    )
    op.drop_table('task')
    op.drop_table('goal')
    # ### end Alembic commands ###