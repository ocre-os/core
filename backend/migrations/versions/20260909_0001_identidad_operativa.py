"""identidad operativa V0

Revision ID: 20260909_0001
Revises:
Create Date: 2026-09-09
"""

from collections.abc import Sequence

from alembic import op
import sqlalchemy as sa


revision: str = "20260909_0001"
down_revision: str | None = None
branch_labels: Sequence[str] | None = None
depends_on: Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "organizacion",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("nombre_comercial", sa.String(length=200), nullable=False),
        sa.Column("nombre_legal", sa.String(length=250), nullable=True),
        sa.Column("telefono_principal", sa.String(length=40), nullable=True),
        sa.Column("email_general", sa.String(length=320), nullable=True),
        sa.Column("sitio_web", sa.String(length=500), nullable=True),
        sa.Column("estado_relacion", sa.String(length=60), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_organizacion_nombre_comercial", "organizacion", ["nombre_comercial"])

    op.create_table(
        "organizacion_rol",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("organizacion_id", sa.Uuid(), nullable=False),
        sa.Column("rol", sa.String(length=60), nullable=False),
        sa.Column("desde", sa.DateTime(timezone=True), nullable=True),
        sa.Column("hasta", sa.DateTime(timezone=True), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["organizacion_id"], ["organizacion.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("organizacion_id", "rol", "desde", name="uq_organizacion_rol_vigencia"),
    )

    op.create_table(
        "contacto",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("nombre", sa.String(length=160), nullable=False),
        sa.Column("apellidos", sa.String(length=200), nullable=True),
        sa.Column("telefono_principal", sa.String(length=40), nullable=True),
        sa.Column("whatsapp", sa.String(length=40), nullable=True),
        sa.Column("email_principal", sa.String(length=320), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_contacto_telefono_principal", "contacto", ["telefono_principal"])
    op.create_index("ix_contacto_whatsapp", "contacto", ["whatsapp"])
    op.create_index("ix_contacto_email_principal", "contacto", ["email_principal"])

    op.create_table(
        "contacto_organizacion",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("contacto_id", sa.Uuid(), nullable=False),
        sa.Column("organizacion_id", sa.Uuid(), nullable=False),
        sa.Column("area", sa.String(length=120), nullable=True),
        sa.Column("cargo", sa.String(length=160), nullable=True),
        sa.Column("es_contacto_principal", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("puede_solicitar_servicio", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("puede_autorizar", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("desde", sa.DateTime(timezone=True), nullable=True),
        sa.Column("hasta", sa.DateTime(timezone=True), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["contacto_id"], ["contacto.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["organizacion_id"], ["organizacion.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "contacto_organizacion_rol",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("contacto_organizacion_id", sa.Uuid(), nullable=False),
        sa.Column("rol", sa.String(length=60), nullable=False),
        sa.ForeignKeyConstraint(
            ["contacto_organizacion_id"],
            ["contacto_organizacion.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("contacto_organizacion_id", "rol", name="uq_contacto_organizacion_rol"),
    )

    op.create_table(
        "perfil_fiscal",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("organizacion_id", sa.Uuid(), nullable=False),
        sa.Column("razon_social", sa.String(length=250), nullable=False),
        sa.Column("rfc", sa.String(length=20), nullable=False),
        sa.Column("regimen_fiscal", sa.String(length=80), nullable=True),
        sa.Column("codigo_postal_fiscal", sa.String(length=12), nullable=True),
        sa.Column("email_facturacion", sa.String(length=320), nullable=True),
        sa.Column("uso_cfdi_default", sa.String(length=20), nullable=True),
        sa.Column("es_predeterminado", sa.Boolean(), nullable=False, server_default=sa.false()),
        sa.Column("vigente_desde", sa.Date(), nullable=True),
        sa.Column("vigente_hasta", sa.Date(), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["organizacion_id"], ["organizacion.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_perfil_fiscal_rfc", "perfil_fiscal", ["rfc"])

    op.create_table(
        "ubicacion",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("organizacion_id", sa.Uuid(), nullable=False),
        sa.Column("nombre", sa.String(length=200), nullable=False),
        sa.Column("direccion_linea_1", sa.String(length=250), nullable=True),
        sa.Column("direccion_linea_2", sa.String(length=250), nullable=True),
        sa.Column("colonia", sa.String(length=160), nullable=True),
        sa.Column("ciudad", sa.String(length=160), nullable=True),
        sa.Column("estado_region", sa.String(length=160), nullable=True),
        sa.Column("codigo_postal", sa.String(length=20), nullable=True),
        sa.Column("pais", sa.String(length=2), nullable=False, server_default="MX"),
        sa.Column("referencias_acceso", sa.Text(), nullable=True),
        sa.Column("horarios", sa.Text(), nullable=True),
        sa.Column("observaciones_tecnicas", sa.Text(), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["organizacion_id"], ["organizacion.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "equipo",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("codigo", sa.String(length=40), nullable=False),
        sa.Column("tipo_familia", sa.String(length=120), nullable=True),
        sa.Column("marca", sa.String(length=160), nullable=True),
        sa.Column("modelo", sa.String(length=160), nullable=True),
        sa.Column("numero_serie", sa.String(length=160), nullable=True),
        sa.Column("descripcion", sa.Text(), nullable=True),
        sa.Column("estado_operativo", sa.String(length=60), nullable=True),
        sa.Column("fecha_alta", sa.DateTime(timezone=True), nullable=False),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.Column("archived_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("codigo"),
    )
    op.create_index("ix_equipo_codigo", "equipo", ["codigo"], unique=True)
    op.create_index("ix_equipo_numero_serie", "equipo", ["numero_serie"])

    op.create_table(
        "equipo_organizacion",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("equipo_id", sa.Uuid(), nullable=False),
        sa.Column("organizacion_id", sa.Uuid(), nullable=False),
        sa.Column("tipo_relacion", sa.String(length=60), nullable=False),
        sa.Column("desde", sa.DateTime(timezone=True), nullable=False),
        sa.Column("hasta", sa.DateTime(timezone=True), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["equipo_id"], ["equipo.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["organizacion_id"], ["organizacion.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "equipo_ubicacion",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("equipo_id", sa.Uuid(), nullable=False),
        sa.Column("ubicacion_id", sa.Uuid(), nullable=False),
        sa.Column("desde", sa.DateTime(timezone=True), nullable=False),
        sa.Column("hasta", sa.DateTime(timezone=True), nullable=True),
        sa.Column("motivo_cambio", sa.String(length=250), nullable=True),
        sa.Column("notas", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["equipo_id"], ["equipo.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["ubicacion_id"], ["ubicacion.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "usuario",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("nombre_mostrado", sa.String(length=160), nullable=False),
        sa.Column("activo", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column("contacto_id", sa.Uuid(), nullable=True),
        sa.Column("ultimo_acceso_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["contacto_id"], ["contacto.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index("ix_usuario_email", "usuario", ["email"], unique=True)

    op.create_table(
        "archivo",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("storage_key", sa.String(length=500), nullable=False),
        sa.Column("nombre_original", sa.String(length=500), nullable=False),
        sa.Column("mime_type", sa.String(length=160), nullable=False),
        sa.Column("size_bytes", sa.BigInteger(), nullable=True),
        sa.Column("sha256", sa.String(length=64), nullable=True),
        sa.Column("uploaded_by", sa.Uuid(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["uploaded_by"], ["usuario.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("storage_key"),
    )
    op.create_index("ix_archivo_sha256", "archivo", ["sha256"])


def downgrade() -> None:
    op.drop_index("ix_archivo_sha256", table_name="archivo")
    op.drop_table("archivo")

    op.drop_index("ix_usuario_email", table_name="usuario")
    op.drop_table("usuario")

    op.drop_table("equipo_ubicacion")
    op.drop_table("equipo_organizacion")

    op.drop_index("ix_equipo_numero_serie", table_name="equipo")
    op.drop_index("ix_equipo_codigo", table_name="equipo")
    op.drop_table("equipo")

    op.drop_table("ubicacion")

    op.drop_index("ix_perfil_fiscal_rfc", table_name="perfil_fiscal")
    op.drop_table("perfil_fiscal")

    op.drop_table("contacto_organizacion_rol")
    op.drop_table("contacto_organizacion")

    op.drop_index("ix_contacto_email_principal", table_name="contacto")
    op.drop_index("ix_contacto_whatsapp", table_name="contacto")
    op.drop_index("ix_contacto_telefono_principal", table_name="contacto")
    op.drop_table("contacto")

    op.drop_table("organizacion_rol")
    op.drop_index("ix_organizacion_nombre_comercial", table_name="organizacion")
    op.drop_table("organizacion")
