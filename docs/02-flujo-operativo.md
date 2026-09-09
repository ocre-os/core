# Flujo Operativo de Ocre OS

**Estado:** Borrador  
**Versión:** 0.2

## 1. Propósito

Definir el ciclo de vida de una atención dentro de Ocre OS, desde la primera interacción hasta la documentación, seguimiento y cierre del trabajo realizado.

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

Cuando una Interacción todavía no puede relacionarse con suficiente certeza con una persona, Organización, Solicitud o Caso existente, podrá permanecer provisionalmente como **Contacto 0 (C0)** mientras se completa su clasificación.

La cadena anterior representa una secuencia lógica del negocio y no una relación obligatoria uno a uno entre objetos.

Ejemplos:

- una Interacción puede generar una nueva Solicitud;
- una Interacción puede relacionarse con una Solicitud existente;
- una Interacción puede agregarse a un Caso existente;
- una Interacción puede permanecer temporalmente como Contacto 0 mientras se identifica su contexto;
- una Solicitud puede resolverse sin requerir una Visita;
- un Caso puede contener múltiples Servicios;
- un Servicio puede requerir múltiples Visitas;
- una Visita puede generar uno o varios Reportes;
- un Caso cerrado puede reabrirse posteriormente.

Ocre OS debe preservar la continuidad de la información independientemente del camino que siga cada atención.

---

## 3. Interacción

### Definición

Evento de comunicación entre una persona y Ocre.

Una Interacción existe desde el momento en que Ocre recibe o registra una comunicación, independientemente de que todavía se conozca o no la identidad de la persona, la Organización relacionada o el motivo completo del contacto.

Puede producirse mediante:

- llamada;
- WhatsApp;
- correo electrónico;
- formulario;
- mensaje desde el portal;
- referencia;
- contacto presencial;
- u otro medio.

Una Interacción puede relacionarse posteriormente con:

- un Contacto;
- una Organización;
- una Solicitud;
- un Caso;
- una Cita;
- un Servicio;
- o ningún elemento adicional si solo requiere conservarse como antecedente.

### Debe conservar como mínimo

- fecha y hora;
- canal;
- identificador disponible del origen;
- contenido o resumen de la comunicación;
- información proporcionada;
- origen o referencia, cuando exista;
- y responsable de clasificación o seguimiento.

### Regla de conservación

Una Interacción nunca debe eliminarse únicamente porque la información asociada ya exista.

Cuando corresponda a información existente, deberá relacionarse con el registro correcto y conservarse como parte de su historial.

Ejemplos:

- un cliente vuelve a preguntar por una Solicitud ya abierta;
- una persona genera nuevamente una Solicitud porque no encontró cómo dar seguimiento a la anterior;
- un operador utiliza un canal diferente para consultar el mismo Caso;
- un cliente vuelve a proporcionar datos que ya estaban registrados;
- una persona intenta contactar varias veces antes de recibir respuesta.

Estas Interacciones pueden no generar una nueva Solicitud ni un nuevo Caso, pero constituyen información operativa relevante.

### Valor futuro

El historial de Interacciones podrá utilizarse para analizar:

- frecuencia de contacto;
- tiempos de respuesta;
- reincidencia de consultas;
- dificultades para utilizar la plataforma;
- necesidades de capacitación;
- efectividad de canales;
- y calidad del seguimiento.

---

## 3.1 Contacto 0 (C0)

### Definición

Contacto 0 es una **clasificación provisional**, no una persona, una empresa ni una Interacción diferente.

Se utiliza cuando existe una Interacción real, pero todavía no hay información suficiente para relacionarla de manera confiable con los elementos existentes de Ocre OS o para determinar qué proceso debe iniciar.

### Entra cuando

Una Interacción requiere clasificación adicional porque todavía existe incertidumbre relevante sobre uno o varios de estos puntos:

- quién está contactando;
- a qué Organización pertenece;
- si ya existe en el sistema;
- si existe una Solicitud relacionada;
- si existe un Caso relacionado;
- cuál es la necesidad concreta;
- o qué acción debe realizarse.

### Sale cuando

Existe información suficiente para clasificar la Interacción y decidir su relación o siguiente acción.

### Resultados posibles

Un Contacto 0 puede terminar:

- relacionado con un Contacto existente;
- relacionado con una Organización existente;
- relacionado con una Solicitud existente;
- relacionado con un Caso existente;
- generando una nueva Solicitud;
- actualizando información ya existente;
- generando un Pendiente;
- o cerrándose sin acción posterior.

### Principio

**Resolver o cerrar un Contacto 0 no elimina la Interacción que lo originó.**

La Interacción permanece como parte del historial y de la trazabilidad del sistema.

---

## 3.2 Clasificación inicial

### Propósito

Determinar a qué elemento del sistema pertenece una nueva Interacción y qué acción debe realizarse como consecuencia.

La clasificación inicial evita generar innecesariamente nuevas Solicitudes o Casos cuando la comunicación corresponde a información ya existente.

### Durante la clasificación se debe intentar determinar

- quién está realizando la Interacción;
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
- Organización, si se conoce;
- Equipo, si se conoce;
- urgencia;
- evidencia inicial;
- siguiente acción.

### Sale cuando

La atención requiere seguimiento estructurado o se determina que no continuará.

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
- Solicitudes;
- Servicios;
- cotizaciones;
- pagos;
- Citas;
- Visitas;
- Reportes;
- refacciones;
- Pendientes;
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
- en evaluación de reincidencia;
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

Representar una intervención programada en una Ubicación o mediante una sesión remota.

### Debe registrar

- fecha;
- horario;
- Ubicación;
- técnicos participantes;
- actividades;
- tiempos;
- evidencias;
- mediciones;
- hallazgos;
- intervenciones;
- Pendientes;
- resultado.

### Regla

Una Visita no equivale necesariamente a un Servicio completo.

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

- Solicitud original;
- necesidad identificada;
- Equipo atendido;
- diagnóstico;
- actividades;
- evidencias;
- intervenciones;
- resultados;
- Pendientes;
- recomendaciones;
- estado final.

---

## 9. Transiciones y continuidad de los casos

Las transiciones dentro de Ocre OS deben responder a eventos reales del negocio.

Una nueva Interacción no genera automáticamente una nueva Solicitud ni un nuevo Caso.

---

### 9.1 Interacción → Clasificación inicial

Toda nueva comunicación entra primero como Interacción.

Si la información disponible es insuficiente para clasificarla con certeza, la Interacción puede permanecer provisionalmente como Contacto 0.

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
- Servicios;
- Visitas;
- refacciones;
- Reportes;
- Pendientes;
- seguimiento;
- y decisiones.

La creación de un Caso no implica necesariamente que exista todavía un diagnóstico o un Servicio autorizado.

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
