from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.core.models import TimestampMixin, UUIDPrimaryKeyMixin


class Equipo(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "equipo"

    codigo: Mapped[str] = mapped_column(String(40), unique=True, nullable=False, index=True)
    tipo_familia: Mapped[str | None] = mapped_column(String(120), nullable=True)
    marca: Mapped[str | None] = mapped_column(String(160), nullable=True)
    modelo: Mapped[str | None] = mapped_column(String(160), nullable=True)
    numero_serie: Mapped[str | None] = mapped_column(String(160), nullable=True, index=True)
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)
    estado_operativo: Mapped[str | None] = mapped_column(String(60), nullable=True)
    fecha_alta: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)
    archived_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class EquipoOrganizacion(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "equipo_organizacion"

    equipo_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("equipo.id", ondelete="CASCADE"), nullable=False
    )
    organizacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("organizacion.id", ondelete="CASCADE"), nullable=False
    )
    tipo_relacion: Mapped[str] = mapped_column(String(60), nullable=False)
    desde: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    hasta: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)


class EquipoUbicacion(UUIDPrimaryKeyMixin, Base):
    __tablename__ = "equipo_ubicacion"

    equipo_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("equipo.id", ondelete="CASCADE"), nullable=False
    )
    ubicacion_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ubicacion.id", ondelete="CASCADE"), nullable=False
    )
    desde: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    hasta: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    motivo_cambio: Mapped[str | None] = mapped_column(String(250), nullable=True)
    notas: Mapped[str | None] = mapped_column(Text, nullable=True)
