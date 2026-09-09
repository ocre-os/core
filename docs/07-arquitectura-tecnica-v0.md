# Arquitectura Técnica V0 de Ocre OS

**Estado:** Borrador implementable  
**Versión:** 0.1

## 1. Objetivo

Definir una arquitectura técnica suficientemente simple para comenzar a desarrollar Ocre OS inmediatamente, pero con una base que pueda crecer sin reconstruir el sistema cuando aumenten los usuarios, Equipos, archivos y Servicios.

La prioridad técnica del V0 es entregar el corte vertical:

**Organización → Contacto → Equipo → Caso → Servicio → Visita → Reporte → Cobro pendiente**

No se añadirá infraestructura únicamente porque pueda ser útil en el futuro.

---

# 2. Decisiones principales

## 2.1 Repositorio

Se utilizará inicialmente un **monorepositorio**: `ocre-os/core`.

Para el tamaño actual del equipo, separar frontend, backend e infraestructura en repositorios diferentes agregaría coordinación y despliegues innecesarios.

La estructura inicial será:

```text
core/
├─ backend/
├─ frontend/
├─ infra/
├─ docs/
├─ scripts/
├─ docker-compose.yml
├─ .env.example
├─ .gitignore
└─ README.md
```

Si en el futuro existen equipos independientes o ciclos de despliegue muy diferentes, esta decisión podrá revisarse.

---

## 2.2 Backend

**Python + FastAPI**.

Componentes iniciales:

- FastAPI — API HTTP;
- SQLAlchemy 2.x — ORM y unidad de trabajo;
- Alembic — migraciones PostgreSQL;
- Pydantic — contratos y validación;
- psycopg — conexión PostgreSQL;
- autenticación basada en usuario y credenciales seguras;
- generación de PDF a partir de HTML/CSS.

### Motivo

FastAPI ofrece una base pequeña, explícita y adecuada para integrar posteriormente lógica diagnóstica e IA sin obligar al dominio a depender de un framework CRM.

---

## 2.3 Base de datos

**PostgreSQL** será la fuente primaria de datos operativos.

No se utilizará una base NoSQL como almacenamiento principal del dominio.

`JSONB` se reservará para datos técnicos todavía flexibles, por ejemplo `registro_tecnico.datos`.

---

## 2.4 Frontend

**Next.js + React + TypeScript**.

El V0 será una aplicación web responsiva y deberá priorizar el uso desde teléfono.

No se desarrollará una aplicación móvil nativa en la primera etapa.

### Objetivo

La misma interfaz deberá servir inicialmente para:

- escritorio administrativo;
- tableta;
- captura técnica desde teléfono.

Posteriormente podrá habilitarse comportamiento PWA cuando aporte valor real.

---

## 2.5 Archivos y Evidencias

Las fotografías, PDFs y documentos no se guardarán ordinariamente dentro de PostgreSQL.

Se utilizará una abstracción de almacenamiento compatible con S3.

### Desarrollo local

Puede comenzar con almacenamiento local controlado.

### Producción

Se utilizará un almacenamiento de objetos compatible con S3.

El proveedor exacto se elegirá por costo y ubicación cuando se prepare el primer despliegue.

La base de datos guardará metadatos y `storage_key`.

---

## 2.6 PDF

Los Reportes se construirán primero como HTML/CSS y se convertirán a PDF desde el backend.

Tecnología inicial recomendada: **WeasyPrint**.

Esto permitirá diseñar formatos profesionales sin mantener un segundo sistema de plantillas exclusivo para PDF.

La versión emitida deberá guardar:

- snapshot de datos;
- archivo PDF;
- número de versión;
- fecha de emisión.

---

# 3. Infraestructura deliberadamente NO incluida todavía

## 3.1 Redis

Redis **no es necesario para el V0**.

Aunque se había considerado anteriormente, introducirlo ahora agrega infraestructura sin resolver un problema actual.

Se incorporará cuando exista una necesidad concreta como:

- colas de trabajo;
- procesamiento pesado en segundo plano;
- caché con beneficio medible;
- rate limiting distribuido;
- sesiones distribuidas.

## 3.2 Microservicios

No se utilizarán microservicios en el V0.

El backend será un **monolito modular**.

Los límites entre módulos existirán en código, pero compartirán proceso y base de datos mientras esto siga siendo la opción más simple y confiable.

## 3.3 Kubernetes

No se utilizará Kubernetes.

Docker Compose en desarrollo y contenedores administrados en producción son suficientes para el tamaño inicial.

---

# 4. Organización del backend

Estructura propuesta:

```text
backend/
├─ app/
│  ├─ main.py
│  ├─ core/
│  │  ├─ config.py
│  │  ├─ database.py
│  │  ├─ security.py
│  │  └─ ids.py
│  ├─ modules/
│  │  ├─ identity/
│  │  ├─ organizations/
│  │  ├─ equipment/
│  │  ├─ interactions/
│  │  ├─ cases/
│  │  ├─ services/
│  │  ├─ visits/
│  │  ├─ reports/
│  │  ├─ tasks/
│  │  └─ billing/
│  └─ shared/
│     ├─ files/
│     └─ audit/
├─ migrations/
├─ tests/
├─ pyproject.toml
└─ alembic.ini
```

Cada módulo podrá contener inicialmente:

