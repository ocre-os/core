from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, model_validator


class EquipoCreate(BaseModel):
    codigo: str = Field(min_length=1, max_length=40)
    tipo_familia: str | None = Field(default=None, max_length=120)
    marca: str | None = Field(default=None, max_length=160)
    modelo: str | None = Field(default=None, max_length=160)
    numero_serie: str | None = Field(default=None, max_length=160)
    descripcion: str | None = None
    estado_operativo: str | None = Field(default=None, max_length=60)
    fecha_alta: datetime
    notas: str | None = None


class EquipoRead(EquipoCreate):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    archived_at: datetime | None


class EquipoOrganizacionCreate(BaseModel):
    organizacion_id: UUID
    tipo_relacion: str = Field(max_length=60)
    desde: datetime
    hasta: datetime | None = None
    notas: str | None = None

    @model_validator(mode="after")
    def fechas_validas(self):
        if self.hasta is not None and self.hasta < self.desde:
            raise ValueError("hasta_no_puede_ser_anterior_a_desde")
        return self


class EquipoOrganizacionRead(EquipoOrganizacionCreate):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    equipo_id: UUID


class EquipoUbicacionCreate(BaseModel):
    ubicacion_id: UUID
    desde: datetime
    hasta: datetime | None = None
    motivo_cambio: str | None = Field(default=None, max_length=250)
    notas: str | None = None

    @model_validator(mode="after")
    def fechas_validas(self):
        if self.hasta is not None and self.hasta < self.desde:
            raise ValueError("hasta_no_puede_ser_anterior_a_desde")
        return self


class EquipoUbicacionRead(EquipoUbicacionCreate):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    equipo_id: UUID
