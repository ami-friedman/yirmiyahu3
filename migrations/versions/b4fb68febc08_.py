"""empty message

Revision ID: b4fb68febc08
Revises: ed3095f499ff
Create Date: 2021-03-12 08:30:36.584801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4fb68febc08'
down_revision = 'ed3095f499ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('category_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'category_id')
    # ### end Alembic commands ###
