from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.organizations.models import Organizacion
from app.modules.organizations.schemas import OrganizacionCreate


def crear_organizacion(db: Session, data: OrganizacionCreate, user_id: UUID) -> Organizacion:
    organizacion = Organizacion(**data.model_dump(), created_by=user_id, updated_by=user_id)
    db.add(organizacion)
    db.commit()
    db.refresh(organizacion)
    return organizacion


def obtener_organizacion(db: Session, organizacion_id: UUID) -> Organizacion | None:
    return db.get(Organizacion, organizacion_id)


def listar_organizaciones(db: Session, limit: int = 50, offset: int = 0) -> list[Organizacion]:
    statement = (
        select(Organizacion)
        .where(Organizacion.archived_at.is_(None))
        .order_by(Organizacion.nombre_comercial)
        .offset(offset)
        .limit(limit)
    )
    return list(db.scalars(statement).all())
