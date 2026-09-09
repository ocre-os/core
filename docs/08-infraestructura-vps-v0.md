# Infraestructura VPS V0 de Ocre OS

**Estado:** Borrador implementable  
**Versión:** 0.1

## 1. Objetivo

Definir los requisitos mínimos y recomendados para desplegar Ocre OS V0 en un VPS con una base suficientemente estable para desarrollo, staging y producción inicial.

Esta especificación deriva de la arquitectura técnica V0:

- backend FastAPI;
- PostgreSQL;
- frontend Next.js;
- despliegue en contenedores;
- almacenamiento de archivos fuera de PostgreSQL mediante servicio compatible con S3;
- generación de PDF desde backend;
- sin Redis, Kubernetes ni microservicios en V0.

---

## 2. Perfil recomendado del VPS

Para ejecutar producción y staging iniciales en el mismo servidor, además del panel de despliegue y los builds:

- **CPU:** 4 vCPU;
- **RAM:** 8 GB;
- **Disco:** 80 GB NVMe mínimo; 160 GB recomendado para mayor margen operativo;
- **Arquitectura:** amd64 / x86_64;
- **Red:** IPv4 pública dedicada;
- **Transferencia:** 1 TB mensual o superior;
- **Sistema operativo:** Ubuntu Server 24.04 LTS 64-bit;
- **Acceso:** SSH con usuario root o usuario con sudo;
- **Snapshots del proveedor:** habilitados cuando estén disponibles.

### Perfil mínimo aceptable

Para una instalación temporal o de bajo presupuesto:

- 2 vCPU;
- 4 GB RAM;
- 80 GB SSD/NVMe.

Este perfil puede funcionar para el V0, pero tendrá menos margen durante builds, generación de PDF, actualizaciones y ejecución simultánea de staging y producción.

---

## 3. Capacidad de expansión

La infraestructura debe permitir aumentar CPU, RAM o disco sin reinstalar la aplicación.

No se requiere inicialmente balanceo de carga ni múltiples nodos.

El primer escalamiento esperado será vertical.

---

## 4. Servicios previstos

El servidor podrá ejecutar inicialmente:

- plataforma de despliegue y proxy inverso;
- backend FastAPI;
- frontend Next.js cuando esté disponible;
- PostgreSQL de producción;
- PostgreSQL o base separada de staging;
- tareas de migración;
- logs de aplicación;
- procesos temporales de build.

Las fotografías, videos, PDFs y otros archivos operativos no deberán depender del disco local del VPS como única copia.

---

## 5. Despliegue

Se recomienda utilizar Coolify como capa de despliegue, sin hacer que la arquitectura de Ocre OS dependa funcionalmente de Coolify.

Coolify proporcionará inicialmente:

- despliegue desde GitHub;
- administración de variables de entorno;
- proxy inverso;
- HTTPS;
- logs;
- despliegues separados para staging y producción;
- administración de servicios y bases de datos.

El código seguirá siendo ejecutable mediante Docker sin Coolify.

---

## 6. Puertos y exposición pública

En operación normal deberán exponerse públicamente únicamente:

- `22/tcp` — SSH, preferentemente restringido;
- `80/tcp` — HTTP para redirección y validación de certificados;
- `443/tcp` — HTTPS.

PostgreSQL no deberá quedar accesible desde Internet.

Los puertos internos del backend tampoco deberán exponerse directamente una vez configurado el proxy inverso.

Durante instalación pueden requerirse puertos temporales de administración; deberán revisarse y limitarse después del aprovisionamiento.

---

## 7. DNS propuesto

Se recomienda reservar un espacio de nombres específico para Ocre OS.

Ejemplo conceptual:

- `os.ocre.mx` — aplicación de producción;
- `api.os.ocre.mx` — API de producción;
- `staging.os.ocre.mx` — aplicación de staging;
- `api-staging.os.ocre.mx` — API de staging;
- `deploy.os.ocre.mx` — panel de despliegue si se utiliza Coolify self-hosted.

Los nombres definitivos se decidirán antes de configurar DNS.

---

## 8. Seguridad inicial obligatoria

Antes de almacenar datos reales:

- autenticación SSH mediante clave;
- deshabilitar o limitar acceso SSH por contraseña después de validar la clave;
- firewall activo;
- PostgreSQL sin puerto público;
- secretos fuera del repositorio;
- credenciales diferentes para staging y producción;
- HTTPS válido;
- actualizaciones de seguridad del sistema;
- contraseñas aleatorias de alta entropía;
- revisión de usuarios y permisos;
- logs de acceso y errores.

---

## 9. Respaldo

Antes de convertir Ocre OS en fuente única de información deberán existir:

### PostgreSQL

- respaldo automático diario;
- copia fuera del VPS;
- retención de varias versiones;
- cifrado cuando corresponda;
- restauración probada.

### Archivos

- almacenamiento compatible con S3;
- versionado o política de respaldo apropiada;
- no depender del volumen Docker local como única copia.

### VPS

Los snapshots del proveedor son una capa adicional, no sustituyen los respaldos de PostgreSQL ni del almacenamiento de objetos.

---

## 10. Staging y producción

Durante V0 ambos ambientes pueden compartir un VPS si permanecen aislados mediante:

- bases de datos diferentes;
- credenciales diferentes;
- variables de entorno diferentes;
- dominios diferentes;
- servicios/contenedores diferentes.

Nunca se utilizarán datos de producción como conjunto de prueba destructiva.

---

## 11. Criterio para iniciar producción real

No se considera suficiente que los contenedores simplemente arranquen.

Antes de almacenar información operacional única deberán comprobarse en staging al menos:

1. despliegue reproducible desde GitHub;
2. conexión a PostgreSQL;
3. aplicación correcta de migraciones;
4. health check;
5. creación y lectura de registros básicos;
6. persistencia después de reiniciar contenedores;
7. HTTPS;
8. respaldo de PostgreSQL;
9. restauración de un respaldo en un ambiente aislado;
10. ausencia de PostgreSQL y servicios internos expuestos públicamente.

La prueba local puede omitirse, pero estas verificaciones no deben eliminarse: se trasladan al ambiente staging del VPS.

---

## 12. Nota sobre el Compose de desarrollo

El `docker-compose.yml` de la rama inicial es para desarrollo y no deberá desplegarse sin endurecimiento en producción.

Entre otras diferencias, producción no deberá utilizar:

- `--reload` en Uvicorn;
- bind mount del código fuente;
- contraseña por defecto;
- puerto PostgreSQL publicado a Internet;
- puerto directo de API como interfaz pública permanente.

Se definirá una configuración de producción específica durante el aprovisionamiento del VPS.

---

## 13. Próximo paso operativo

1. seleccionar proveedor y región del VPS;
2. contratar una instancia que cumpla el perfil recomendado;
3. registrar clave SSH;
4. instalar y endurecer el sistema base;
5. instalar la plataforma de despliegue;
6. conectar GitHub;
7. desplegar staging antes de producción;
8. configurar DNS, HTTPS y respaldos;
9. validar el recorrido mínimo del V0 en staging.
