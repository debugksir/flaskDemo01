"""empty message

Revision ID: 57babbf728c6
Revises: 
Create Date: 2019-03-08 11:47:24.480354

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '57babbf728c6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('id_UNIQUE', table_name='test')
    op.drop_table('test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=45), nullable=False),
    sa.Column('sex', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('age', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('address', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8mb4',
    mysql_engine=u'InnoDB'
    )
    op.create_index('id_UNIQUE', 'test', ['id'], unique=True)
    op.drop_table('article')
    op.drop_table('user')
    # ### end Alembic commands ###
