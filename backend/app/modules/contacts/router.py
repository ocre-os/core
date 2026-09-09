from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user
from app.modules.contacts.schemas import (
    ContactoCreate,
    ContactoOrganizacionCreate,
    ContactoOrganizacionRead,
    ContactoRead,
)
from app.modules.contacts.service import (
    crear_contacto,
    listar_contactos,
    obtener_contacto,
    vincular_organizacion,
)
from app.modules.identity.models import Usuario

router = APIRouter(prefix="/contactos", tags=["contactos"])


@router.post("", response_model=ContactoRead, status_code=status.HTTP_201_CREATED)
def crear(payload: ContactoCreate, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    return crear_contacto(db, payload, user.id)


@router.get("", response_model=list[ContactoRead])
def listar(db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)], limit: int = Query(50, ge=1, le=200), offset: int = Query(0, ge=0)) -> list[object]:
    return listar_contactos(db, limit, offset)


@router.get("/{contacto_id}", response_model=ContactoRead)
def obtener(contacto_id: UUID, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    contacto = obtener_contacto(db, contacto_id)
    if contacto is None or contacto.archived_at is not None:
        raise HTTPException(status_code=404, detail="contacto_no_encontrado")
    return contacto


@router.post("/{contacto_id}/organizaciones", response_model=ContactoOrganizacionRead, status_code=201)
def vincular(contacto_id: UUID, payload: ContactoOrganizacionCreate, db: Annotated[Session, Depends(get_db)], user: Annotated[Usuario, Depends(get_current_user)]) -> object:
    contacto = obtener_contacto(db, contacto_id)
    if contacto is None or contacto.archived_at is not None:
        raise HTTPException(status_code=404, detail="contacto_no_encontrado")
    try:
        return vincular_organizacion(db, contacto, payload)
    except ValueError as exc:
        raise HTTPException(status_code=409 if str(exc).endswith("vinculado") else 404, detail=str(exc)) from exc

