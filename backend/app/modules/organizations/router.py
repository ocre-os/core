from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.modules.organizations.schemas import OrganizacionCreate, OrganizacionRead
from app.modules.organizations.service import (
    crear_organizacion,
    listar_organizaciones,
    obtener_organizacion,
)

router = APIRouter(prefix="/organizaciones", tags=["organizaciones"])


@router.post("", response_model=OrganizacionRead, status_code=status.HTTP_201_CREATED)
def crear(
    payload: OrganizacionCreate,
    db: Session = Depends(get_db),
) -> OrganizacionRead:
    return crear_organizacion(db, payload)


@router.get("", response_model=list[OrganizacionRead])
def listar(
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
) -> list[OrganizacionRead]:
    return listar_organizaciones(db, limit=limit, offset=offset)


@router.get("/{organizacion_id}", response_model=OrganizacionRead)
def obtener(
    organizacion_id: UUID,
    db: Session = Depends(get_db),
) -> OrganizacionRead:
    organizacion = obtener_organizacion(db, organizacion_id)
    if organizacion is None or organizacion.archived_at is not None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="organizacion_no_encontrada")
    return organizacion
