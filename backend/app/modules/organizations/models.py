from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, String, Text, UniqueConstraint, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.core.models import TimestampMixin, UUIDPrimaryKeyMixin


class Organizacion(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "organizacion"

    nombre_comercial: Mapped[str] = mapped_column(String(200), nullable=False, index=True)
    nombre_legal: Mapped[str | None] = mapped_column(String(250), nullable=True)
    telefono_principal: Mapped[str | None] = mapped_column(String(40), nullable=True)
    email_general: Mapped[str | None] = mapped_column(String(320), nullable=True)
    sitio_web: Mapped[str | None] = mapped_column(String(500), nullable=True)
    estado_relacion: Mapped[str | None] = mapped_column(String(60), nullable=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_by: Mapped[UUID | None] = mapped_column(Uuid(as_uuid=True), ForeignKey("usuario.id"), nullable=True)
    updated_by: Mapped[UUID | None] = mapped_column(Uuid(as_uuid=True), ForeignKey("usuario.id"), nullable=True)


class OrganizacionRol(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "organizacion_rol"
    __table_args__ = (
        UniqueConstraint("organizacion_id", "rol", "desde", name="uq_organizacion_rol_vigencia"),
    )

    organizacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("organizacion.id", ondelete="CASCADE"), nullable=False
    )
    rol: Mapped[str] = mapped_column(String(60), nullable=False)
    desde: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    hasta: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)


class Contacto(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "contacto"

    nombre: Mapped[str] = mapped_column(String(160), nullable=False)
    apellidos: Mapped[str | None] = mapped_column(String(200), nullable=True)
    telefono_principal: Mapped[str | None] = mapped_column(String(40), nullable=True, index=True)
    whatsapp: Mapped[str | None] = mapped_column(String(40), nullable=True, index=True)
    email_principal: Mapped[str | None] = mapped_column(String(320), nullable=True, index=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class ContactoOrganizacion(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "contacto_organizacion"

    contacto_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("contacto.id", ondelete="CASCADE"), nullable=False
    )
    organizacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("organizacion.id", ondelete="CASCADE"), nullable=False
    )
    area: Mapped[str | None] = mapped_column(String(120), nullable=True)
    cargo: Mapped[str | None] = mapped_column(String(160), nullable=True)
    es_contacto_principal: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    puede_solicitar_servicio: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    puede_autorizar: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    desde: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    hasta: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)


class ContactoOrganizacionRol(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "contacto_organizacion_rol"
    __table_args__ = (
        UniqueConstraint("contacto_organizacion_id", "rol", name="uq_contacto_organizacion_rol"),
    )

    contacto_organizacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True),
        ForeignKey("contacto_organizacion.id", ondelete="CASCADE"),
        nullable=False,
    )
    rol: Mapped[str] = mapped_column(String(60), nullable=False)


class PerfilFiscal(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "perfil_fiscal"

    organizacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("organizacion.id", ondelete="CASCADE"), nullable=False
    )
    razon_social: Mapped[str] = mapped_column(String(250), nullable=False)
    rfc: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    regimen_fiscal: Mapped[str | None] = mapped_column(String(80), nullable=True)
    codigo_postal_fiscal: Mapped[str | None] = mapped_column(String(12), nullable=True)
    email_facturacion: Mapped[str | None] = mapped_column(String(320), nullable=True)
    uso_cfdi_default: Mapped[str | None] = mapped_column(String(20), nullable=True)
    es_predeterminado: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    vigente_desde: Mapped[date | None] = mapped_column(Date, nullable=True)
    vigente_hasta: Mapped[date | None] = mapped_column(Date, nullable=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)


class Ubicacion(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "ubicacion"

    organizacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("organizacion.id", ondelete="CASCADE"), nullable=False
    )
    nombre: Mapped[str] = mapped_column(String(200), nullable=False)
    direccion_linea_1: Mapped[str | None] = mapped_column(String(250), nullable=True)
    direccion_linea_2: Mapped[str | None] = mapped_column(String(250), nullable=True)
    colonia: Mapped[str | None] = mapped_column(String(160), nullable=True)
    ciudad: Mapped[str | None] = mapped_column(String(160), nullable=True)
    estado_region: Mapped[str | None] = mapped_column(String(160), nullable=True)
    codigo_postal: Mapped[str | None] = mapped_column(String(20), nullable=True)
    pais: Mapped[str] = mapped_column(String(2), default="MX", nullable=False)
    referencias_acceso: Mapped[str | None] = mapped_column(Text, nullable=True)
    horarios: Mapped[str | None] = mapped_column(Text, nullable=True)
    observaciones_tecnicas: Mapped[str | None] = mapped_column(Text, nullable=True)
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
