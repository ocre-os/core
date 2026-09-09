from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.modules.equipment.models import Equipo, EquipoOrganizacion, EquipoUbicacion
from app.modules.equipment.schemas import (
    EquipoCreate,
    EquipoOrganizacionCreate,
    EquipoUbicacionCreate,
)
from app.modules.organizations.models import Organizacion, Ubicacion


def crear_equipo(db: Session, data: EquipoCreate) -> Equipo:
    equipo = Equipo(**data.model_dump())
    db.add(equipo)
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise ValueError("codigo_ya_registrado") from exc
    db.refresh(equipo)
    return equipo


def listar_equipos(db: Session, limit: int, offset: int) -> list[Equipo]:
    return list(db.scalars(select(Equipo).where(Equipo.archived_at.is_(None)).order_by(Equipo.codigo).offset(offset).limit(limit)).all())


def obtener_equipo(db: Session, equipo_id: UUID) -> Equipo | None:
    return db.get(Equipo, equipo_id)


def vincular_organizacion(db: Session, equipo: Equipo, data: EquipoOrganizacionCreate) -> EquipoOrganizacion:
    if (org := db.get(Organizacion, data.organizacion_id)) is None or org.archived_at is not None:
        raise ValueError("organizacion_no_encontrada")
    relation = EquipoOrganizacion(equipo_id=equipo.id, **data.model_dump())
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return relation


def vincular_ubicacion(db: Session, equipo: Equipo, data: EquipoUbicacionCreate) -> EquipoUbicacion:
    location = db.get(Ubicacion, data.ubicacion_id)
    if location is None or location.archived_at is not None:
        raise ValueError("ubicacion_no_encontrada")
    active = db.scalar(select(EquipoUbicacion).where(EquipoUbicacion.equipo_id == equipo.id, EquipoUbicacion.hasta.is_(None)))
    if active is not None:
        raise ValueError("equipo_ya_tiene_ubicacion_activa")
    relation = EquipoUbicacion(equipo_id=equipo.id, **data.model_dump())
    db.add(relation)
    db.commit()
    db.refresh(relation)
    return relation
