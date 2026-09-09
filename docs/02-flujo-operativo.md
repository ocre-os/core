# Flujo Operativo de Ocre OS

**Estado:** Borrador  
**Versión:** 0.1

## 1. Propósito

Definir el ciclo de vida de una atención dentro de Ocre OS, desde el primer contacto hasta la documentación y seguimiento del trabajo realizado.

---

## 2. Cadena principal

El flujo general de atención es:

Interacción
→ Clasificación inicial
→ Solicitud
→ Caso
→ Servicio
→ Visita
→ Reporte
→ Seguimiento o cierre

Esta cadena representa una secuencia lógica del negocio y no una relación obligatoria uno a uno entre objetos.

Una interacción puede relacionarse directamente con información ya existente y no necesariamente generar una nueva Solicitud o un nuevo Caso.

Ejemplos:

- una interacción puede generar una nueva Solicitud;
- una interacción puede agregarse a un Caso existente;
- una Solicitud puede resolverse sin requerir una visita;
- un Caso puede contener múltiples Servicios;
- un Servicio puede requerir múltiples Visitas;
- una Visita puede generar uno o varios Reportes;
- un Caso cerrado puede reabrirse posteriormente.

Ocre OS debe preservar la continuidad de la información independientemente del camino que siga cada atención.

---

## 3. Contacto 0

### Propósito

Registrar toda nueva interacción entrante que todavía no ha sido clasificada dentro del contexto existente de Ocre OS.

Un Contacto 0 puede corresponder tanto a una persona desconocida como a un cliente, contacto, organización, solicitud o caso ya existente.

El sistema no debe asumir que una nueva interacción representa necesariamente una nueva persona, una nueva solicitud o un nuevo caso.

### Entra cuando

Ocre recibe una nueva interacción por cualquier canal, por ejemplo:

- llamada;
- WhatsApp;
- correo electrónico;
- formulario;
- mensaje desde el portal;
- referencia;
- contacto presencial;
- u otro medio.

### Debe conservar como mínimo

- fecha y hora;
- canal;
- identificador disponible del origen;
- contenido o resumen de la interacción;
- información proporcionada;
- origen o referencia, cuando exista;
- y responsable de clasificación o seguimiento.

### Durante su clasificación

El sistema deberá intentar determinar si la interacción corresponde a:

- una persona ya existente;
- una organización existente;
- una solicitud existente;
- un caso existente;
- una nueva necesidad;
- una nueva persona u organización;
- o información que no requiere acción adicional.

### Regla de conservación

Una interacción nunca debe eliminarse únicamente porque la información asociada ya exista.

Cuando una interacción corresponda a información existente, deberá relacionarse con el registro correcto y conservarse como parte de su historial.

Ejemplos:

- un cliente vuelve a preguntar por una solicitud ya abierta;
- una persona genera nuevamente una solicitud porque no encontró cómo dar seguimiento a la anterior;
- un operador utiliza un canal diferente para consultar el mismo caso;
- un cliente vuelve a proporcionar datos que ya estaban registrados;
- una persona intenta contactar varias veces antes de recibir respuesta.

Estas interacciones pueden no generar una nueva solicitud ni un nuevo caso, pero constituyen información operativa relevante.

### Resultado posible

Un Contacto 0 puede:

- generar una nueva Solicitud;
- relacionarse con una Solicitud existente;
- relacionarse con un Caso existente;
- actualizar información de un Contacto u Organización;
- generar una acción de seguimiento;
- registrarse únicamente como interacción;
- o cerrarse sin acción posterior.

### Principio

**Cerrar un Contacto 0 no significa descartar la interacción.**

El registro debe permanecer disponible para trazabilidad y análisis histórico.

## 3.1 Interacción

### Definición

Evento de comunicación entre una persona y Ocre.

Una interacción puede producirse mediante cualquier canal y puede estar relacionada con:

- un Contacto;
- una Organización;
- una Solicitud;
- un Caso;
- una cita;
- un servicio;
- o ningún elemento identificado todavía.

### Propósito

Mantener un historial cronológico de comunicaciones sin obligar a que cada comunicación genere un nuevo objeto de negocio.

### Valor futuro

El historial de interacciones podrá utilizarse para analizar:

- frecuencia de contacto;
- tiempos de respuesta;
- reincidencia de consultas;
- dificultades para utilizar la plataforma;
- necesidades de capacitación;
- efectividad de canales;
- y calidad del seguimiento.

## 3.2 Clasificación inicial

### Propósito

Determinar a qué elemento del sistema pertenece una nueva Interacción y qué acción debe realizarse como consecuencia.

