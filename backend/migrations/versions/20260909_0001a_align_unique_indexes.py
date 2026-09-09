"""Align redundant unique constraints with SQLAlchemy metadata.

Revision ID: 20260909_0001a
Revises: 20260909_0001
"""

from collections.abc import Sequence

from alembic import op

revision: str = "20260909_0001a"
down_revision: str | None = "20260909_0001"
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    # The existing unique indexes continue enforcing uniqueness.
    op.drop_constraint("equipo_codigo_key", "equipo", type_="unique")
    op.drop_constraint("usuario_email_key", "usuario", type_="unique")


def downgrade() -> None:
    op.create_unique_constraint("usuario_email_key", "usuario", ["email"])
    op.create_unique_constraint("equipo_codigo_key", "equipo", ["codigo"])
