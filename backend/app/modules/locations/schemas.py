from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class UbicacionCreate(BaseModel):
    organizacion_id: UUID
    nombre: str = Field(min_length=1, max_length=200)
    direccion_linea_1: str | None = Field(default=None, max_length=250)
    direccion_linea_2: str | None = Field(default=None, max_length=250)
    colonia: str | None = Field(default=None, max_length=160)
    ciudad: str | None = Field(default=None, max_length=160)
    estado_region: str | None = Field(default=None, max_length=160)
    codigo_postal: str | None = Field(default=None, max_length=20)
    pais: str = Field(default="MX", min_length=2, max_length=2)
    referencias_acceso: str | None = None
    horarios: str | None = None
    observaciones_tecnicas: str | None = None


class UbicacionRead(UbicacionCreate):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    archived_at: datetime | None
    created_at: datetime
    updated_at: datetime
