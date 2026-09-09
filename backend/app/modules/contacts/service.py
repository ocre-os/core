from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.contacts.schemas import ContactoCreate, ContactoOrganizacionCreate
from app.modules.organizations.models import (
    Contacto,
    ContactoOrganizacion,
    ContactoOrganizacionRol,
    Organizacion,
)


def crear_contacto(db: Session, data: ContactoCreate, user_id: UUID) -> Contacto:
    contacto = Contacto(**data.model_dump())
    db.add(contacto)
    db.commit()
    db.refresh(contacto)
    return contacto


def listar_contactos(db: Session, limit: int = 50, offset: int = 0) -> list[Contacto]:
    statement = (
        select(Contacto).where(Contacto.archived_at.is_(None))
        .order_by(Contacto.nombre, Contacto.apellidos).offset(offset).limit(limit)
    )
    return list(db.scalars(statement).all())


def obtener_contacto(db: Session, contacto_id: UUID) -> Contacto | None:
    return db.get(Contacto, contacto_id)


def vincular_organizacion(
    db: Session, contacto: Contacto, data: ContactoOrganizacionCreate
) -> ContactoOrganizacion:
    organizacion = db.get(Organizacion, data.organizacion_id)
    if organizacion is None or organizacion.archived_at is not None:
        raise ValueError("organizacion_no_encontrada")
    existing = db.scalar(select(ContactoOrganizacion).where(
        ContactoOrganizacion.contacto_id == contacto.id,
        ContactoOrganizacion.organizacion_id == data.organizacion_id,
    ))
    if existing is not None:
        raise ValueError("contacto_organizacion_ya_vinculado")
    relation = ContactoOrganizacion(
        contacto_id=contacto.id,
        organizacion_id=data.organizacion_id,
        **data.model_dump(exclude={"organizacion_id", "roles"}),
    )
    db.add(relation)
    db.flush()
    for role in data.roles:
        db.add(ContactoOrganizacionRol(contacto_organizacion_id=relation.id, rol=role))
    db.commit()
    db.refresh(relation)
    return relation
