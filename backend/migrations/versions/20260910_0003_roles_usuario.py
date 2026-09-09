"""Add internal roles to users.

Revision ID: 20260910_0003
Revises: 20260910_0002
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "20260910_0003"
down_revision: str | None = "20260910_0002"
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("usuario", sa.Column("rol", sa.String(length=30), nullable=True))
    op.execute("UPDATE usuario SET rol = 'admin' WHERE rol IS NULL")
    op.alter_column("usuario", "rol", nullable=False, server_default="tecnico")


def downgrade() -> None:
    op.alter_column("usuario", "rol", server_default=None)
    op.drop_column("usuario", "rol")
