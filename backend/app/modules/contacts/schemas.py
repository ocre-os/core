from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ContactoCreate(BaseModel):
    nombre: str = Field(min_length=1, max_length=160)
    apellidos: str | None = Field(default=None, max_length=200)
    telefono_principal: str | None = Field(default=None, max_length=40)
    whatsapp: str | None = Field(default=None, max_length=40)
    email_principal: str | None = Field(default=None, max_length=320)
    notas: str | None = None


class ContactoRead(ContactoCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    archived_at: datetime | None
    created_at: datetime
    updated_at: datetime


class ContactoOrganizacionCreate(BaseModel):
    organizacion_id: UUID
    area: str | None = Field(default=None, max_length=120)
    cargo: str | None = Field(default=None, max_length=160)
    roles: list[str] = Field(default_factory=list, max_length=10)
    es_contacto_principal: bool = False
    puede_solicitar_servicio: bool = True
    puede_autorizar: bool = False
    notas: str | None = None


class ContactoOrganizacionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    contacto_id: UUID
    organizacion_id: UUID
    area: str | None
    cargo: str | None
    es_contacto_principal: bool
    puede_solicitar_servicio: bool
    puede_autorizar: bool
    notas: str | None
