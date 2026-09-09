from uuid import UUID

from sqlalchemy import BigInteger, ForeignKey, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.core.models import TimestampMixin, UUIDPrimaryKeyMixin


class Archivo(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    __tablename__ = "archivo"

    storage_key: Mapped[str] = mapped_column(String(500), unique=True, nullable=False)
    nombre_original: Mapped[str] = mapped_column(String(500), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(160), nullable=False)
    size_bytes: Mapped[int | None] = mapped_column(BigInteger, nullable=True)
    sha256: Mapped[str | None] = mapped_column(String(64), nullable=True, index=True)
    uploaded_by: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("usuario.id"), nullable=True
    )
