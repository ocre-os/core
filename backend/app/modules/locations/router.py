from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.modules.identity.models import Usuario
from app.modules.locations.schemas import UbicacionCreate, UbicacionRead
from app.modules.locations.service import crear_ubicacion, listar_ubicaciones, obtener_ubicacion

router = APIRouter(prefix="/ubicaciones", tags=["ubicaciones"])


@router.post("", response_model=UbicacionRead, status_code=status.HTTP_201_CREATED)
def crear(payload: UbicacionCreate, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    try:
        return crear_ubicacion(db, payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.get("", response_model=list[UbicacionRead])
def listar(
    db: Annotated[Session, Depends(get_db)],
    user: Annotated[Usuario, Depends(get_current_user)],
    organizacion_id: UUID | None = Query(default=None),  # noqa: B008
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
) -> list[object]:
    return listar_ubicaciones(db, organizacion_id, limit, offset)


@router.get("/{ubicacion_id}", response_model=UbicacionRead)
def obtener(ubicacion_id: UUID, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    ubicacion = obtener_ubicacion(db, ubicacion_id)
    if ubicacion is None or ubicacion.archived_at is not None:
        raise HTTPException(status_code=404, detail="ubicacion_no_encontrada")
    return ubicacion
