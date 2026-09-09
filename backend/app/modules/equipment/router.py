from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.modules.equipment.schemas import (
    EquipoCreate,
    EquipoOrganizacionCreate,
    EquipoOrganizacionRead,
    EquipoRead,
    EquipoUbicacionCreate,
    EquipoUbicacionRead,
)
from app.modules.equipment.service import (
    crear_equipo,
    listar_equipos,
    obtener_equipo,
    vincular_organizacion,
    vincular_ubicacion,
)
from app.modules.identity.models import Usuario

router = APIRouter(prefix="/equipos", tags=["equipos"])


def _equipo(db: Session, equipo_id: UUID):
    equipo = obtener_equipo(db, equipo_id)
    if equipo is None or equipo.archived_at is not None:
        raise HTTPException(status_code=404, detail="equipo_no_encontrado")
    return equipo


@router.post("", response_model=EquipoRead, status_code=status.HTTP_201_CREATED)
def crear(payload: EquipoCreate, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    try:
        return crear_equipo(db, payload)
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc)) from exc


@router.get("", response_model=list[EquipoRead])
def listar(db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)], limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)) -> list[object]:
    return listar_equipos(db, limit, offset)


@router.get("/{equipo_id}", response_model=EquipoRead)
def obtener(equipo_id: UUID, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    return _equipo(db, equipo_id)


@router.post("/{equipo_id}/organizaciones", response_model=EquipoOrganizacionRead, status_code=201)
def relacion_organizacion(equipo_id: UUID, payload: EquipoOrganizacionCreate, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    try:
        return vincular_organizacion(db, _equipo(db, equipo_id), payload)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.post("/{equipo_id}/ubicaciones", response_model=EquipoUbicacionRead, status_code=201)
def relacion_ubicacion(equipo_id: UUID, payload: EquipoUbicacionCreate, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    try:
        return vincular_ubicacion(db, _equipo(db, equipo_id), payload)
    except ValueError as exc:
        raise HTTPException(status_code=409 if "activa" in str(exc) else 404, detail=str(exc)) from exc
