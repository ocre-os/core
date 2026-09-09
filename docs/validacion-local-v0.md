# Validación técnica local V0

Fecha: 2026-09-09. Rama: `feat/v0-foundation`.

## Entorno verificado

- Windows 11 Pro, versión 10.0.26200; ThinkPad X280.
- Ubuntu 24.04.4 LTS sobre kernel WSL2 6.18.33.2, con systemd.
- Intel i5-8350U, 4 núcleos / 8 hilos; aproximadamente 16 GB físicos.
- WSL dispone de 7,7 GiB de RAM y 2 GiB de swap.
- Git 2.43.0, curl 8.5.0 y ca-certificates ya estaban instalados.
- Docker Engine 29.1.3 y Compose 2.40.3 instalados desde Ubuntu
  (`docker.io`, `docker-compose-v2`); servicio habilitado y activo.
- GitHub CLI 2.45.0 instalado para autenticar Git desde el navegador.
- El usuario `ocre` pertenece al grupo `docker`. La sesión del agente, abierta
  antes del cambio, utiliza `sg docker -c 'docker ...'` sin sudo.
- No se instaló Docker Desktop, Coolify, Redis ni Kubernetes.
- Dependencias resueltas dentro de las imágenes: FastAPI 0.141.1,
  SQLAlchemy 2.0.52, Alembic 1.19.2 y psycopg 3.3.5; pytest 8.4.2 en desarrollo.
- Autenticación local con hash `scrypt`, tokens HMAC con expiración y registro
  inicial de un único usuario mientras la tabla `usuario` está vacía.

## Alcance y documentación

Se revisaron los documentos 00–07: modelo operativo, glosario, flujo, reglas,
dominio, MVP, datos V0 y arquitectura técnica. No existe un documento específico
de infraestructura VPS V0 en esta rama.

La implementación corresponde a la base técnica: FastAPI, PostgreSQL 16,
SQLAlchemy 2.x, Alembic y un monolito modular. Existen las 12 tablas previstas
para identidad operativa y endpoints de alta, listado y consulta de organizaciones.
`archivo` almacena metadatos y `storage_key`, sin blobs; el servicio de almacenamiento
de archivos todavía no está implementado. El ciclo operativo completo del MVP
no está implementado y no forma parte de esta validación de bootstrap.

## Fallos reproducidos y correcciones

1. Compose fallaba sin `.env`. Se creó una copia local del ejemplo, ignorada por
   Git, con permisos 600; el README ahora documenta ese paso.
2. Alembic rechazaba URLs con `%` por interpolación de ConfigParser. Se escapó
   ese carácter al introducir la URL en la configuración de Alembic.
3. Seis campos de entrada de organizaciones aceptaban longitudes que PostgreSQL
   rechazaba, provocando HTTP 500. Los contratos Pydantic ahora aplican los límites
   existentes del esquema y devuelven HTTP 422.
4. `alembic check` detectaba restricciones únicas redundantes para `equipo.codigo`
   y `usuario.email`. La revisión `20260909_0001a` elimina solo las restricciones
   duplicadas; los índices únicos existentes siguen protegiendo los valores.
   La revisión original conserva su SQL; solo se ordenaron imports.
5. Los tipos de retorno de las rutas describían esquemas Pydantic, aunque retornan
   modelos ORM. Se corrigieron las anotaciones y se usó `Annotated` para dependencias.
6. Compose publicaba PostgreSQL y una API sin autenticación en todas las interfaces.
   Se limitaron ambos puertos a `127.0.0.1` y se añadió el health check de la API.
7. La imagen original no incluía las dependencias opcionales de pruebas. Compose
   utiliza ahora el target `development`; el target `runtime` conserva únicamente
   las dependencias de ejecución. Se añadió `.dockerignore`.

## Verificaciones

Los comandos reproducibles están en el README. Se comprobaron:

- configuración de Compose y construcción de contenedores;
- construcción del target `runtime` y arranque de su comando predeterminado en
  un contenedor temporal sin montajes; health HTTP 200, importación de todos los
  módulos de `app` y ausencia de pytest en esa imagen;
- PostgreSQL 16.15, migración inicial y revisión correctiva;
- coincidencia del esquema con los modelos mediante `alembic check`;
- repetición de `upgrade head` y ciclo `downgrade base` / `upgrade head` en bases
  temporales independientes, nunca sobre los datos de desarrollo;
- arranque de FastAPI y respuestas HTTP 200 de `/health`, `/health/live` y OpenAPI;
- persistencia, lectura, paginación, archivo lógico y errores 404/422 de organizaciones;
- rechazo de seis campos demasiado largos y aceptación de sus longitudes máximas;
- URL codificada de Alembic y respuesta 503 sin filtrar detalles internos;
- registro inicial, rechazo del segundo registro, login correcto/incorrecto,
  `/auth/me`, protección de organizaciones, token inválido y auditoría de alta;
