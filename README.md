# core
Core Repository for OCRE OS
Ocre OS es el sistema operativo interno de la empresa Ocre, diseñado para gestionar servicios técnicos, expedientes de máquinas y generación de reportes profesionales desde el campo. Objetivo, convertir el conocimiento técnico en procesos repetibles y escalables, mejorando rapidez, consistencia y capacidad de cobro.

Clientes. datos fiscales y de contacto. máquinas asociadas, historial de servicios. Máquinas, modelo, serie, configuración, fotos, notas técnicas, historial. Servicios, apertura de caso, diagnóstico, actividades, tiempos, refacciones, evidencias. Reportes, generación automática en PDF, listo para enviar y soportar el cobro.

## Desarrollo local

Requisitos: Git, Docker Engine y Docker Compose v2. En WSL2, Docker debe estar
activo y el usuario debe pertenecer al grupo `docker`. No se requiere Docker Desktop.
Si acabas de incorporarte al grupo, abre una nueva sesión o ejecuta `newgrp docker`.

Desde `~/src/ocre-os/core`, en la rama `feat/v0-foundation`:

```bash
# Solo la primera vez; conserva tu .env si ya existe.
cp --update=none .env.example .env
chmod 600 .env
docker compose config --quiet
docker compose up -d --build --wait
docker compose ps
curl --fail http://127.0.0.1:8000/health
```

La API está en <http://127.0.0.1:8000/docs>. `/health/live` verifica el proceso;
`/health` verifica también la conexión a PostgreSQL. Las migraciones se aplican
antes de arrancar la API. PostgreSQL conserva sus datos en el volumen `postgres_data`.

Este Compose es exclusivamente de desarrollo: tiene recarga de código, credenciales
de ejemplo y puertos limitados a localhost. La autenticación interna está activa:
el primer usuario se registra una sola vez y las rutas de organizaciones requieren
un token Bearer. Usa datos ficticios y conserva `.env` fuera de Git. En un entorno
real cambia `OCRE_AUTH_SECRET` por un valor aleatorio largo.
Si cambias las credenciales locales, mantén `POSTGRES_*` y `DATABASE_URL` coherentes;
los caracteres especiales de la URL deben codificarse como URL. Cambiar `.env` no
cambia la contraseña de una base ya inicializada.

## Verificaciones

La imagen de desarrollo instala el extra `dev` de `backend/pyproject.toml`.

```bash
docker compose exec -T api alembic current
docker compose exec -T api alembic check
docker compose exec -T api python -m pytest -q -p no:cacheprovider
docker compose exec -T -e OCRE_RUN_DB_TESTS=1 api python -m pytest -q -p no:cacheprovider
docker compose exec -T api ruff check --no-cache app migrations tests
docker compose exec -T api python -m pip check
docker compose exec -T -e PYTHONPYCACHEPREFIX=/tmp/ocre-pycache api python -m compileall -q app migrations tests
```

Las pruebas de PostgreSQL requieren permiso para crear bases, disponible con el
usuario del Compose local. Crean bases `ocre_test_<uuid>` independientes y las
eliminan al terminar; prueban migraciones, reversión y persistencia HTTP sin alterar
los datos de desarrollo. No ejecutes estas pruebas contra producción. Sin
`OCRE_RUN_DB_TESTS=1`, se omiten las dos pruebas de integración.

Para comprobar la imagen sin las herramientas de desarrollo:

```bash
docker build --target runtime -t ocre-os-api:local ./backend
```

Para detener el entorno conservando los datos:

```bash
docker compose stop
```

Consulta [la validación técnica local](docs/validacion-local-v0.md) para conocer
el alcance probado y los pendientes de la base V0.
