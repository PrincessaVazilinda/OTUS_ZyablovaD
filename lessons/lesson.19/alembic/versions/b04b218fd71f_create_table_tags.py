"""create table tags

Revision ID: b04b218fd71f
Revises: ea80539a5edd
Create Date: 2022-05-19 20:25:47.327599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b04b218fd71f"
down_revision = "ea80539a5edd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tags")
    # ### end Alembic commands ###