La clasificación inicial evita generar innecesariamente nuevas Solicitudes o Casos cuando la comunicación corresponde a información ya existente.

### Durante la clasificación se debe intentar determinar

- quién está realizando la interacción;
- a qué Organización pertenece;
- si existe un Equipo relacionado;
- si existe una Solicitud relacionada;
- si existe un Caso relacionado;
- cuál es la necesidad expresada;
- si existe una atención anterior potencialmente relacionada;
- y cuál debe ser la siguiente acción.

### Resultados posibles

Una Interacción clasificada puede:

- generar una nueva Solicitud;
- agregarse a una Solicitud existente;
- agregarse a un Caso existente;
- provocar la reapertura provisional de un Caso;
- actualizar información existente;
- generar un Pendiente;
- registrarse únicamente como comunicación;
- o cerrarse sin requerir otra acción.

### Principio

La clasificación debe ocurrir antes de decidir automáticamente que una nueva comunicación representa un nuevo Caso.

Cuando exista incertidumbre razonable sobre su relación con un Caso anterior, deberá preservarse inicialmente la continuidad del historial hasta obtener evidencia suficiente para clasificarla correctamente.

---

## 4. Solicitud

### Entra cuando
Existe una necesidad suficientemente clara como para requerir análisis, respuesta, seguimiento o ejecución.

### Debe conservar
- quién solicita;
- qué expresó originalmente;
- necesidad percibida;
- organización, si se conoce;
- equipo, si se conoce;
- urgencia;
- evidencia inicial;
- siguiente acción.

### Sale cuando
La atención requiere seguimiento estructurado.

### Resultado posible
- creación de Caso;
- resolución directa;
- rechazo;
- espera de información;
- espera de autorización.

---

## 5. Caso

### Propósito
Agrupar todo el seguimiento relacionado con una necesidad concreta.

### Puede contener
- comunicaciones;
- solicitudes;
- servicios;
- cotizaciones;
- pagos;
- citas;
- visitas;
- reportes;
- refacciones;
- pendientes;
- decisiones;
- evidencias.

### Regla provisional
Un Caso representa continuidad de atención, no una sola actividad.

### Estados preliminares
- nuevo;
- pendiente de información;
- pendiente de cotización;
- pendiente de anticipo;
- agendado;
- en atención;
- esperando refacción;
- esperando respuesta del cliente;
- pendiente de validación;
- cerrado;
- cancelado.

Estos estados deberán validarse con procesos reales antes de considerarse definitivos.

---

## 6. Servicio

### Propósito
Representar trabajo profesional específico ejecutado por Ocre.

### Ejemplos
- Diagnóstico General Inicial;
- reparación;
- mantenimiento;
- calibración;
- instalación;
- capacitación;
- modificación;
- consultoría.

### Regla
Un Caso puede contener uno o varios Servicios.

Un Servicio puede requerir una o varias Visitas.

---

## 7. Visita

### Propósito
Representar una intervención programada en una ubicación o mediante una sesión remota.

### Debe registrar
- fecha;
- horario;
- ubicación;
- técnicos participantes;
- actividades;
- tiempos;
- evidencias;
- mediciones;
- hallazgos;
- intervenciones;
- pendientes;
- resultado.

### Regla
Una visita no equivale necesariamente a un servicio completo.

---

## 8. Reporte

### Propósito
Comunicar formalmente al cliente el trabajo realizado y su resultado.

### Debe poder derivarse de
- una Visita;
- un Servicio;
- una etapa del Caso;
- o el cierre completo del Caso.

### Debe reflejar
- solicitud original;
- necesidad identificada;
- equipo atendido;
- diagnóstico;
- actividades;
- evidencias;
- intervenciones;
- resultados;
- pendientes;
- recomendaciones;
- estado final.

---

## 9. Transiciones

Las transiciones entre etapas deben ocurrir por eventos reales del negocio.

Ejemplos:

- Contacto 0 → Solicitud:
  se identifica una necesidad concreta.

- Solicitud → Caso:
  la necesidad requiere seguimiento estructurado.

- Caso → Servicio:
  se autoriza o define una actividad técnica concreta.

- Servicio → Visita:
  se programa ejecución presencial o remota.

- Visita → Reporte:
  existe información suficiente para documentar lo realizado.

- Caso → Cerrado:
  no quedan acciones dentro del alcance acordado.

---

## 10. Principio de no pérdida de contexto

La información obtenida en una etapa no debe descartarse cuando el proceso avanza.

Cada transición debe enriquecer el historial y mantener trazabilidad completa.
