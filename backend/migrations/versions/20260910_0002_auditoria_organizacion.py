"""Add creator and updater references to organizations.

Revision ID: 20260910_0002
Revises: 20260909_0001a
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260910_0002"
down_revision: str | None = "20260909_0001a"
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("organizacion", sa.Column("created_by", sa.Uuid(), nullable=True))
    op.add_column("organizacion", sa.Column("updated_by", sa.Uuid(), nullable=True))
    op.create_foreign_key("fk_organizacion_created_by", "organizacion", "usuario", ["created_by"], ["id"])
    op.create_foreign_key("fk_organizacion_updated_by", "organizacion", "usuario", ["updated_by"], ["id"])


def downgrade() -> None:
    op.drop_constraint("fk_organizacion_updated_by", "organizacion", type_="foreignkey")
    op.drop_constraint("fk_organizacion_created_by", "organizacion", type_="foreignkey")
    op.drop_column("organizacion", "updated_by")
    op.drop_column("organizacion", "created_by")
