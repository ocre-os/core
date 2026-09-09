from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class OrganizacionCreate(BaseModel):
    nombre_comercial: str
    nombre_legal: str | None = None
    telefono_principal: str | None = None
    email_general: EmailStr | None = None
    sitio_web: str | None = None
    estado_relacion: str | None = "cliente"
    notas: str | None = None


class OrganizacionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    nombre_comercial: str
    nombre_legal: str | None
    telefono_principal: str | None
    email_general: str | None
    sitio_web: str | None
    estado_relacion: str | None
    notas: str | None
    created_at: datetime
    updated_at: datetime
