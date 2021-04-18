"""empty message

Revision ID: 87158c0132f4
Revises: b4fb68febc08
Create Date: 2021-03-12 11:37:08.559147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87158c0132f4'
down_revision = 'b4fb68febc08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('book', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'category_id')
    op.drop_table('category')
    # ### end Alembic commands ###
