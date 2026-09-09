from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class OrganizacionCreate(BaseModel):
    nombre_comercial: str = Field(max_length=200)
    nombre_legal: str | None = Field(default=None, max_length=250)
    telefono_principal: str | None = Field(default=None, max_length=40)
    email_general: str | None = Field(default=None, max_length=320)
    sitio_web: str | None = Field(default=None, max_length=500)
    estado_relacion: str | None = Field(default="cliente", max_length=60)
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
