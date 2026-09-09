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

## 9. Transiciones y continuidad de los casos

Las transiciones dentro de Ocre OS deben responder a eventos reales del negocio.

Una nueva interacción no genera automáticamente una nueva Solicitud ni un nuevo Caso.

---

### 9.1 Interacción → Clasificación inicial

Toda nueva comunicación entra primero como Interacción.

Durante su clasificación se determina si corresponde a:

- información nueva;
- una Solicitud existente;
- un Caso existente;
- una necesidad nueva;
- una posible reincidencia;
- o una comunicación que únicamente debe conservarse en el historial.

---

### 9.2 Clasificación inicial → Solicitud

Se genera una nueva Solicitud cuando se identifica una necesidad que:

- no pertenece razonablemente a una Solicitud existente;
- requiere respuesta, análisis, seguimiento o ejecución;
- y posee información suficiente para comenzar su atención.

La Solicitud debe conservar siempre la expresión original de la necesidad del cliente.

---

### 9.3 Solicitud → Caso

Una Solicitud genera un Caso cuando requiere continuidad estructurada de atención.

Un Caso puede incluir:

- comunicaciones;
- investigación;
- diagnóstico;
- cotizaciones;
- pagos;
- agenda;
- servicios;
- visitas;
- refacciones;
- reportes;
- pendientes;
- seguimiento;
- y decisiones.

La creación de un Caso no implica necesariamente que exista todavía un diagnóstico o un servicio autorizado.

---

### 9.4 Caso → Servicio

Se genera o relaciona un Servicio cuando existe una actividad profesional concreta que Ocre deberá ejecutar.

Ejemplos:

- Diagnóstico General Inicial;
- diagnóstico específico;
- reparación;
- mantenimiento;
- calibración;
- modificación;
- instalación;
- capacitación;
- consultoría.

Un mismo Caso puede contener múltiples Servicios.

---

### 9.5 Servicio → Visita

Se genera una Visita cuando una actividad requiere una intervención programada presencial o remota.

Un Servicio puede requerir múltiples Visitas.

Una Visita no implica por sí misma que el Servicio haya concluido.

---

### 9.6 Visita → Reporte

Cuando exista información suficiente sobre el trabajo ejecutado deberá poder generarse un Reporte.

El Reporte debe construirse principalmente a partir de la información capturada durante la operación y no mediante reconstrucción posterior de memoria.

---

## 10. Reincidencias y reapertura de casos

### 10.1 Principio de presunción de continuidad

Cuando exista una nueva incidencia en un Equipo recientemente intervenido y sea lógica o técnicamente posible una relación con el trabajo anterior, Ocre OS deberá favorecer inicialmente la continuidad del Caso anterior.

Esto no significa afirmar que la nueva incidencia tenga la misma causa.

Significa que primero deberá descartarse razonablemente la relación con la intervención anterior antes de fragmentar el historial.

---

### 10.2 Reapertura provisional

Un Caso cerrado podrá reabrirse provisionalmente cuando exista una nueva Interacción potencialmente relacionada con él.

La reapertura deberá registrar explícitamente el motivo.

Ejemplo:

> Posible reincidencia posterior a intervención. Pendiente determinar relación con Caso anterior.

El Caso deberá entrar en un estado que represente esta incertidumbre.

**Estado provisional sugerido:**

`En evaluación de reincidencia`

Este nombre queda sujeto a validación posterior.

---

### 10.3 Clasificación técnica de la reincidencia

La relación entre la nueva incidencia y el Caso anterior no deberá decidirse únicamente por:

- cercanía temporal;
- similitud superficial del síntoma;
- opinión del cliente;
- o pertenecer al mismo Equipo.

La clasificación podrá requerir preguntas técnicas y posteriormente diagnóstico en sitio.

Las preguntas deberán adaptarse al historial real del Equipo y a la intervención realizada anteriormente.

Ejemplos de información relevante:

- síntoma actual;
- momento en que apareció;
- comportamiento del Equipo desde la intervención anterior;
- tiempo que funcionó correctamente;
- operador actual;
- cambios realizados;
- condiciones de operación;
- archivos utilizados;
- intervenciones posteriores;
- y estado de los componentes previamente reparados.

---

### 10.4 Resultados de la evaluación

Después de obtener evidencia suficiente pueden ocurrir al menos cuatro resultados.

#### A. Continuación del Caso anterior

Se determina que la nueva incidencia forma parte de la misma problemática.

El Caso continúa abierto y se conserva toda la información dentro del mismo historial.

#### B. Reincidencia relacionada

Se identifica una nueva manifestación o consecuencia relacionada con la intervención anterior.

El Caso anterior continúa siendo la referencia principal y se documenta la relación.

#### C. Problema independiente

Se determina que la nueva incidencia no corresponde al Caso anterior.

Se crea un nuevo Caso y se conserva una relación explícita con el Caso que originó la investigación.

Ejemplo:

> Caso 161 creado durante la evaluación de reincidencia del Caso 154. Se determinó que la nueva falla es independiente.

#### D. Problemas simultáneos

Se determina que existe continuidad de la falla anterior y, adicionalmente, una nueva problemática independiente.

El Caso original continúa abierto y se genera además un nuevo Caso relacionado.

---

### 10.5 Responsabilidad y asignación técnica

La posible relación con una intervención anterior debe influir en la asignación del técnico.

Cuando exista una reincidencia potencial, deberá considerarse preferentemente al técnico que realizó la intervención anterior, debido a su conocimiento del contexto.

Sin embargo, esto no será una regla absoluta.

Ocre OS deberá permitir asignar otro técnico cuando:

- el técnico anterior no esté disponible;
- la especialidad requerida sea diferente;
- la urgencia lo requiera;
- o exista otra razón operativa válida.

El nuevo técnico deberá tener acceso al historial completo necesario para continuar la atención.

---

### 10.6 Trazabilidad de la decisión

Toda decisión de:

- reabrir;
- continuar;
- separar;
- crear un nuevo Caso;
- o relacionar múltiples Casos

deberá conservar el motivo de la decisión y la evidencia disponible.

El sistema no deberá borrar la incertidumbre que existió durante el proceso.

Debe ser posible reconstruir posteriormente:

1. qué reportó el cliente;
2. por qué se sospechó una reincidencia;
3. qué se investigó;
4. qué evidencia se obtuvo;
5. y por qué finalmente se decidió continuar o crear otro Caso.

---

## 11. Principio de no pérdida de contexto

La información obtenida en una etapa no debe descartarse cuando el proceso avanza.

Cada transición debe enriquecer el historial y mantener trazabilidad completa.