- Ruff, `pip check` y compilación de Python.

La suite ampliada contiene 11 casos, incluidos los dos de integración optativa.
Antes de las correcciones, las siete regresiones nuevas fallaban y la prueba
original de liveness pasaba. Después de corregir, los 11 casos pasan.
Las bases temporales se eliminan al finalizar; no se cargaron organizaciones
de prueba en la base de desarrollo.

Estado final: únicamente `core-api-1` y `core-db-1` activos y saludables, revisión
`20260909_0001a` aplicada. No quedan bases `ocre_test_*` ni el contenedor temporal.
La validación se realizó en `feat/v0-foundation`. Los commits de cierre se
identifican en el historial Git de la rama; la integración a `main` requiere revisión.

## Pendientes para revisión antes del siguiente incremento

Estos puntos se reportan sin rediseñar el dominio ni añadir funcionalidades:

- **Seguridad:** la autenticación interna mínima ya está activa, pero faltan
  autorización por rol/organización, rotación y revocación de tokens. El usuario
  de PostgreSQL del Compose es administrador y el backend ejecuta como root dentro
  del contenedor. Esta configuración es local, no una configuración de producción.
- **Integridad documentada todavía no implementada:** no hay restricciones
  `hasta >= desde` en relaciones de equipos, ni garantía de una sola ubicación
  activa o un solo perfil fiscal predeterminado. Definir su implementación antes
  de habilitar escrituras funcionales sobre esas entidades.
- **Trazabilidad:** existe `AuditUserMixin`, pero las entidades no lo utilizan;
  faltan `created_by`/`updated_by` y la identidad autenticada que los complete.
- **Roles:** el contrato de alta usa `estado_relacion="cliente"` por defecto,
  mientras el dominio también tiene `organizacion_rol`. Revisar el significado
  y valor inicial antes de ampliar la API; se conservó el comportamiento actual.
- **Conservación:** varias FKs tienen `ON DELETE CASCADE`. No hay endpoint de
  borrado, pero un borrado SQL directo puede eliminar relaciones históricas.
- **Reproducibilidad exacta:** las versiones Python tienen rangos y las imágenes
  usan etiquetas móviles, sin lockfile ni digests fijados. El bootstrap se puede
  repetir con los comandos documentados, pero una reconstrucción futura puede
  resolver otras versiones. La suite actual emite dos avisos de deprecación de
  Starlette/TestClient relacionados con httpx y AnyIO; no causan fallos.
- **Herramientas de build:** Buildx no está instalado. Compose construyó las
  imágenes y `docker build` completó con el constructor legacy; se observaron
  advertencias sobre Bake/Buildx y deprecación del constructor legacy. No se
  añadió otro paquete al equipo en esta etapa.
- **Producción y operación real:** faltan backups/restauración probada, logs
  estructurados, almacenamiento de archivos, autenticación y el resto del MVP.
- **Documentación:** falta infraestructura VPS V0. El glosario define Visita como
  presencia física, mientras flujo/dominio/datos admiten también sesiones remotas;
  conviene armonizarlo antes de implementar ese módulo.
- **Capacidad:** quedan aproximadamente 48 GiB en C:. El espacio libre aparente
  del disco virtual Linux no representa capacidad física adicional. Vigilar
  imágenes, caché de builds y volúmenes a medida que crezca el proyecto.

## Resultado de la revisión para cierre de foundation

Las correcciones revisadas permiten cerrar el alcance de bootstrap local descrito
en la sección 14 de `07-arquitectura-tecnica-v0.md`. Las pruebas de ejecución no
equivalen a aprobar el MVP para uso con datos reales.

Los siguientes pendientes técnicos ya tienen una regla documentada; no requieren
inventar una política de negocio:

- implementar `hasta >= desde` en las relaciones temporales de equipos
  (`06-modelo-de-datos-v0.md`, sección 19);
- garantizar un perfil fiscal predeterminado por organización y una ubicación
  activa por equipo (secciones 6.6 y 7.4 del mismo documento);
- incorporar autenticación y autores de cambios antes de usar datos reales
  (`07-arquitectura-tecnica-v0.md`, sección 7).

Antes de ampliar las funcionalidades, sí requieren revisión de significado:

- diferenciar `estado_relacion` de los roles y decidir el valor inicial de alta;
- armonizar la definición de Visita física/remota entre los documentos;
- definir el tratamiento de correcciones y conservación del historial antes de
  ofrecer operaciones de borrado.

Estos puntos quedan fuera de los commits de corrección de bootstrap. Deben
seguirse en el siguiente incremento, con pruebas de sus reglas y revisión del dominio.
