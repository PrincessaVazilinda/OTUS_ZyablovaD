"""upgrade author name

Revision ID: bfb8d98c4f6f
Revises: dfe016ae0bdd
Create Date: 2023-02-01 21:04:13.738520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bfb8d98c4f6f"
down_revision = "dfe016ae0bdd"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "blog_authors",
        "name",
        existing_type=sa.VARCHAR(length=80),
        type_=sa.String(length=160),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "blog_authors",
        "name",
        existing_type=sa.String(length=160),
        type_=sa.VARCHAR(length=80),
        existing_nullable=False,
        existing_server_default=sa.text("''::character varying"),
    )
    # ### end Alembic commands ###