```text
models.py
schemas.py
service.py
router.py
```

No se crearán capas adicionales si todavía no existe una necesidad que las justifique.

---

# 5. Organización del frontend

```text
frontend/
├─ app/
├─ components/
├─ features/
│  ├─ organizations/
│  ├─ contacts/
│  ├─ equipment/
│  ├─ cases/
│  ├─ visits/
│  ├─ reports/
│  └─ tasks/
├─ lib/
├─ public/
└─ package.json
```

El frontend organizará código por función del negocio y no únicamente por tipo visual de componente.

---

# 6. API

La API inicial utilizará HTTP/JSON bajo `/api/v1`.

Ejemplos conceptuales:

```text
POST   /api/v1/organizaciones
GET    /api/v1/organizaciones/{id}
POST   /api/v1/contactos
POST   /api/v1/equipos
POST   /api/v1/interacciones
POST   /api/v1/solicitudes
POST   /api/v1/casos
POST   /api/v1/casos/{id}/servicios
POST   /api/v1/visitas
POST   /api/v1/visitas/{id}/registros-tecnicos
POST   /api/v1/visitas/{id}/evidencias
POST   /api/v1/casos/{id}/reportes
POST   /api/v1/reportes/{id}/emitir
POST   /api/v1/casos/{id}/pendientes
POST   /api/v1/casos/{id}/cobros
```

Los endpoints definitivos se diseñarán mientras se implementa cada corte vertical; esta lista solo establece dirección.

---

# 7. Autenticación y autorización

## V0 interno

La primera versión tendrá autenticación para usuarios internos.

Requisitos mínimos:

- contraseñas con hash robusto;
- sesiones/token con expiración;
- usuario activo/inactivo;
- protección de rutas;
- registro del usuario que crea o modifica información crítica.

## Portal del cliente

No se implementará en la primera entrega interna, pero `Usuario` permanecerá separado de `Contacto` para poder asignar posteriormente permisos sobre Organizaciones específicas.

---

# 8. Configuración y secretos

Toda configuración dependiente del ambiente se administrará mediante variables de entorno.

Nunca se guardarán en GitHub:

- contraseñas reales;
- secretos JWT;
- credenciales de PostgreSQL de producción;
- claves S3;
- claves de proveedores externos.

El repositorio tendrá `.env.example` sin secretos.

---

# 9. Docker

## Desarrollo

`docker-compose.yml` levantará inicialmente:

- PostgreSQL;
- backend.

El frontend podrá ejecutarse localmente durante desarrollo o incorporarse al Compose conforme se estabilice.

## Producción

Cada aplicación tendrá su Dockerfile.

El despliegue podrá ser administrado mediante Coolify u otra plataforma compatible con Docker en el VPS.

La arquitectura no dependerá de Coolify para funcionar.

---

# 10. Entornos

Se contemplan tres ambientes conceptuales:

- `development` — máquina local;
- `staging` — validación antes de producción;
- `production` — datos reales.

Para acelerar el arranque, staging puede compartir inicialmente el mismo VPS de producción mediante servicios y bases separadas, siempre que los datos y credenciales permanezcan aislados.

---

# 11. Respaldo

Antes de utilizar Ocre OS como única fuente de información real deberán existir:

- respaldo automático de PostgreSQL;
- respaldo o versionado de archivos importantes;
- procedimiento probado de restauración.

Tener backups sin haber probado restauración no se considerará una estrategia suficiente.

---

# 12. Observabilidad mínima

V0 debe incluir:

- logs estructurados del backend;
- identificación de errores;
- health check HTTP;
- registro de migración aplicada;
- logs de despliegue.

No se instalará inicialmente una plataforma compleja de observabilidad.

---

# 13. Flujo de desarrollo

Mientras la documentación sea el único contenido modificado, pueden existir commits directos controlados en `main`.

Al comenzar código ejecutable se cambia la regla:

1. crear rama por incremento;
2. implementar;
3. ejecutar pruebas;
4. revisar diff;
5. integrar a `main` mediante Pull Request.

Esto evita convertir `main` en un área experimental conforme el sistema empieza a operar.

---

# 14. Primera rama de implementación

Nombre recomendado:

`feat/v0-foundation`

Objetivo:

1. crear estructura backend/frontend/infra;
2. levantar PostgreSQL local;
3. crear FastAPI con health check;
4. configurar SQLAlchemy y Alembic;
5. generar migración 001 del Modelo de Datos V0;
6. crear primera Organización mediante API;
7. incluir prueba automática básica.

### Criterio de terminación

Desde una computadora de desarrollo debe poder ejecutarse:

```text
docker compose up
```

y obtener una API saludable conectada a PostgreSQL con migraciones aplicables.

---

# 15. Decisiones que no necesitamos tomar todavía

No bloquean la primera rama:

- proveedor definitivo de VPS;
- proveedor definitivo de object storage;
- diseño visual final;
- pasarela de pago;
- integración WhatsApp;
- proveedor de correo transaccional;
- IA utilizada para diagnóstico;
- proveedor de autenticación externo;
- aplicación móvil nativa.

---

# 16. Próximo paso

Crear la rama `feat/v0-foundation` y generar el esqueleto ejecutable del proyecto.

A partir de ese punto el repositorio dejará de contener únicamente especificaciones y empezará a contener Ocre OS ejecutable.
