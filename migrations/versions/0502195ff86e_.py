"""empty message

Revision ID: 0502195ff86e
Revises: 
Create Date: 2020-09-24 17:56:47.641502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0502195ff86e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('email_tracker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('loan_id', sa.Integer(), nullable=True),
    sa.Column('last_trigger', sa.Integer(), nullable=True),
    sa.Column('is_overdue', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['loan_id'], ['loan.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('loan_id')
    )
    op.alter_column('subscriber', 'paid',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('false'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('subscriber', 'paid',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('false'))
    op.drop_table('email_tracker')
    # ### end Alembic commands ###