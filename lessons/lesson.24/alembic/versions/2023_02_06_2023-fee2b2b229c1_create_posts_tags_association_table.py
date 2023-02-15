"""create posts-tags association table

Revision ID: fee2b2b229c1
Revises: 8605758fcfe8
Create Date: 2023-02-06 20:23:57.607972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fee2b2b229c1"
down_revision = "8605758fcfe8"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "posts_tags_association",
        sa.Column("post_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["post_id"],
            ["blog_posts.id"],
        ),
        sa.ForeignKeyConstraint(
            ["tag_id"],
            ["blog_tags.id"],
        ),
        sa.PrimaryKeyConstraint("post_id", "tag_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("posts_tags_association")
    # ### end Alembic commands ###
