"""empty message

Revision ID: 7ec2358350a0
Revises: 0502195ff86e
Create Date: 2020-11-02 21:58:45.358127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ec2358350a0'
down_revision = '0502195ff86e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('loan', sa.Column('extended_date', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('loan', 'extended_date')
    # ### end Alembic commands ###
