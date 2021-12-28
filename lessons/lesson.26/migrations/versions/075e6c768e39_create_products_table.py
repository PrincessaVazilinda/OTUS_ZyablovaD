"""create products table

Revision ID: 075e6c768e39
Revises: 
Create Date: 2021-11-30 20:32:24.184252

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '075e6c768e39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'product',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), server_default='', nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###