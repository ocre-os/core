from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.locations.schemas import UbicacionCreate
from app.modules.organizations.models import Organizacion, Ubicacion


def crear_ubicacion(db: Session, data: UbicacionCreate) -> Ubicacion:
    organizacion = db.get(Organizacion, data.organizacion_id)
    if organizacion is None or organizacion.archived_at is not None:
        raise ValueError("organizacion_no_encontrada")
    ubicacion = Ubicacion(**data.model_dump())
    db.add(ubicacion)
    db.commit()
    db.refresh(ubicacion)
    return ubicacion


def listar_ubicaciones(db: Session, organizacion_id: UUID | None, limit: int = 50, offset: int = 0) -> list[Ubicacion]:
    statement = select(Ubicacion).where(Ubicacion.archived_at.is_(None))
    if organizacion_id is not None:
        statement = statement.where(Ubicacion.organizacion_id == organizacion_id)
    statement = statement.order_by(Ubicacion.nombre).offset(offset).limit(limit)
    return list(db.scalars(statement).all())


def obtener_ubicacion(db: Session, ubicacion_id: UUID) -> Ubicacion | None:
    return db.get(Ubicacion, ubicacion_id)
