from datetime import UTC, datetime
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import (
    create_access_token,
    get_current_user,
    hash_password,
    require_role,
    verify_password,
)
from app.modules.identity.models import Usuario
from app.modules.identity.schemas import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserCreateRequest,
    UserRead,
)

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest, db: Annotated[Session, Depends(get_db)]) -> Usuario:
    if db.scalar(select(func.count()).select_from(Usuario)):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="registro_cerrado")
    user = Usuario(email=payload.email.lower(), password_hash=hash_password(payload.password), nombre_mostrado=payload.nombre_mostrado, rol="admin")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Annotated[Session, Depends(get_db)]) -> TokenResponse:
    user = db.scalar(select(Usuario).where(Usuario.email == payload.email.lower()))
    if user is None or not user.activo or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="credenciales_invalidas")
    user.ultimo_acceso_at = datetime.now(UTC)
    db.commit()
    return TokenResponse(access_token=create_access_token(user.id))


@router.get("/me", response_model=UserRead)
def me(user: Annotated[Usuario, Depends(get_current_user)]) -> Usuario:
    return user


@router.post("/users", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(
    payload: UserCreateRequest,
    db: Annotated[Session, Depends(get_db)],
    admin: Annotated[Usuario, Depends(require_role("admin"))],
) -> Usuario:
    if db.scalar(select(Usuario).where(Usuario.email == payload.email.lower())) is not None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email_ya_registrado")
    user = Usuario(email=payload.email.lower(), password_hash=hash_password(payload.password), nombre_mostrado=payload.nombre_mostrado, rol=payload.rol)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get("/users", response_model=list[UserRead])
def list_users(
    db: Annotated[Session, Depends(get_db)],
    admin: Annotated[Usuario, Depends(require_role("admin"))],
) -> list[Usuario]:
    return list(db.scalars(select(Usuario).order_by(Usuario.email)).all())
